# 🌌 Sloan Digital Sky Survey (SDSS) – Galaxy Classification using Machine Learning

This repository focuses on **classifying galaxies** from the **Sloan Digital Sky Survey (SDSS)** dataset using various **machine learning techniques**.  
The goal is to build accurate models capable of identifying galaxy types based on photometric and spectral features.

---

## 📌 Project Overview

- Utilizes SDSS photometric/spectral data including:  
  **u, g, r, i, z magnitudes**, redshift values, positional coordinates, and derived features.
- Performs **data preprocessing**, feature engineering, and visualization.
- Applies multiple ML algorithms to classify galaxies into:  
  **Elliptical**, **Spiral**, and **Irregular** categories.
- Compares performance across different models.

---

## 🛠️ Workflow

1. **Data Collection**  
   Collect SDSS data (CSV or via SkyServer SQL query).

2. **Exploratory Data Analysis (EDA)**  
   - Visualization of distributions  
   - Correlation heatmaps  
   - Feature insights

3. **Data Preprocessing**  
   - Missing value handling  
   - Scaling/Normalization  
   - Feature selection

4. **Model Training & Evaluation**  
   Models used:
   - Logistic Regression  
   - SVM  
   - Random Forest  
   - KNN  
   - Gradient Boosting / XGBoost (optional)  
   - Neural Networks (optional)

   Metrics:
   - Accuracy  
   - Precision  
   - Recall  
   - F1-score  
   - ROC-AUC  

5. **Results & Comparison**  
   - Confusion matrices  
   - Feature importance  
   - Model comparison table

---

## 📁 Repository Structure
├── data/<br>
│ └── sdss_galaxy_data.csv<br>
├── notebooks/<br>
│ └── SDSS_Galaxy_Classification.ipynb<br>
├── src/<br>
│ ├── preprocessing.py<br>
│ ├── models.py<br>
│ ├── evaluation.py<br>
├── results/<br>
│ └── plots/<br>
└── README.md


---

## 📊 Results Summary

- Models achieve high accuracy for galaxy type classification.
- Tree-based models (Random Forest, Gradient Boosting) often perform the best.
- Strong visual insights via plotted metrics (CM, ROC, Feature Importance).

---

## 🔍 Dataset Source

Data obtained from the **Sloan Digital Sky Survey (SDSS)** – SkyServer.  
More info: *SDSS DR (Data Releases)*.

---

## 💡 Future Enhancements

- Deep learning–based classification using galaxy images.
- Integration of multi-survey data (DES, Pan-STARRS).
- Web deployment of the final trained model.

---
