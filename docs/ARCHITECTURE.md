# Architecture

```
input (upload / zip / Drive / path; .IMG converter) -> detect, trim, orient, scale-match
  -> [METADATA_ALIGNMENT hook] -> [DEM_RENDER_RELIGHT hook]
  -> candidates: multi-scale RootSIFT | simulated tilted views | SuperPoint + LightGlue | [PROPOSE_ALIGNMENTS hook]
  -> Lunar Structural Graph filter (triangle side-ratio consistency, iterative pruning)
  -> uniform grid selection
  -> model selection: MAGSAC++ | spread-RANSAC | manual seed (accuracy tiers, coverage-aware score)
  -> [CHANCE_VERIFICATION hook] -> Huber refinement -> optional TPS correction (only if held-out error improves)
  -> [DENSE_TIE_POINTS hook]
  -> metrics (held-out RMSE, uniformity, SSIM/NCC) -> verdict -> exports + dashboard
```
Brightness depends on shape, albedo, sun and view, so structure rather than intensity is matched. Model selection is coverage-aware because a model fitted to one clustered patch can look perfect and be wrong elsewhere. Metrics are held out because fit residuals flatter the model.
