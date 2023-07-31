# Gestion-emploi-du-temps
Ceci est une application Flask développée avec Python. Elle utilise Bootstrap pour le design et MySQL pour la base de données.

Installation
Cloner le dépôt : git clone https://github.com/votre-nom/votre-projet.git
Aller dans le répertoire du projet : cd votre-projet
Installer les dépendances : 
pip install Flask
pip install Flask-MySQLdb
Python 3.x : Langage de programmation principal utilisé pour développer l'application Flask.

Flask : Framework web léger et puissant pour créer des applications web en Python.

Flask-MySQLdb (ou Flask-MySQL) : Extension Flask qui permet de se connecter à une base de données MySQL.

Bootstrap : Framework CSS et JavaScript pour styliser et rendre le site web réactif.

Jinja2 : Moteur de template utilisé par Flask pour générer les pages HTML dynamiquement.

MySQL Server : Base de données MySQL pour stocker les données de l'application.
Configurer la base de données MySQL dans le fichier config.py
Utilisation
Lancer l'application : python app.py
Aller sur http://localhost:5000/ dans votre navigateur pour utiliser l'application
Fonctionnalités
Connexion des utilisateurs : L'application propose une page de connexion où les utilisateurs peuvent saisir leur nom d'utilisateur, leur mot de passe et leur statut (étudiant ou professeur). En fonction de ces informations, l'application redirige l'utilisateur vers la page appropriée : la page "emploi_du_temps.html" pour les étudiants et la page "index.html" pour les professeurs.

Affichage de l'emploi du temps : Sur la page "emploi_du_temps.html", les étudiants peuvent voir leur emploi du temps affiché sous forme de tableau. Les informations sur les modules, les professeurs, les dates, les heures, les salles, les unités d'enseignement et le nombre d'heures sont récupérées depuis la base de données MySQL et affichées dynamiquement à l'aide de templates Jinja2.

Ajout d'un emploi du temps : Sur la page "index.html", les professeurs peuvent ajouter un nouvel élément à l'emploi du temps. Ils remplissent un formulaire avec les détails du nouveau module, du professeur, de la date, des heures, de la salle, de l'unité d'enseignement et du nombre d'heures, puis soumettent le formulaire. Les informations sont ensuite enregistrées dans la base de données MySQL.

Modification d'un emploi du temps : Sur la page "emploi_du_temps.html", les étudiants et les professeurs ont la possibilité de modifier les détails d'un élément de l'emploi du temps. Ils peuvent cliquer sur le bouton "Modifier" à côté de l'élément qu'ils souhaitent modifier, ce qui les redirigera vers une page de modification où le formulaire est pré-rempli avec les informations actuelles de l'élément. Après avoir apporté les modifications souhaitées et soumis le formulaire, les informations sont mises à jour dans la base de données MySQL.

Suppression d'un emploi du temps : Sur la page "emploi_du_temps.html", les étudiants et les professeurs ont la possibilité de supprimer un élément de l'emploi du temps. Ils peuvent cliquer sur le bouton "Supprimer" à côté de l'élément qu'ils souhaitent supprimer, et une confirmation sera demandée avant que l'élément soit effectivement supprimé de la base de données MySQL.
Auteur
serignz fallou seck
