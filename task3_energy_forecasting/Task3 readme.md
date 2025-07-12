# 🔋 Task 3: Energy Consumption Time Series Forecasting

This project forecasts short-term household energy usage using time-stamped power consumption data. It involves cleaning, transforming, and modeling the data using three different forecasting techniques:

- **Prophet** (for capturing trends and seasonality)
- **ARIMA** (a classical statistical model)
- **XGBoost** (a machine learning approach)

---

## 📌 Objective

To build predictive models that can estimate future household energy consumption, compare model performance, and visualize key trends and components in the data.

---

## 📂 Dataset

- **Name:** Household Power Consumption Dataset
- **Format:** CSV (`Electricity_consumption.csv`)
- **Key Columns:**
  - `Date`, `Time` — combined into a single `datetime` field
  - `Global_active_power` — target variable (energy usage in kilowatts)
  - `Voltage`, `Global_intensity`, and three sub-metering columns

---

## 🧪 Project Workflow

### 🔹 1. Data Preprocessing
- Loaded dataset and handled mixed-type warnings
- Combined `Date` and `Time` into a `datetime` column
- Converted all relevant columns to numeric format
- Handled missing values with `errors='coerce'`
- Set `datetime` as the index
- Resampled data to **daily average power consumption**

### 🔹 2. Feature Engineering
- Extracted date-based features:
  - `year`, `month`, `day`, `weekday`, `is_weekend`

---

## 🔮 Model 1: Prophet Forecasting

- Used Facebook's Prophet library
- Renamed columns to `ds` and `y` as required by Prophet
- Trained on daily global active power data
- Forecasted 30 days into the future
- Visualized:
  - Forecast with confidence intervals
  - Seasonal components (trend, weekly seasonality)

---

## 📉 Model 2: ARIMA Forecasting

- Used `statsmodels` ARIMA with (p,d,q) = (5,1,2)
- Trained on the cleaned time series data
- Forecasted 30 future time points
- Displayed observed vs forecasted data on a line plot
- Addressed warnings related to unsupported datetime indexing

---

## 🤖 Model 3: XGBoost Forecasting

- Used `xgboost` for lag-based forecasting
- Created `lag1` feature as the main input
- Split data into train and test sets
- Trained `XGBRegressor`
- Evaluated using RMSE (Root Mean Squared Error)
- Plotted actual vs predicted results

---

## 📊 Visualizations

- Line plots for model comparisons
- Prophet seasonal component plots
- RMSE metric printed for XGBoost performance
- Forecast visualizations with annotations

---

## ⚖️ Model Comparison

| Model    | Forecasting Type     | Strengths                          | Limitations                     |
|----------|----------------------|------------------------------------|---------------------------------|
| Prophet  | Seasonality-aware    | Easy to interpret, trend detection | Slower, slightly heavy          |
| ARIMA    | Statistical          | Simple and interpretable           | Lacks built-in seasonality      |
| XGBoost  | Machine Learning     | Handles nonlinearities well        | Requires careful feature setup  |

---

## 🛠️ Tools & Libraries

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `statsmodels` (for ARIMA)
- `prophet` (for trend-seasonality modeling)
- `xgboost` and `scikit-learn` (for machine learning)

---

## ✅ Key Learnings

- Time series data often needs careful datetime parsing and resampling
- Prophet provides excellent interpretability through component plots
- ARIMA is useful for quick statistical modeling
- XGBoost is powerful for machine learning forecasting with feature engineering
- RMSE and visual plots are essential to compare model effectiveness

---

## 📁 Files in This Folder

- `energy_forecasting.ipynb` — Main Jupyter notebook
- `Electricity_consumption.csv` — Dataset file (this was a large file so it was compressed in a zipfile for smoother and easy access.)
- `README.md` — This summary file

---

## 📌 Task Summary (Submission-Ready)

- ✅ Jupyter Notebook with code, graphs, and markdown
- ✅ Data cleaning, feature engineering, model training, and evaluation
- ✅ Visualizations for all models
- ✅ This `README.md` file for documentation
