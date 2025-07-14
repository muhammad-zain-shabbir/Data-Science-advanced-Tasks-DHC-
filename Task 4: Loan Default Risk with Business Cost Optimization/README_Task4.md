
# 🏦 Task 4: Loan Default Risk with Business Cost Optimization

This project focuses on predicting loan default risk and optimizing the decision threshold by integrating business cost considerations into machine learning model evaluation.

---

## 📌 Objective

- Train binary classification models to predict the probability of loan default.
- Define business-specific costs for misclassification (false positives and false negatives).
- Adjust model threshold to minimize total financial cost.

---

## 📂 Dataset

- **Name:** Home Credit Default Risk – Application dataset  
- **File Used:** `application_train.csv` 
- **Source:** [Kaggle Dataset Link](https://www.kaggle.com/competitions/home-credit-default-risk/data?select=application_train.csv)

---

## 🧪 Project Workflow

### 1. Load & Inspect Data
- Loaded `application_train.csv` and checked dimensions and column types.

### 2. Data Cleaning & Preprocessing
- Dropped columns with >40% missing values.
- Removed remaining rows with missing data.
- Label encoded categorical features.

### 3. Model Development
- Models used:
  - Logistic Regression
  - CatBoostClassifier
- Evaluated using accuracy score and confusion matrix.

### 4. Business Cost Optimization
- Cost assumptions:
  - False Positive (FP): ₹5000
  - False Negative (FN): ₹1000
- Predicted probabilities from CatBoost.
- Iterated over multiple thresholds to compute total cost.
- Identified the threshold with the lowest cost.

### 5. Visualization & Interpretation
- Confusion Matrix displayed as a heatmap for CatBoost predictions.
- Bar chart comparing accuracy of Logistic Regression and CatBoost.
- Detailed classification reports printed for both models.

---

## 📊 Results & Insights

- **Logistic Regression Accuracy:** ~91.36%
- **CatBoost Accuracy:** ~91.37%
- **Optimal Threshold:** Displayed in notebook output.
- **Minimum Total Cost:** Displayed in notebook output.

- CatBoost performed slightly better.
- Visualization helps interpret model effectiveness.
- Threshold optimization can significantly reduce financial impact.

---

## 🛠️ Tools & Libraries

- Python, Jupyter Notebook
- Libraries: `pandas`, `numpy`, `scikit-learn`, `catboost`, `seaborn`, `matplotlib`

---

## 📁 Project Structure

```
task4_loan_default_risk/
├── application_train.csv (this was a large file so it has been compressed in a folder and it's name is: compressed_data.csv.gz) 
├── loan_default_risk_optimization.ipynb
└── README.md
```

---

## ✅ Submission Checklist

- [x] Jupyter Notebook with well-structured code and markdown
- [x] Data cleaning, encoding, modeling, and threshold tuning
- [x] Visuals: Confusion matrix, accuracy comparison
- [x] Business cost analysis for threshold tuning
- [x] Final README.md included
