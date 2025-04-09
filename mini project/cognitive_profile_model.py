import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import joblib

# 1. Load and Preprocess Data
def load_data(file_path):
    """
    Loads and preprocesses user learning data.
    The file should contain features such as quiz scores, time spent on content, and engagement metrics.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess the dataset, separating features and labels, and normalizing the features.
    """
    X = data.drop(columns=['user_id', 'learning_level'])  # Features
    y = data['learning_level']  # Labels (e.g., Beginner, Intermediate, Advanced)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

# 2. Build Cognitive Profile Model
def build_model():
    """
    Initializes a Random Forest Classifier as the cognitive profiling model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    return model

# 3. Train Model
def train_model(model, X_train, y_train):
    """
    Train the cognitive profiling model.
    """
    model.fit(X_train, y_train)
    return model

# 4. Evaluate Model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model's accuracy and display classification metrics.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("Classification Report:")
    print(report)

# 5. Save Model
def save_model(model, file_name='cognitive_profile_model.pkl'):
    """
    Saves the trained model to a file for later use.
    """
    joblib.dump(model, file_name)
    print(f"Model saved to {file_name}")

# 6. Load Model (for predictions)
def load_model(file_name='cognitive_profile_model.pkl'):
    """
    Loads a pre-trained model from a file.
    """
    try:
        model = joblib.load(file_name)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# 7. Main Execution
if __name__ == '__main__':
    # Load dataset
    data_file = 'user_learning_data.csv'  # Path to your dataset
    data = load_data(data_file)

    if data is not None:
        # Preprocess data
        X, y = preprocess_data(data)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Build and train the model
        model = build_model()
        model = train_model(model, X_train, y_train)

        # Evaluate the model
        evaluate_model(model, X_test, y_test)

        # Save the model for later use
        save_model(model)

