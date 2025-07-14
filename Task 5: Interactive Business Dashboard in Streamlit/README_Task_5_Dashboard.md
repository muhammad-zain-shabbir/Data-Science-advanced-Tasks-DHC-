
# 📊 Task 5: Interactive Business Dashboard in Streamlit

## ✅ Objective
Develop an interactive dashboard for analyzing sales, profit, and segment-wise performance using the Global Superstore dataset.

---

## 📂 Dataset Used
- **Name:** Sample - Superstore.csv
- **Source:** [Kaggle - Global Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **File used in this task:** `global_superstore.csv` (renamed from the original)


---

## 🛠️ Tools and Libraries
- Python
- Streamlit
- Pandas
- Plotly

---

## 🧹 Data Preprocessing
- Loaded CSV file using Pandas with proper encoding.
- Parsed `Order Date` to datetime.
- Removed missing values in critical columns.
- Ensured proper data types for plotting.

---

## 🎯 Dashboard Features

### 🔍 Sidebar Filters
- Filter by **Region**
- Filter by **Category**

### 📈 KPIs Displayed
- **Total Sales**
- **Total Profit**
- **Total Orders**

### 📊 Visualizations
- **Bar Chart**: Sales by Sub-Category
- **Line Chart**: Sales over Time
- **Pie Chart**: Profit Distribution by Region
- **Bar Chart**: Top 5 Customers by Sales

---

## 📁 Files Included in This Task

| File Name | Description |
|-----------|-------------|
| `dashboard_app.py` | Main Streamlit app code |
| `global_superstore.csv` | Dataset (renamed from Sample - Superstore.csv) |
| `README.md` | Project documentation |
| `Task_5_Streamlit_Dashboard_Reference.ipnyb |

---

## 🚀 How to Run

1. Install Streamlit if not already:
```bash
pip install streamlit
```

2. Navigate to the project directory in your terminal:
```bash
cd path/to/your/project
```

3. Run the app:
```bash
streamlit run dashboard_app.py
```

---

## 📌 Skills Demonstrated
- Business Intelligence (BI) dashboarding
- Data storytelling and KPI visualization
- Streamlit user interactivity
- Plotly chart integration

---

## 📣 Result
An interactive, browser-based dashboard that helps users visualize and analyze business performance across regions and categories.

