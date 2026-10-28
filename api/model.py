"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn : elle appelle la fonction
predict() de src/predict.py, qui charge models/sentiment.joblib une seule fois.
"""
from typing import Literal, TypedDict

from sentiment_app.predict import charger_modele
from sentiment_app.predict import predict as _predict

SEUIL_ABSTENTION = 0.60


class Prediction(TypedDict):
    label: Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        charger_modele()  # échoue immédiatement si le joblib manque : on ne démarre pas sans modèle

    def predict(self, text: str) -> Prediction:
        """Renvoie le verdict, la confiance et un aperçu du texte."""
        r = _predict(text)  # lève ValueError si le texte est vide
        score = float(r["score"])
        label = r["label"].upper()
        verdict: Literal["POSITIVE", "NEGATIVE", "INDETERMINE"] = (
            "INDETERMINE" if score < SEUIL_ABSTENTION else label
        )
        return {"label": verdict, "score": score, "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans le paquet)."""
    return SentimentClassifier()
