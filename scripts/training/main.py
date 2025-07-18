import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import MultiLabelBinarizer

# === Cargar dataset con características ===
features_df = pd.read_csv("data/processed/features_dataset.csv")
features_df["genres"] = features_df["genres"].apply(eval)

# === Separar variables ===
X = features_df.drop(columns=["userId", "movieId", "rating"])
y = (features_df["rating"] >= 4).astype(int)  # Clasificación binaria

# === One-Hot para géneros ===
mlb = MultiLabelBinarizer()
genres_encoded = pd.DataFrame(mlb.fit_transform(X["genres"]), columns=mlb.classes_)
X = X.drop(columns=["genres"]).reset_index(drop=True)
X = pd.concat([X, genres_encoded], axis=1)

# === División en entrenamiento y prueba ===
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# === Definir modelos ===
# Línea base: regresión logística
baseline_model = LogisticRegression(max_iter=1000, random_state=42)

# Modelos adicionales
additional_models = {
    "random_forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "gradient_boosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "svm_rbf": SVC(kernel="rbf", probability=True, random_state=42),
}

# === Entrenamiento y evaluación ===
reports = {}

# Directorio de salida
output_dir = "models"
os.makedirs(output_dir, exist_ok=True)

# ---- Entrenar modelo base ----
print("\n=== Modelo base: Logistic Regression ===")
baseline_model.fit(X_train, y_train)
y_pred_base = baseline_model.predict(X_test)
report_base = classification_report(y_test, y_pred_base, target_names=["No le gustó", "Le gustó"], output_dict=True)
reports["logistic_regression"] = report_base
print(classification_report(y_test, y_pred_base, target_names=["No le gustó", "Le gustó"]))
joblib.dump(baseline_model, os.path.join(output_dir, "logistic_regression.joblib"))

# ---- Entrenar modelos adicionales ----
for name, model in additional_models.items():
    print(f"\n=== Modelo adicional: {name} ===")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=["No le gustó", "Le gustó"], output_dict=True)
    reports[name] = report
    print(classification_report(y_test, y_pred, target_names=["No le gustó", "Le gustó"]))
    joblib.dump(model, os.path.join(output_dir, f"{name}.joblib"))

# === Guardar reportes finales ===
reports_df = pd.DataFrame({
    model: {
        "precision": reports[model]["Le gustó"]["precision"],
        "recall": reports[model]["Le gustó"]["recall"],
        "f1-score": reports[model]["Le gustó"]["f1-score"]
    }
    for model in reports
}).T

reports_df.to_csv("data/processed/model_reports.csv")
print("\n=== Comparación de modelos (F1, Precision, Recall - clase 'Le gustó') ===")
print(reports_df.round(3))
