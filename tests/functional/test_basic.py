import os
from pathlib import Path

from sphinx.cmd.build import build_main


CURRENT_DIR = Path(__file__).resolve().parent
TEST_DIR = CURRENT_DIR.parent
DOCS_DIR = TEST_DIR.parent / "docs"


def test_basic(tmp_path):
    assert build_main([os.fspath(DOCS_DIR), os.fspath(tmp_path / "html")]) == 0
