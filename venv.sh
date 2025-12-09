#!/bin/bash

# Mettre à jour les paquets
sudo apt update && sudo apt upgrade -y

# Installer Python et les outils nécessaires
sudo apt install -y python3-pip python3-setuptools python3-venv

# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Mettre à jour pip
pip install --upgrade pip

# Créer le fichier requirements.txt

# Installer toutes les bibliothèques listées dans requirements.txt
pip install -r requirements.txt

# Télécharger le modèle français de spaCy
python -m spacy download fr_core_news_md
