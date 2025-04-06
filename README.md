🛡️ Description du Projet SecurityCamera : Détecteur de Mouvement avec Alerte Sonore

# Détecteur de Mouvement avec Alerte Sonore (OpenCV + Python)

## 🎯 Choix du Projet

Le choix de ce projet s’est porté sur la détection de mouvement en temps réel à l’aide d’une webcam. L’objectif était de mettre en œuvre une solution simple, visuelle et interactive utilisant la bibliothèque OpenCV. Pour renforcer l’aspect pratique, une alerte sonore est déclenchée lorsqu’un mouvement est détecté, simulant un système d’alarme de sécurité.

Ce projet est particulièrement utile pour comprendre les bases de la vision par ordinateur, la manipulation d’images en temps réel, ainsi que les contours et les différences d’images.

---

## ⚙️ Installation

### Prérequis

- Python 3.x
- Modules Python :
  - `opencv-python`
  - `winsound` (intégré à Windows)

### Étapes

1. **Téléchargez ou clonez le projet.**

2. **Placez un fichier audio `alert.wav` dans le même dossier que le script.**

3. **Installez les dépendances :**

```bash
pip install opencv-python





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








