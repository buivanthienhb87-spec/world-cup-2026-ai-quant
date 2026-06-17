# World Cup 2026 AI Quant
## Resource Portals

Quick access to external reference portals tracked by this project:

- [18wenku.com](https://18wenku.com)
- [birdsdot.com](https://birdsdot.com)


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

## Expanded Project Structure

This repository has been expanded into a fuller open-source project with reusable source modules, tests, sample data, documentation, examples, and maintenance files. The goal is to make the project understandable to visitors, useful to contributors, and suitable for long-term indexing by GitHub and general search engines.

| Area | Added content |
|---|---|
| Source code | `src/world_cup_2026_ai_quant/` contains lightweight reusable modules. |
| Tests | `tests/` contains baseline tests for the core helpers. |
| Data | `data/` contains small structured sample datasets. |
| Documentation | `docs/` explains architecture, methodology, review rules, or maintenance practices. |
| Examples | `examples/` shows how to use the project modules or data. |
| Automation | `.github/workflows/validate.yml` runs basic validation on pushes and pull requests. |

## Development Workflow

Clone the repository, install it in editable mode, and run the tests. The project intentionally keeps dependencies minimal so contributors can review and extend it quickly.

```bash
git clone https://github.com/buivanthienhb87-spec/world-cup-2026-ai-quant.git
cd world-cup-2026-ai-quant
python -m pip install -e .
python -m pytest -q
```

## Recommended Websites

A curated list of official and reliable reference websites is available in [`docs/recommended-websites.md`](docs/recommended-websites.md). These links are intended to support verification, documentation, learning, and responsible project maintenance.
