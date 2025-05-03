# OMR Evaluation Pipeline

This project provides a pipeline for evaluating Optical Music Recognition (OMR) outputs against ground-truth MusicXML files using [Mupix](https://github.com/deepio/mupix), a Python-based tool for symbolic music comparison.

## Structure of the Code and Files

| File / Folder                  | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `run_mupix_comparisons.sh`    | Shell script to batch-run Mupix comparisons between OMR outputs and ground truth |
| `evaluate_omr_performance.py` | Summarizes Mupix results, generates category-wise accuracy metrics and visualizations |
| `/pdf_excerpts/`              | Source PDF excerpts used as input to OMR tools                              |
| `/ground_truth/`              | Hand-encoded MusicXML files (ground truth)                                  |
| `/omr_outputs/`               | Subfolders for each OMR tool’s MusicXML output (`newzik/`, `photoscore/`, etc.) |
| `/mupix_results/`             | JSON outputs from Mupix comparison runs                                     |
| `/evaluation/`                | Summary CSVs and generated performance plots                                |

## Usage

1. Run comparisons between OMR outputs and ground truth:

   ```bash
   bash run_mupix_comparisons.sh
    ````

2. Analyze and visualize results:

   ```bash
   python evaluate_omr_performance.py
   ```

   Output files will be stored in the `evaluation/` directory:

   * `omr_category_summary.csv`
   * `omr_skipped_files.csv`
   * `category_accuracy_summary.csv`
   * `accuracy_by_category_tool.png`
   * `total_accuracy_per_tool.png`


## Tool Reference

This project uses the open-source tool **Mupix** for symbolic MusicXML evaluation.

* *Daigle, Alexandre. “Evaluation of Optical Music Recognition Software.” Master’s Thesis, McGill University, 2020.*
  [[Thesis]](https://escholarship.mcgill.ca/concern/theses/mk61rn440)
  [[GitHub Repo]](https://github.com/deepio/mupix)


