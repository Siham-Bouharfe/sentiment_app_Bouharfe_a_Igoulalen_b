# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

L'interface n'importe jamais `predict()` ni le fichier `.joblib` : elle communique uniquement avec l'API HTTP. Cela sépare l'affichage du modèle et permet de remplacer ou déployer le modèle sans modifier Streamlit.

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Quand le modèle hésite, l'API renvoie `INDETERMINE` et l'interface indique qu'un humain doit vérifier l'avis. C'est plus honnête qu'un verdict forcé avec une confiance faible.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

Si l'API tombe, l'utilisateur reçoit un message lisible indiquant de lancer `uvicorn api.main:app`. Le fichier d'exemple est traité par lots et les réponses incertaines sont comptées séparément pour être vérifiées.
