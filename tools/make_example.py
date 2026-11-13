"""Regenerate examples/selftest_dashboard.png by running the notebook's own pipeline on the synthetic pair.
Run from the repo root:  python tools/make_example.py"""
import os, shutil, tempfile
from pathlib import Path
import nbload
out = Path(__file__).resolve().parents[1] / "examples"
os.chdir(tempfile.mkdtemp())
g = nbload.load()
R = g["run_selftest"](light_delta=20)
print("verdict:", R["level"], "| ground-truth mean error (px):", round(float(R["gt_err"].mean()), 3))
shutil.copy("selftest_out/dashboard.png", out / "selftest_dashboard.png")
