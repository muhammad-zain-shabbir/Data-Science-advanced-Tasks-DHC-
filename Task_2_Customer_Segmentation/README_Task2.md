# 🧠 Task 2: Customer Segmentation Using Unsupervised Learning

## 📌 Objective
Segment mall customers based on their annual income and spending habits using unsupervised learning techniques. Use insights to recommend personalized marketing strategies.

---

## 📂 Dataset
- **Source:** [Kaggle – Mall Customers Dataset](https://www.kaggle.com/datasets/shwetabh123/mall-customers)
- **Features Used:**  
  - Gender  
  - Age  
  - Annual Income (k$)  
  - Spending Score (1–100)

---

## 🧹 Data Cleaning
- Standardized column names
- Renamed:
  - `genre` → `gender`
  - `annual_income_(k$)` → `income`
  - `spending_score_(1-100)` → `score`

---

## 🔍 Exploratory Data Analysis
- **Visualizations:**
  - Gender distribution
  - Age histogram
  - Income vs Spending Score scatter plot
- Helped identify diverse customer behaviors

---

## 🤖 Clustering with K-Means
- Used `income` and `score` for clustering
- Determined optimal number of clusters using **Elbow Method**
- Applied **K-Means (5 clusters)**
- Assigned cluster labels to original data

---

## 📉 Dimensionality Reduction
- **PCA:** Confirmed structure of clusters in 2D
- **t-SNE:** Highlighted well-separated, dense clusters

---

## 🎯 Marketing Strategies by Segment

**Cluster 0**  
💰 High income, 🔥 high spenders  
→ Offer loyalty rewards, memberships, early access

**Cluster 1**  
💰 High income, 📉 low spenders  
→ Send personalized offers, motivate purchase

**Cluster 2**  
💸 Low income, 🔥 high spenders  
→ Highlight discounts, bundles, referrals

**Cluster 3**  
💸 Low income, 📉 low spenders  
→ Run re-engagement campaigns and surveys

**Cluster 4**  
💵 Mid income, 📊 mid spenders  
→ Promote trending items and smart upsells

---

## 🛠️ Tools & Libraries
- Python (Jupyter Notebook)
- `pandas`, `matplotlib`, `seaborn`
- `sklearn`: KMeans, PCA, t-SNE

---

## 📁 Files in This Repo
- `customer_segmentation.ipynb`: Main notebook
- `mall_customers.csv`: Dataset
- `README.md`: Project overview

---

## ✅ Skills Demonstrated
- Unsupervised learning (K-Means)
- Dimensionality reduction (PCA, t-SNE)
- Business insight extraction from clusters
