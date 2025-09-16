import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("beer-servings.csv")

# Select features and target
data = df[["beer_servings", "spirit_servings", "wine_servings", "total_litres_of_pure_alcohol"]].dropna()
X = data[["beer_servings", "spirit_servings", "wine_servings"]]
y = data["total_litres_of_pure_alcohol"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved as model.pkl")
