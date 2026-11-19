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
