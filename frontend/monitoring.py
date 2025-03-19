import streamlit as st
import pandas as pd

def display_monitoring_section():
    """Displays monitoring data from CSV files in a metrics format."""
    st.subheader("📊 Monitoring Dashboard")

    # Load sales data
    sales_data = pd.read_csv("media/monitoring_data/sales_data.csv")
    st.metric(label="📈 Total Customers", value=len(sales_data))
    avg_satisfaction = sales_data["customer_satisfaction"].mean()
    st.metric(label="😊 Avg Customer Satisfaction", value=round(avg_satisfaction, 2))

    # Load competitor data
    competitors = pd.read_csv("media/monitoring_data/competitor_activity.csv")
    st.metric(label="🏆 Active Competitors", value=len(competitors))

    # Load budget data
    budget = pd.read_csv("media/monitoring_data/budget_utilization.csv")
    total_expense = budget[budget["transaction_type"] == "expense"]["amount"].sum()
    total_income = budget[budget["transaction_type"] == "income"]["amount"].sum()
    st.metric(label="💰 Total Budget Utilized", value=f"${total_expense}")

    # Load operational efficiency data
    efficiency_data = pd.read_csv("media/monitoring_data/operational_efficiency.csv")
    avg_efficiency = efficiency_data["efficiency_score"].mean()
    st.metric(label="⚡ Operational Efficiency", value=f"{round(avg_efficiency, 2)}%")
