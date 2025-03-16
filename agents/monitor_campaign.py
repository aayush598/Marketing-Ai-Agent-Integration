import pandas as pd
import os

# Folder for monitoring CSV files
DATA_FOLDER = "media/monitoring_data"

# Ensure folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Define file paths
SALES_FILE = os.path.join(DATA_FOLDER, "sales_data.csv")
COMPETITOR_FILE = os.path.join(DATA_FOLDER, "competitor_activity.csv")
BUDGET_FILE = os.path.join(DATA_FOLDER, "budget_utilization.csv")
EFFICIENCY_FILE = os.path.join(DATA_FOLDER, "operational_efficiency.csv")
LEADS_FILE = os.path.join(DATA_FOLDER, "lead_conversion.csv")

def monitor_campaign(product_name, product_features, description, audience, platform):
    """Track and measure marketing campaign performance using CSV data."""

    print(f"📊 Monitoring campaign performance for {product_name} on {platform}...")

    # Load CSV files
    sales_df = load_csv(SALES_FILE)
    competitor_df = load_csv(COMPETITOR_FILE)
    budget_df = load_csv(BUDGET_FILE)
    efficiency_df = load_csv(EFFICIENCY_FILE)
    leads_df = load_csv(LEADS_FILE)

    # ✅ 1. Sales & Customer Satisfaction Tracking
    sales_performance = f"{len(sales_df)} customers"
    avg_satisfaction = f"{sales_df['customer_satisfaction'].mean():.2f}/100" if not sales_df.empty else "N/A"
    feedback_summary = summarize_feedback(sales_df)

    # ✅ 2. Competitor Activity Tracking
    latest_competitor_activity = competitor_df["competitor_activity"].dropna().tolist() if not competitor_df.empty else ["No recent competitor activity"]

    # ✅ 3. Budget Utilization
    total_income = budget_df[budget_df["transaction_type"] == "income"]["amount"].sum() if not budget_df.empty else 0
    total_expense = budget_df[budget_df["transaction_type"] == "expense"]["amount"].sum() if not budget_df.empty else 0
    budget_utilization = f"${total_expense} spent from ${total_income} budget"

    # ✅ 4. Operational Efficiency Review
    avg_efficiency_score = f"{efficiency_df['efficiency_score'].mean():.2f}/100" if not efficiency_df.empty else "N/A"
    efficiency_status = "Optimal" if float(avg_efficiency_score.split("/")[0]) > 75 else "Needs Improvement"

    # ✅ 5. Lead Conversion Statistics
    lead_conversion_rate = f"{leads_df['conversion_rate'].mean():.2f}%" if not leads_df.empty else "N/A"

    # Return monitoring metrics
    return {
        "sales_performance": sales_performance,
        "lead_conversion_rate": lead_conversion_rate,
        "customer_feedback": feedback_summary,
        "satisfaction_score": avg_satisfaction,
        "competitor_activity": latest_competitor_activity,
        "budget_utilization": budget_utilization,
        "operational_efficiency": efficiency_status,
    }

def load_csv(file_path):
    """Load CSV file into a DataFrame, handling missing files."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"⚠ CSV file not found: {file_path}")
        return pd.DataFrame()  # Return empty DataFrame if file doesn't exist

def summarize_feedback(df):
    """Summarize customer feedback from sales data."""
    if df.empty or "customer_feedback" not in df.columns:
        return "No feedback data available."
    
    positive_feedback = df[df["customer_feedback"].str.contains("good|excellent|amazing|positive", case=False, na=False)]
    negative_feedback = df[df["customer_feedback"].str.contains("bad|poor|negative|slow", case=False, na=False)]

    return f"{len(positive_feedback)} positive, {len(negative_feedback)} negative reviews."
