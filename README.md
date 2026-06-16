# World Cup 2026 AI Quant

World Cup 2026 AI Quant is an open research repository for **football data analysis, baseline prediction models, feature engineering experiments, and reproducible evaluation workflows** related to the 2026 FIFA World Cup. The project is intended for educational and analytical use.

The repository does not provide betting advice, guaranteed predictions, or financial recommendations. Model outputs should be treated as experimental research results that require validation and careful interpretation.

## Research Goals

| Goal | Description |
|---|---|
| Data organization | Maintain transparent tables for teams, matches, features, and results. |
| Baseline models | Compare simple statistical baselines before testing complex methods. |
| Reproducibility | Keep notebooks, scripts, and assumptions easy to review. |
| Evaluation | Use train/test splits, calibration checks, and clear metrics. |

## Repository Structure

| Path | Purpose |
|---|---|
| `data/` | Small example datasets and schemas. |
| `notebooks/` | Research notebooks and exploratory analysis. |
| `src/` | Reusable Python modules for loading data and evaluating models. |
| `docs/` | Methodology notes and evaluation policy. |
| `templates/` | Experiment report templates. |

## Suggested Workflow

1. Collect or import a documented dataset.
2. Validate missing values, duplicate records, and date consistency.
3. Build transparent baseline features such as team rating, recent form, and match context.
4. Train simple baseline models before adding complex algorithms.
5. Evaluate with accuracy, log loss, Brier score, calibration, and confidence intervals where appropriate.
6. Document limitations in every experiment report.

## Evaluation Policy

A useful model report should include the dataset version, training window, feature list, target definition, evaluation split, metrics, and known limitations. Results should never be presented as guaranteed outcomes.

## Contributing

Contributions are welcome for data schemas, reproducible notebooks, methodology reviews, and documentation improvements. Avoid unsupported performance claims and disclose assumptions clearly.

## License

This project is released under the MIT License.
