from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from cheater.providers.mrantifun import MrAntiFunProvider


def test_parse_search_results(tmp_path):
    sample_html = (
        Path(__file__).with_name("sample_search.html").read_text(encoding="utf-8")
    )
    provider = MrAntiFunProvider()
    results = list(provider.parse_search_results(sample_html))
    assert results, "No results parsed"
    first = results[0]
    assert first.title
    assert first.url.startswith("https://mrantifun.net/"), first.url
