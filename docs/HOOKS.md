# Reserved hooks
Assign `HOOKS['NAME'] = fn` to install a stage. `report.json` records which hooks are installed.

| Name | Contract |
|---|---|
| `METADATA_ALIGNMENT` | `fn(meta, src_shape, ref_shape) -> {'scale': float or None}` |
| `DEM_RENDER_RELIGHT` | `fn(src_bgr, ref_bgr, meta) -> (src_for_matching, ref_for_matching)` pixel-aligned to the crops, or `None` |
| `PROPOSE_ALIGNMENTS` | `fn(src_bgr, ref_bgr, meta) -> [(name, H_src_to_ref 3x3), ...]` |
| `CHANCE_VERIFICATION` | `fn(P0, P1, H, src_shape, ref_shape) -> {'accept': bool, 'nfa': float, 'tol_px': float}` |
| `DENSE_TIE_POINTS` | `fn(src_bgr, ref_bgr, H) -> (P0 Nx2, P1 Nx2, conf N)` |
