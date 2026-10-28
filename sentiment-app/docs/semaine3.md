# Semaine 3 — interface Streamlit

L'interface affiche « à vérifier » lorsque la confiance du modèle est inférieure à 60 %, afin qu'un agent humain puisse reprendre les cas incertains.
Ce seuil évite de présenter comme certaines les prédictions faibles, notamment sur les avis mitigés où le modèle « sac de mots » comprend mal le retournement.
Le compromis est acceptable pour le service client : les avis très incertains sont contrôlés par un humain, tandis que les avis évidents restent traités automatiquement.
