# Pics2vid
French/English

#PicsToVideo
PicsToVideo est un projet Python interactif basique et brut qui permet de convertir un ensemble d’images en une vidéo MP4 personnalisée. Grâce à une interface graphique conviviale, vous pouvez facilement configurer les paramètres de votre vidéo, y compris le nombre d’images par seconde et la qualité de l’encodage.


Fonctionnalités principales

Interface intuitive : Utilisation de Tkinter pour une interaction utilisateur simple.
Support des images : Accepte les formats PNG, JPG et JPEG.
Redimensionnement automatique : Vérifie que toutes les images ont la même taille. Si nécessaire, les images sont redimensionnées automatiquement pour correspondre à la taille de la première image.

Paramètres personnalisés :
Images par seconde (FPS) : Contrôlez la fluidité de votre vidéo.
Qualité de l'encodage : Ajustez la qualité de 0 (basse qualité) à 100 (haute qualité, par défaut 90).
Encodage MP4 : Utilisation du codec mp4v pour créer des vidéos compatibles avec de nombreux lecteurs.
Barre de progression : Suivez l’avancement de l’encodage en temps réel.
Préservation des fichiers existants : Évite d'écraser un fichier existant avec le même nom.
Prérequis
Python 3.7 ou plus
Bibliothèques Python :
opencv-python
pillow
tqdm

Système d'exploitation compatible : Windows, macOS, Linux.

Installation
Windows: copiez les deux fichiers dans un répertoire dédié: ex: "MonPics2Video":
RunMeFirst.bat
Pics2video.py
Lancez le fichier RunMeFirst.bat et le programme vérifie automatiquement les dépendances, les installe au besoin puis lance le script


Pour les autres:
Clonez le dépôt 
git clone https://github.com/Giribot/picstovideo.git
cd picstovideo

Installez les dépendances :
pip install opencv-python pillow tqdm

Utilisation
Lancez le script :

python picstovideo.py
Suivez les instructions pour :

Sélectionner un dossier contenant les images.
Configurer le nombre d’images par seconde (FPS) et la qualité de l’encodage.
Choisir l’emplacement de sauvegarde du fichier vidéo.
Laissez PicsToVideo générer votre vidéo MP4.

Contributions
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour signaler un bug ou proposer une amélioration.

Licence:
Creative Common ! (cf Github)


-----
English

PicsToVideo is a basic, raw, interactive Python project that converts a set of images into a custom MP4 video. With a user-friendly GUI, you can easily configure your video settings, including frames per second and encoding quality.

Key Features

Intuitive interface: Uses Tkinter for easy user interaction.

Image support: Accepts PNG, JPG, and JPEG formats.

Auto-resizing: Checks that all images are the same size. If necessary, images are automatically resized to match the size of the first frame.

Custom settings:
Frames per second (FPS): Control the smoothness of your video.

Encoding quality: Adjust the quality from 0 (low quality) to 100 (high quality, default 90).

MP4 encoding: Uses the mp4v codec to create videos that are compatible with many players.

Progress bar: Track the encoding progress in real time.

Preserving existing files: Avoids overwriting an existing file with the same name.

Prerequisites
Python 3.7 or later
Python libraries:
opencv-python
pillow
tqdm
Compatible operating system: Windows, macOS, Linux.

Installation
Windows: copy the two files into a dedicated directory: ex: "MyPics2Video":
RunMeFirst.bat
Pics2video.py
Run the RunMeFirst.bat file and the program automatically checks the dependencies, installs them if necessary and then launches the script

For others:
Clone the repository
git clone https://github.com/Giribot/picstovideo.git
cd picstovideo

Install the dependencies:
pip install opencv-python pillow tqdm

Usage
Run the script:

python picstovideo.py
Follow the instructions to:

Select a folder containing the images.
Configure the number of frames per second (FPS) and the encoding quality.
Choose the location to save the video file.
Let PicsToVideo generate your MP4 video.

Contributions
Contributions are welcome! Please submit a pull request or open an issue to report a bug or suggest an improvement.

License:
Creative Common! (cf Github)
