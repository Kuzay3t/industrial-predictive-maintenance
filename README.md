# industrial-predictive-maintenance

# Industrial Predictive Maintenance

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

A comprehensive research and implementation of an AI-powered predictive maintenance system integrating Machine Learning and IoT technologies to address the growing need for efficient and reliable maintenance strategies in Nigerian industrial sectors.

---

## 📖 Overview

This project benchmarks classification performance for binary-class fault detection under real-world imbalanced data conditions. It evaluates four machine learning models and proposes a novel **stacking ensemble architecture** for fault prediction in rotating electromechanical machinery — specifically **turbines**, **pumps**, and **compressors**.

Traditional reactive maintenance leads to high costs, unplanned downtime, and production inefficiencies. This system enables early fault detection using real-time sensor data, aligned with **Industry 4.0** principles.

---

## 🔬 Research Highlights

- Benchmarks **4 ML classifiers**: Logistic Regression, Random Forest, SVM, and XGBoost
- Proposes a **stacking ensemble** (SVM + Random Forest + XGBoost as base learners; Logistic Regression as meta-learner)
- Handles **class imbalance** via algorithm-level correction (`class_weight='balanced'`)
- Applies **SHAP-based interpretability** analysis for sensor-level explainability
- Uses **McNemar's statistical test** to validate performance differences

---

## 📊 Results Summary

| Model | Accuracy | Precision | Recall | F1-Score | MCC |
|---|---|---|---|---|---|
| Logistic Regression | 0.9420 | 0.9848 | 0.4248 | 0.5936 | 0.4023 |
| Random Forest | 0.9831 | 0.9635 | 0.8627 | 0.9103 | 0.8801 |
| XGBoost | 0.9798 | 0.9552 | 0.8366 | 0.8920 | 0.8720 |
| SVM | 0.9779 | 1.0000 | 0.7778 | 0.8750 | 0.8800 |
| **Stacking Ensemble** | **0.9837** | **0.9706** | **0.8627** | **0.9135** | **0.9065** |

> The stacking ensemble achieved the highest overall performance with an AUC of **0.987**.

---

## 🗂️ Repository Structure
