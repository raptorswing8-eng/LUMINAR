import os, sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import nbload

@pytest.fixture(scope="session")
def ns(tmp_path_factory):
    os.chdir(tmp_path_factory.mktemp("work"))
    return nbload.load()
