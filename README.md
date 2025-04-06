# Projet-IA
 Description du Projet SecurityCamera : Détecteur de Mouvement avec Alerte Sonore
🎯 Objectif du projet
Ce projet a pour but de développer un système de détection de mouvement en temps réel à l'aide d'une webcam, en utilisant la bibliothèque OpenCV. Lorsqu'un mouvement significatif est détecté dans le champ de vision de la caméra, le système affiche visuellement la zone concernée et déclenche une alerte sonore via le module winsound.

🔧 Fonctionnalités principales
🎥 Capture vidéo en direct via webcam

🧠 Analyse de mouvement en comparant deux images successives

🔍 Traitement d'image pour repérer les zones en mouvement :

Conversion en niveaux de gris

Floutage pour réduire le bruit

Seuillage binaire

Dilatation pour accentuer les mouvements

🟩 Détection de contours et affichage d'un rectangle vert autour de la zone détectée

🔔 Alerte sonore automatique en cas de mouvement

🖼️ Affichage en temps réel du flux vidéo avec surlignage des mouvements

🛠️ Technologies utilisées
Technologie	Utilisation
Python	Langage principal du projet
OpenCV	Traitement d'image et capture vidéo
winsound	Lecture du son d'alerte (Windows uniquement)
🧪 Principe de fonctionnement
Deux images successives sont capturées depuis la webcam.

On calcule la différence entre ces deux images pour repérer les changements.

Une série de traitements (conversion en gris, flou, seuillage, dilatation) est appliquée pour isoler les zones de mouvement.

Les contours sont extraits, et seuls ceux ayant une surface suffisante (plus de 8000 pixels) sont considérés comme du mouvement.

Si un mouvement est détecté :

Un rectangle est affiché sur l'image.

Une alerte sonore (alert.wav) est jouée.

Le processus recommence en boucle pour une détection continue.

🧩 Applications possibles
Surveillance vidéo à domicile ou au bureau

Systèmes d’alarme de sécurité

Projets domotiques

Détection de présence pour interaction automatisée (ex : lumière, enregistrement)

