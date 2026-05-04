Backend SaaS API
API REST backend pour une application SaaS, construite avec FastAPI et SQLAlchemy, avec gestion des migrations via Alembic.

Stack technique

FastAPI — framework web Python haute performance
SQLAlchemy — ORM pour la gestion de la base de données
Alembic — migrations de base de données
Python 3.12


Structure du projet
Backend_Saas/
├── app/                  # Code principal de l'application
│   ├── models/           # Modèles SQLAlchemy
│   ├── routers/          # Routes FastAPI
│   ├── schemas/          # Schémas Pydantic
│   └── ...
├── alembic/              # Migrations de base de données
├── main.py               # Point d'entrée de l'application
├── alembic.ini           # Configuration Alembic
├── requirements.txt      # Dépendances Python
└── .gitignore



Installation
1. Cloner le repo
bashgit clone https://github.com/Cedrichgl/Backend_Saas.git
cd Backend_Saas
2. Créer et activer l'environnement virtuel
bashpython -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
3. Installer les dépendances
bashpip install -r requirements.txt
4. Configurer les variables d'environnement
Créer un fichier .env à la racine :
envDATABASE_URL=postgresql://user:password@localhost:5432/saas_db
SECRET_KEY=your_secret_key
5. Appliquer les migrations
bashalembic upgrade head
6. Lancer le serveur
bashfastapi dev main.py
# ou en production :
uvicorn main:app --host 0.0.0.0 --port 8000
L'API est accessible sur http://localhost:8000
La documentation interactive sur http://localhost:8000/docs

Auteur
Cédric Hiheglo — GitHub
