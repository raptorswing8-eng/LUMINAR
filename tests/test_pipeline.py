"""Known-answer tests on a synthetic crater pair (true transform known)."""
from pathlib import Path

def test_pipeline_cells_define_api(ns):
    for n in ("run_pipeline", "run_selftest", "HOOKS", "hook_status", "apply_H"):
        assert n in ns, n

def test_recovers_known_transform_moderate_sun_change(ns):
    R = ns["run_selftest"](light_delta=20)
    assert R["level"] in ("HIGH", "MEDIUM")
    assert R["gt_err"].mean() < 1.0

def test_exports_exist(ns):
    ns["run_selftest"](light_delta=20)
    for f in ("registered.png", "match_points.csv", "report.json", "dashboard.png"):
        assert (Path("selftest_out") / f).exists(), f

def test_fails_safely_with_no_common_appearance(ns):
    R = ns["run_selftest"](light_delta=100)
    assert R["level"] != "HIGH"

def test_hooks_default_to_placeholders(ns):
    assert set(ns["hook_status"]().values()) == {"placeholder"}
