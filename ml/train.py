import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from database.connection import engine


def train_model():
    # Load data from database
    df = pd.read_sql("SELECT * FROM player_stats", engine)

    # Features for prediction
    features = [
        "points_per_game",
        "three_point_ratio",
        "free_throw_ratio",
        "total_games"
    ]

    X = df[features]
    y = df["hall_of_fame"]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, predictions))
    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))
    # Feature Importance
    importances = model.feature_importances_

    print("\nFeature Importances:")
    for feature, importance in zip(features, importances):
        print(f"{feature}: {importance:.4f}")



if __name__ == "__main__":
    train_model()