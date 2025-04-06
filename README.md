🛡️ Description du Projet SecurityCamera : Détecteur de Mouvement avec Alerte Sonore

# Détecteur de Mouvement avec Alerte Sonore

Ce projet Python utilise la bibliothèque OpenCV pour détecter les mouvements via une webcam, et joue un son d'alerte lorsqu'un mouvement significatif est détecté.

## Fonctionnalités

- Capture vidéo en temps réel via la webcam.
- Comparaison de deux images consécutives pour détecter un changement de scène.
- Filtrage du bruit avec un flou gaussien et seuillage.
- Détection de contours pour identifier les zones de mouvement.
- Déclenchement d’un signal sonore (`alert.wav`) lorsqu’un mouvement important est détecté (zone > 8000 px²).
- Affichage en direct avec surlignage des zones détectées.

## Prérequis

- Python 3.x
- Modules :
  - `opencv-python`
  - `winsound` (disponible uniquement sur



# 🎮 Système de Contrôle par Détection de Couleur (OpenCV + PyAutoGUI)

## 📌 Description Projet ObjectDetection

Ce projet permet de contrôler certaines actions de l’ordinateur à l’aide d’un objet de couleur spécifique détecté via la webcam. Grâce à la vision par ordinateur (OpenCV) et à l’automatisation de clavier (PyAutoGUI), l’utilisateur peut interagir sans utiliser de périphériques traditionnels comme le clavier ou la souris.

Exemple d’interaction : en déplaçant un objet jaune vers le haut ou vers le bas dans le champ de la webcam, le programme simule l’appui sur les touches fléchées "haut" ou "bas".

---

## 🧠 Fonctionnalités

- 📷 Capture vidéo en temps réel via webcam
- 🎯 Détection précise d’un objet de couleur jaune (en HSV)
- 🕹️ Déclenchement automatique de touches :
  - Haut ⬆️ → si l’objet se déplace vers le haut
  - Bas ⬇️ → si l’objet se déplace vers le bas
- 🔔 Alerte sonore lorsque l’objet atteint le haut de l’image
- 🧪 Visualisation des différentes étapes : image d'origine, HSV, masque, résultat

---

## 🛠️ Technologies utilisées

- [Python 3.x](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [winsound (Windows only)](https://docs.python.org/3/library/winsound.html)

---

## 🚀 Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/votre-utilisateur/controle-couleur-opencv.git
   cd controle-couleur-opencv








