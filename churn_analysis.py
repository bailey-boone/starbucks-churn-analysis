import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load Data
df = pd.read_csv("starbucks_customers.csv")

# summary Stats
print(df.describe())

# Visualizations 
sns.boxplot(x="churned", y="avg_monthly_spend", data=df)
plt.title("Average Spend by Churn Status")
plt.show()

sns.scatterplot(x="visits_per_month", y="reward_points", hue="churned", data=df)
plt.title("Visits vs Rewards (Churn Highlighted)")
plt.show()

# model
X = df[["age", "income", "avg_monthly_spend", "visits_per_month", "reward_points", "last_purchase_days"]]
y = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("\n--- Model Evaluation ---")
print(classification_report(y_test, y_pred))
