
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")
st.title("📊 Global Superstore Dashboard")

# Load data
df = pd.read_csv("global_superstore.csv", encoding='ISO-8859-1')
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df.dropna(subset=['Order Date', 'Sales', 'Profit', 'Customer Name'], inplace=True)
df['Sales'] = df['Sales'].astype(float)

# Sidebar filters
regions = st.sidebar.multiselect("Select Region:", df['Region'].unique(), default=df['Region'].unique())
categories = st.sidebar.multiselect("Select Category:", df['Category'].unique(), default=df['Category'].unique())

# Filter data
filtered_df = df[(df['Region'].isin(regions)) & (df['Category'].isin(categories))]

# KPIs
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = len(filtered_df)

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.metric("🧾 Total Orders", total_orders)

# Charts
st.subheader("Sales by Sub-Category")
fig1 = px.bar(filtered_df.groupby("Sub-Category")["Sales"].sum().sort_values().reset_index(), x="Sales", y="Sub-Category", orientation="h")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Sales Trend Over Time")
fig2 = px.line(filtered_df.groupby("Order Date")["Sales"].sum().reset_index(), x="Order Date", y="Sales")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Profit by Region")
fig3 = px.pie(filtered_df, names='Region', values='Profit', title='Profit Distribution')
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Top 5 Customers by Sales")
top_customers = filtered_df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(5).reset_index()
fig4 = px.bar(top_customers, x="Customer Name", y="Sales", title="Top 5 Customers")
st.plotly_chart(fig4, use_container_width=True)
