# 🩺 Health Calculator Microservice with CI/CD on Azure

## 🎯 Objectif

Développer un **microservice Python/Flask** capable de :
- Calculer le **BMI** (Body Mass Index)
- Calculer le **BMR** (Basal Metabolic Rate)

Avec :
- Déploiement automatique sur **Azure App Service** via **GitHub Actions**.

---

## 🔢 Formules utilisées

- **BMI** :
BMI = poids (kg) / (taille (m))²


- **BMR (Harris-Benedict Formula)** :
- Hommes :
  ```
  BMR = 88.362 + (13.397 × poids) + (4.799 × taille) - (5.677 × âge)
  ```
- Femmes :
  ```
  BMR = 447.593 + (9.247 × poids) + (3.098 × taille) - (4.330 × âge)
  ```

---

## 📦 Structure du projet

```bash
health-calculator-service/
├── app.py                # Application Flask principale
├── health_utils.py        # Fonctions de calcul BMI et BMR
├── Dockerfile             # Dockerfile pour la containerisation
├── Makefile               # Makefile pour automatiser les commandes
├── requirements.txt       # Dépendances Python
└── .github/workflows/ci-cd.yml  # Déploiement automatique via GitHub Actions

🚀 Déploiement automatique sur Azure
Le projet utilise GitHub Actions pour réaliser un déploiement continu vers Azure App Service.

Prérequis
Un compte Azure actif.

Un App Service Azure (Linux / Python 3.9 ou 3.10).

Le Publish Profile de l'App Service

📋 API disponible

Endpoint	Méthode	Description	Paramètres attendus
/bmi	POST	Calcul du BMI	{ "height": mètres, "weight": kilogrammes }
/bmr	POST	Calcul du BMR	{ "height": centimètres, "weight": kilogrammes, "age": années, "gender": "male" ou "female" }

Endpoint | Méthode | Description | Paramètres attendus
/bmi | POST | Calcul du BMI | { "height": mètres, "weight": kilogrammes }
/bmr | POST | Calcul du BMR | { "height": centimètres, "weight": kilogrammes, "age": années, "gender": "male" ou "female" }
