"""MrAntiFun trainer provider."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List
from urllib.parse import quote_plus, urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://mrantifun.net"
SEARCH_URL = BASE_URL + "/index.php?search/1&q={query}&o=date"


@dataclass
class Trainer:
    """Representation of a trainer result."""

    title: str
    url: str
    provider: str = "MrAntiFun"


class MrAntiFunProvider:
    """Provider for scraping trainers from mrantifun.net."""

    def search(self, query: str) -> List[Trainer]:
        """Search the MrAntiFun forums for trainers matching ``query``."""
        encoded = quote_plus(query)
        resp = requests.get(SEARCH_URL.format(query=encoded), timeout=15)
        resp.raise_for_status()
        return list(self.parse_search_results(resp.text))

    @staticmethod
    def parse_search_results(html: str) -> Iterable[Trainer]:
        """Parse search results HTML and yield :class:`Trainer` objects."""
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.select("h3.contentRow-title a"):
            title = re.sub(r"\s+", " ", link.get_text(strip=True))
            url = urljoin(BASE_URL, link.get("href"))
            yield Trainer(title=title, url=url)
