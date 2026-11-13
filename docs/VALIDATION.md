# Validation
Synthetic crater field warped by a known transform; error is measured on a 12x12 grid in reference pixels (`run_selftest`).
Reproduce: `pytest -q`, or `python tools/make_example.py` for the dashboard.

| Sun change | Mode | Result |
|---|---|---|
| 20° | automatic | HIGH; mean error 0.17 px, max 0.27 px (RootSIFT-only CPU run, current notebook) |
| 100° | automatic | must not be HIGH (test asserts it); previously measured as FAILED |

These are synthetic results, not a labelled Chandrayaan-2 benchmark. Real oblique-vs-nadir pairs currently give LOW or FAILED verdicts (see Limitations in the README).
