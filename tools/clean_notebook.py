"""Clean a Colab notebook for publishing: clear outputs, drop widget state, blank personal share links.
Usage: python tools/clean_notebook.py in.ipynb out.ipynb"""
import json, re, sys
src, dst = sys.argv[1:3]
nb = json.load(open(src))
for c in nb["cells"]:
    if c["cell_type"] == "code":
        c["outputs"] = []; c["execution_count"] = None
    c.get("metadata", {}).pop("colab", None)
    s = "".join(c["source"]) if isinstance(c["source"], list) else c["source"]
    s = re.sub(r'IMG_INPUT = "https://drive\.google\.com[^"]*"', 'IMG_INPUT = ""', s)
    c["source"] = s.splitlines(keepends=True)
nb["metadata"].pop("widgets", None)
nb["metadata"].pop("colab", None)
json.dump(nb, open(dst, "w"), indent=1, ensure_ascii=False)
