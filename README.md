
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
industrial-predictive-maintenance/
│
├── AI_IoT_Predictive_Maintenance_Analysis.ipynb  # Main analysis notebook
├── equipment_anomaly_data.csv                    # Dataset (7,672 sensor records)
├── requirements.txt                              # Python dependencies
├── setup.py                                      # Package installation
├── pyproject.toml                                # Modern Python config
│
├── Box plot of dataset.png
├── ML processing pipeline flowchart.png
├── ROC curve performance plotted against the f...
├── comparative confusion matrix of four models...
├── comparative scatter plot of dataset.png
├── plot of dataset features after preprocessing...
├── plot of dataset features before preprocessing...
├── precision-recall curve.png
├── primary metric comparison.png
├── training-testing curve.png
│
├── CONTRIBUTING.md
├── LICENSE
└── README.md


---

## 🚀 Usage

Launch the main analysis notebook:

```bash
jupyter notebook AI_IoT_Predictive_Maintenance_Analysis.ipynb
```

The notebook walks through the full pipeline: data loading → EDA → preprocessing → model training → evaluation → SHAP interpretability.

---

## 🔍 Key Findings

- **Temperature and pressure** are the most influential fault predictors (SHAP analysis)
- **Vibration × Temperature interaction** produces a compounding fault signal — simultaneous anomalies in both sensors are far more indicative of failure than either alone
- **Logistic Regression** fails to capture non-linear sensor interaction patterns, confirming the fault-detection problem is inherently non-linear
- The **stacking ensemble** successfully combines SVM's precision discipline and XGBoost's fault-detection aggressiveness into a more balanced unified architecture
- All pairwise model performance differences were statistically significant (McNemar's test, α = 0.05)

---

## 🏭 Application Context

This system targets rotating electromechanical machinery critical to:
- ⚡ National power generation
- 🛢️ Oil and gas operations
- 🏗️ Manufacturing facilities

It provides a practical pathway for Nigerian industries to transition from reactive/preventive maintenance toward intelligent, data-driven operations aligned with **Industry 4.0**.

---

## 📄 Citation

If you use this work, please cite:

```bibtex
@article{kuzayet2026benchmarking,
  title={Benchmarking Classification Performance for Binary-Class Fault Detection Under Real-World Imbalanced Data Conditions},
  author={Kuzayet, Bagai Glory and Honour, Eje Obed and Bala, Jibril Abdullahi},
  institution={Federal University of Technology Minna},
  year={2026}
}
```

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get involved.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Bagai Glory Kuzayet** — kuzayet.m2204354@st.futminna.edu.ng
- **Eje Obed Honour** — obed.m2200396@st.futminna.edu.ng
- **Jibril Abdullahi Bala** — jibril.bala@futminna.edu.ng

*Department of Mechatronics Engineering, Federal University of Technology Minna, Niger State, Nigeria*
