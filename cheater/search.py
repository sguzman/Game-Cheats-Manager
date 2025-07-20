"""Unified trainer search across providers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .providers import MrAntiFunProvider


@dataclass
class SearchResult:
    title: str
    url: str
    provider: str


def search_all(query: str) -> List[SearchResult]:
    """Search all providers for ``query`` and return aggregated results."""
    results: List[SearchResult] = []

    provider = MrAntiFunProvider()
    for trainer in provider.search(query):
        results.append(SearchResult(trainer.title, trainer.url, trainer.provider))

    return results
