"""Load the pipeline definitions (and the Cell 9 self-test) straight from notebooks/LUMINAR.ipynb.
No second copy of the code exists. Used by the tests and by make_example.py."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
ROOT = Path(__file__).resolve().parents[1]
NB = ROOT / "notebooks" / "LUMINAR.ipynb"
MARKERS = ("CELL 0b", "Cell 3 ", "Cell 4 ", "Cell 5 ", "Cell 6 ", "Cell 7", "Cell 8a", "Cell 8b", "Cell 9 ")

def load():
    g = {"__name__": "luminar_nb"}
    for c in json.load(open(NB))["cells"]:
        if c["cell_type"] != "code": continue
        s = "".join(c["source"])
        if any(m in s[:120] for m in MARKERS) or "def hartley(" in s:
            exec(compile(s, "notebook-cell", "exec"), g)
    g["CFG"]["show"] = False
    return g
