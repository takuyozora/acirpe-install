#!/bin/bash

echo "!start_pulse"

echo "#Installation de VLC ..."
echo "Le logiciel est en train d'installer VLC.\nCe logiciel permet de lire facilement un ensemble immense de fichier audio et vidéo."
apt-get install vlc -y -q=3 2>&1 /dev/null

echo "!next_step"
echo "#Installation de Flash"
echo "Le logiciel est en train d'installer le plugin flash player.\nCe logiciel permet de charger des annimation contenue dans les page web et de les afficher."
apt-get install flashplugin-installer -y -q=3 2>&1 /dev/null

echo "!next_step"
echo "#Installation de GIMP"
echo "Le logiciel est en train d'installer GIMP.\nCe logiciel premet de manipuler très finement des images, de les redimensionner ou de les créer de toutes pièce."
apt-get install gimp -y -q=3 2>&1 /dev/null

echo "!next_step"
echo "#Installation des codecs"
echo "Le logiciel est en train d'installer des codecs.\nCes paquets servent à lire un maximum de format de fichiers différents."
wget -q http://www.medibuntu.org/sources.list.d/`lsb_release -cs`.list --output-document=/etc/apt/sources.list.d/medibuntu.list && apt-get -q=3 -y update && apt-get --yes -q=3 --allow-unauthenticated install medibuntu-keyring && apt-get -q=3 -y update && apt-get install -q=3 -y non-free-codecs libdvdcss2 gstreamer0.10-plugins-ugly regionset libdvdnav4 && sudo apt-get -q update 
ubuntu-restricted-extras 

echo "!stop_pulse"
echo "!next_step"
echo "Le logiciel a fini d'installer les programmes pour le système."
echo "!end"


