"""Contrôles de la sortie HTML, sans navigateur ni dépendance."""
import json
import unittest
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://www.ladelicieuserie.fr"
INDEXED = {"/", "/devis/", "/biscuits-personnalises/", "/biscuits-mariage/",
           "/biscuits-entreprise/", "/biscuits-fetes-de-famille/", "/biscuiterie-calais/"}


class Page(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.tags = []
        self.values = {}
        self.capture = None
        self.feed(file.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == "title" or (tag == "script" and attrs.get("type") == "application/ld+json"):
            self.capture = tag
            self.values[tag] = ""

    def handle_endtag(self, tag):
        if self.capture == tag:
            self.capture = None

    def handle_data(self, text):
        if self.capture:
            self.values[self.capture] += text

    def find(self, tag, **filters):
        return [attrs for name, attrs in self.tags if name == tag and
                all(attrs.get(k) == v for k, v in filters.items())]


def as_file(path):
    return ROOT / (unquote(path).lstrip("/") + ("index.html" if path.endswith("/") else ""))


paths = INDEXED | {"/confidentialite/", "/mentions-legales/", "/404.html", "/thanks.html"}
pages = {path: Page(as_file(path)) for path in paths}


class Site(unittest.TestCase):
    def test_metadata_and_graph(self):
        titles, descs = set(), set()
        for path, page in pages.items():
            with self.subTest(path=path):
                self.assertEqual(len(page.find("h1")), 1)
                self.assertEqual(len(page.find("main")), 1)
                self.assertEqual(page.find("html")[0]["lang"], "fr")
                title = page.values["title"].strip()
                desc = page.find("meta", name="description")[0]["content"]
                self.assertTrue(title and desc)
                self.assertNotIn(title, titles)
                self.assertNotIn(desc, descs)
                titles.add(title)
                descs.add(desc)
                if path != "/404.html":
                    self.assertEqual(page.find("link", rel="canonical")[0]["href"], DOMAIN + path)
                indexed = not any("noindex" in m["content"] for m in page.find("meta", name="robots"))
                self.assertEqual(indexed, path in INDEXED)
                for prop in ("og:title", "og:description", "og:image", "og:url", "og:locale"):
                    self.assertTrue(page.find("meta", property=prop)[0]["content"])
                graph = json.loads(page.values["script"])["@graph"]
                self.assertFalse(any(e["@type"] in {"Review", "AggregateRating"} for e in graph))
                if path in INDEXED - {"/"}:
                    crumb = next(e for e in graph if e["@type"] == "BreadcrumbList")
                    self.assertEqual([x["item"] for x in crumb["itemListElement"]], [DOMAIN + "/", DOMAIN + path])
                ids = Counter(a["id"] for _, a in page.tags if "id" in a)
                self.assertFalse({i for i,n in ids.items() if n != 1})

    def test_all_local_links_and_images(self):
        for path, page in pages.items():
            with self.subTest(path=path):
                targets = [a["href"] for a in page.find("a")]
                targets.extend(a["src"] for _, a in page.tags if a.get("src"))
                targets.extend(a["href"] for a in page.find("link") if a.get("href"))
                for img in page.find("img"):
                    self.assertTrue(all(k in img for k in ("width","height","alt")))
                    targets.extend(candidate.split()[0] for candidate in img.get("srcset","").split(",") if candidate.strip())
                for target in targets:
                    u = urlsplit(urljoin(DOMAIN+path, target))
                    self.assertNotIn("contact@exemple.fr", target)
                    if u.scheme != "https" or u.netloc != "www.ladelicieuserie.fr":
                        continue
                    self.assertTrue(as_file(u.path).is_file(), target)
                    if u.fragment:
                        self.assertIn(u.fragment, [a.get("id") for _,a in pages[u.path].tags], target)
                if path in INDEXED - {"/devis/"}:
                    self.assertIn("/devis/", targets)

    def test_sitemap_and_form(self):
        ns = {"s":"http://www.sitemaps.org/schemas/sitemap/0.9"}
        locations = [e.text for e in ElementTree.parse(ROOT/"sitemap.xml").findall(".//s:loc",ns)]
        self.assertCountEqual(locations, [DOMAIN+p for p in INDEXED])
        self.assertIn(DOMAIN+"/sitemap.xml", (ROOT/"robots.txt").read_text())
        form = pages["/devis/"].find("form")[0]
        self.assertEqual((form["method"],form["action"]), ("post","https://formsubmit.co/ladelicieuserie@gmail.com"))
        fields = pages["/devis/"].find("input")
        self.assertEqual([f["value"] for f in fields if f["name"]=="_next"],[DOMAIN+"/thanks.html"])
        self.assertTrue(any(f["name"]=="_honey" for f in fields))
        self.assertFalse(any(f["name"]=="next" for f in fields))


if __name__ == "__main__":
    unittest.main()
