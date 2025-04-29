# 🩺 Health Calculator Microservice with CI/CD on Azure

Ceci est un **microservice Python/Flask** capable de :

- Calculer le **BMI** (Body Mass Index)  
- Calculer le **BMR** (Basal Metabolic Rate)

Avec :

- Déploiement automatique sur **Azure App Service** via **GitHub Actions**.

---

## 🔢 Formules utilisées

### **BMI**  
```text
BMI = poids (kg) / (taille (m))²
```

### **BMR (Harris-Benedict Formula)**

- **Hommes** :
```text
BMR = 88.362 + (13.397 × poids) + (4.799 × taille) - (5.677 × âge)
```

- **Femmes** :
```text
BMR = 447.593 + (9.247 × poids) + (3.098 × taille) - (4.330 × âge)
```

---

## 📦 Structure du projet

```bash
health-calculator-service/
├── app.py                          # Application Flask principale
├── health_utils.py                 # Fonctions de calcul BMI et BMR
├── Dockerfile                      # Dockerfile pour la containerisation
├── Makefile                        # Makefile pour automatiser les commandes
├── requirements.txt                # Dépendances Python
└── .github/workflows/main.yml      # Déploiement automatique via GitHub (optionnel)
```

---

## 🔄 Déploiement GitHub–Azure (CI/CD)

### 🎯 Prérequis :

- Un compte **Azure** actif  
- Un **App Service** Azure (Linux / Python 3.9 ou 3.10)  
- Le **Publish Profile** de l'App Service (uniquement si déploiement manuel)

### ⚙️ Déploiement automatique :

Ce projet est déployé automatiquement à chaque mise à jour de la branche `main`, grâce à :

✅ L’intégration native de GitHub dans **Azure App Service**  
✅ Azure qui construit et déploie automatiquement l’image Docker depuis votre dépôt GitHub  
✅ **Aucune configuration de secrets manuels** ni fichier `.yml` obligatoire

### 📍 Étapes depuis le portail Azure :

1. Allez dans votre **App Service** > **Centre de déploiement**
2. Choisissez **GitHub** comme source
3. Sélectionnez le dépôt et la branche à suivre
4. Azure s’occupe du reste 🚀

---

## 📋 API disponible

| Endpoint | Méthode | Description       | Paramètres attendus                                                                 |
|----------|---------|-------------------|--------------------------------------------------------------------------------------|
| `/bmi`   | POST    | Calcul du BMI     | `{ "height": mètres, "weight": kilogrammes }`                                       |
| `/bmr`   | POST    | Calcul du BMR     | `{ "height": centimètres, "weight": kilogrammes, "age": années, "gender": "male" ou "female" }` |

---

## 🚀 DEMO

**URL de démonstration :**  
🔗 [https://myhealthapp-h7e6cwfsazdxg4ca.canadacentral-01.azurewebsites.net](https://myhealthapp-h7e6cwfsazdxg4ca.canadacentral-01.azurewebsites.net)

---
