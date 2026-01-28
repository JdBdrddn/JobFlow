# JobFlow 

**Système de suivi des candidatures pour étudiants en informatique**

##  À propos du projet

JobFlow est une application web full-stack conçue pour aider les étudiants et chercheurs d'emploi à organiser et suivre leurs candidatures. Ce projet a été développé dans le cadre de mon portfolio pour démontrer mes compétences en développement web moderne.

### Fonctionnalités actuelles
-  API RESTful avec FastAPI
-  Base de données PostgreSQL
-  Modèle de données pour les candidatures
-  Architecture backend complète
-  Interface utilisateur (en développement)

### Fonctionnalités prévues
- Ajout de nouvelles candidatures
- Visualisation de toutes les candidatures
- Mise à jour du statut des candidatures
- Tableau de bord avec statistiques
- Système de notifications pour les suivis

##  Technologies utilisées

### Backend
- **FastAPI** - Framework web moderne et rapide pour Python
- **Python 3.11+** - Langage de programmation
- **SQLAlchemy** - ORM pour la gestion de base de données
- **PostgreSQL** - Base de données relationnelle
- **Uvicorn** - Serveur ASGI pour FastAPI

### Frontend (à venir)
- HTML5
- CSS3
- JavaScript

##  Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python 3.11 ou supérieur
- PostgreSQL 14 ou supérieur
- pip (gestionnaire de paquets Python)
- Git

##  Installation et configuration

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-username/jobflow.git
cd jobflow
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

**Activer l'environnement virtuel :**

- Windows :
```bash
.venv\Scripts\activate
```

- macOS/Linux :
```bash
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer PostgreSQL

1. Ouvrez pgAdmin ou votre outil de gestion PostgreSQL
2. Créez une nouvelle base de données nommée `jobflow_db`

### 5. Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet :

```env
DATABASE_PASSWORD=votre_mot_de_passe_postgresql
```

** Important :** Ne partagez jamais votre fichier `.env` ! Il est déjà inclus dans `.gitignore`.

### 6. Lancer l'application

```bash
uvicorn main:app --reload
```

L'API sera accessible à l'adresse : `http://127.0.0.1:8000`

### 7. Tester l'API

Accédez à la documentation interactive de l'API :
- Swagger UI : `http://127.0.0.1:8000/docs`
- ReDoc : `http://127.0.0.1:8000/redoc`

##  Structure du projet

```
jobflow/
│
├── main.py              # Point d'entrée de l'application FastAPI
├── database.py          # Configuration de la connexion à la base de données
├── models.py            # Modèles SQLAlchemy (schéma de données)
├── requirements.txt     # Dépendances Python
├── .env                 # Variables d'environnement (non versionné)
├── .gitignore          # Fichiers à ignorer par Git
└── README.md           # Ce fichier
```

##  Modèle de données

### Table : job_applications

| Colonne       | Type    | Description                              |
|---------------|---------|------------------------------------------|
| id            | Integer | Identifiant unique (clé primaire)        |
| company       | String  | Nom de l'entreprise                      |
| position      | String  | Titre du poste                           |
| status        | String  | Statut (Applied, Interview, Offer, etc.) |
| applied_date  | Date    | Date de candidature                      |

##  Statut du projet

**Phase actuelle :** Développement du backend 

**Prochaines étapes :**
1. Implémentation des endpoints POST et GET
2. Tests des fonctionnalités backend
3. Développement de l'interface utilisateur
4. Déploiement en production



