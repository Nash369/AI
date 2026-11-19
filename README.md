# AI Coursework

This repository contains my Artificial Intelligence coursework: the weekly lab code, the results from running each lab, and my assignment work.

## Lab Overview

The code files keep the lecturer's original names, so the number in a file name is one lower than the lab number (for example, Lab 09 runs `lab08_genetic_algorithm_regression.py`).

| Week | Date | Lab | Code | Results | Submission |
| :---: | :---: | --- | --- | --- | --- |
| 4 | 2026/09/30 | Lab 02 - Search Foundations | [lab01_search_foundations.py](all_experiments/lab01_search_foundations.py) | [results/lab01](results/lab01) | - |
| 5 | 2026/10/08 | Lab 03 - Informed Search | [lab02_informed_search.py](all_experiments/lab02_informed_search.py) | [results/lab02](results/lab02) | [Assignment 2](Assignment2) |
| 6 | 2026/10/14 | Lab 04 - Search Engineering | [lab03_search_engineering.py](all_experiments/lab03_search_engineering.py) | [results/lab03](results/lab03) | - |
| 7 | 2026/10/21 | Lab 05 - Fuzzy Logic and ANFIS | [lab04_fuzzy_anfis.py](all_experiments/lab04_fuzzy_anfis.py) | [results/lab04](results/lab04) | - |
| 8 | 2026/10/28 | Lab 06 - Robotics Sensor Control | [lab05_robotics_sensor_control.py](all_experiments/lab05_robotics_sensor_control.py) | [results/lab05](results/lab05) | - |
| 9 | 2026/11/04 | Lab 07 - Handwriting OCR Evaluation | [lab06_handwriting_ocr_worked.py](all_experiments/lab06_handwriting_ocr_worked.py) | [results/lab06](results/lab06) | - |
| 10 | 2026/11/11 | Lab 08 - Airline Tweet Sentiment | [lab07_airline_sentiment.py](all_experiments/lab07_airline_sentiment.py) | [results/lab07](results/lab07) | - |
| 11 | 2026/11/18 | Lab 09 - Genetic Algorithms | [lab08_genetic_algorithm_regression.py](all_experiments/lab08_genetic_algorithm_regression.py) | [results/lab08](results/lab08) | - |

## Lab Details

**Lab 02 - Search Foundations.** Runs BFS, DFS and UCS over the OpenFlights route graph and compares path cost, number of hops and nodes expanded for three airport pairs.
Results: `metrics.csv`, `route_comparison.png`

**Lab 03 - Informed Search.** Adds GBFS, A* and Weighted A* using a Haversine distance heuristic, checks the heuristic is admissible, and compares search effort with UCS.
Results: `metrics (1).csv`, `heuristic_check.csv`, `expanded_nodes.png`

**Lab 04 - Search Engineering.** Turns the search code into the `utils/` package with pytest unit tests and a command-line tool (`python -m utils`), then benchmarks four algorithms on ten routes.
Results: `benchmark.csv`, `benchmark_summary.csv`, `benchmark_expansions.png`

**Lab 05 - Fuzzy Logic and ANFIS.** Builds a fuzzy inference system and an ANFIS model on the Air Quality dataset.
Results: `metrics.csv`, `split.csv`, `fuzzy_fixed_points.csv`, `fuzzy_memberships.png`, `fuzzy_control_surface.png`, `predicted_vs_actual.png`, `temperature_humidity.png`

**Lab 06 - Robotics Sensor Control.** Compares a rule-based controller with a decision tree on robot sensor readings and tests how each copes with sensor noise.
Results: `metrics.csv`, `split.csv`, `feature_scores.csv`, `tree_depth_validation.csv`, `rule_controller.txt`, `rule_per_class.csv`, `noise_robustness.csv`, `noise_robustness.png`, `confusion_matrices.png`

**Lab 07 - Handwriting OCR Evaluation.** Runs Tesseract OCR on 89 handwritten medicine names, with and without image preprocessing, and measures exact match, edit distance, character error rate and blank outputs before sorting the failures by type.
Results: `metrics.csv`, `predictions.csv`, `error_analysis.csv`, `sample_grid.png`, `ocr_failures.png`, `preprocessed/`

**Lab 08 - Airline Tweet Sentiment.** Trains a bag-of-words Multinomial Naive Bayes classifier on 14,640 airline tweets using a 70/15/15 split without leakage, and compares it with a majority-class baseline.
Results: `metrics.csv`, `validation_results.csv`, `per_class_metrics.csv`, `per_airline_f1.csv`, `error_analysis.csv`, `test_predictions.csv`, `split.csv`, `confusion_matrix.png`

**Lab 09 - Genetic Algorithms.** Uses a genetic algorithm to learn linear regression coefficients for medical insurance charges, checks the results over ten random seeds, compares them with ordinary least squares, and tests a smaller population.
Results: `ga_10_runs.csv`, `ga_sensitivity_pop40.csv`, `summary.csv`, `split.csv`, `convergence.png`

## Repository Structure

```
AI/
├── Assignment2/        Assignment 2 (search algorithms)
├── all_experiments/    lab code and the utils/ search package
├── results/            outputs from running each lab
└── all_datasets/       datasets used by the labs
```

## Running the Labs

```
pip install -r requirements.txt
python all_experiments/lab04_fuzzy_anfis.py
```

Run the scripts from the repository root so they can find `all_datasets/`.
