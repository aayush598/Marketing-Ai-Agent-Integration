import random

def monitor_campaign(product_name, product_features, description, audience, platform):
    """Track and measure marketing campaign performance."""

    print(f"📊 Monitoring campaign performance for {product_name} on {platform}...")

    # Simulating monitoring metrics (Replace with actual tracking logic)
    metrics = {
        "sales_performance": f"{random.randint(500, 2000)} units sold",
        "lead_conversion_rate": f"{random.uniform(2.5, 10.0):.2f}%",
        "customer_feedback": random.choice(["Positive", "Mixed", "Negative"]),
        "satisfaction_score": f"{random.randint(70, 100)} / 100",
        "competitor_activity": random.choice(["Increased ads", "New product launch", "No major changes"]),
        "budget_utilization": f"${random.randint(5000, 20000)} spent",
        "operational_efficiency": random.choice(["Optimal", "Needs Improvement"]),
    }

    return metrics
