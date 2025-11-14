import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic customer data
n = 300  # number of customers
data = {
    "customer_id": range(1, n+1),
    "age": np.random.randint(18, 70, n),
    "income": np.random.randint(30000, 120000, n),
    "avg_monthly_spend": np.random.randint(10, 150, n),
    "visits_per_month": np.random.randint(1, 12, n),
    "reward_points": np.random.randint(0, 1000, n),
    "last_purchase_days": np.random.randint(1, 120, n)
}

df = pd.DataFrame(data)

# Simulate churn (customers with fewer visits and higher last_purchase_days)
df["churned"] = np.where(
    (df["visits_per_month"] < 3) & (df["last_purchase_days"] > 60),
    1,
    0
)