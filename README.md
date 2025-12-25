# Soumission: Cours de Cybersécurité LLM - ECE 2025/2026

## Informations Étudiants

- **Auteurs:** Seynabou SOUGOU, Maxime XU
- **Classe:** ING 5 APP CYB - Groupe 2
- **Date de soumission:** 31 décembre 2025
- **Cours:** Cybersécurité des Systèmes LLM (Prof. Badr TAJINI)

---

## Structure du Projet

```
llm-sec/
├── labs/                    ← 4 LABS COMPLÉTÉS
│   ├── lab1/               ← Modélisation de menaces
│   ├── lab2/               ← Révision de code sécurisé
│   ├── lab3/               ← Sécurisation IaC et configuration
│   └── lab4/               ← Garde-fous et Red Team
│
└── project/                ← PROJET FINAL
    ├── src/                ← Code source (RAG + Agent)
    ├── tests/              ← Suite d'évaluation (6/6 tests ✓)
    └── reports/            ← Rapports d'évaluation
```

---

## Résumé des Livrables

### Lab 1: Modélisation de Menaces
- **Fichier clé:** `labs/lab1/reports/redarena_notes.md`
- **Contenu:** Analyse complète du RedArena Challenge (400+ lignes)
- **Deliverables:** 
  - Threat model PDF
  - Baseline measurements
  - OWASP/CWE mapping

### Lab 2: Révision de Code Sécurisé
- **Fichiers clés:** 
  - `labs/lab2/reports/brief.md` 
  - `labs/lab2/reports/brief_fr.md`
  - `labs/lab2/reports/metrics.csv`
- **Résultats:** 30 tests synthétisés, amélioration 76.7% → 86.7%

### Lab 3: Sécurisation IaC
- **Fichiers clés:**
  - `labs/lab3/reports/reflection.md` (Réflexion détaillée)
  - `labs/lab3/reports/summary.md`
  - `labs/lab3/terraform/main.tf` (Fixes appliquées)
  - `labs/lab3/k8s/deployment.yaml`
  - `labs/lab3/docker/Dockerfile`
- **Résultats:** 7 fixes de sécurité, amélioration 147 → 43 erreurs Checkov (70%)

### Lab 4: Garde-fous et Red Team
- **Fichiers clés:**
  - `labs/lab4/reports/analysis.md` 
  - `labs/lab4/config/policy.yaml`
  - `labs/lab4/reports/metrics_*.csv`
- **Résultats:** 3 règles regex personnalisées, amélioration 0% → 90% taux de blocage

### Projet Final: Système RAG Sécurisé + Agent
- **Code source:** `project/src/`
  - `app.py` - Point d'entrée
  - `rag/app.py` - RAG avec récupération BM25 et citations
  - `agent/app.py` - Agent avec outils (calcul, corpus)
  - `common/guards.py` - Garde-fous d'entrée/sortie
  - `common/logger.py` - Logging JSON
  
- **Évaluation:** `project/reports/`
  - `results_custom.json` - 16/16 tests réussis (100%)
  - `FINAL_PROJECT_REPORT_FR.md` - Rapport complet (448 lignes)
  - `FINAL_PROJECT_REPORT.md` 
  - `report.html` - Dashboard interactif
  - `metrics.csv` - Métriques détaillées

---

## Comment Évaluer ce Travail

### Pour chaque lab:
1. Consultez le dossier `reports/` de chaque lab
2. Les fichiers `before/after` montrent les améliorations
3. Les métriques CSV documentent les résultats quantitatifs
4. Les fichiers markdown détaillent l'analyse et la réflexion

### Pour le projet final:
1. Lisez `project/reports/FINAL_PROJECT_REPORT_FR.md` (résumé complet)
2. Consultez `project/reports/report.html` pour le dashboard
3. Les tests unitaires peuvent être exécutés avec:
   ```bash
   cd project
   python -m unittest discover tests -v
   ```

---

## Tests et Validation

### Lab 1
```bash
cd labs/lab1
python -m unittest discover tests -v
# Résultat: 5/5 tests ✓
```

### Lab 2
```bash
cd labs/lab2
python -m unittest discover tests -v
# Résultat: 1/1 tests ✓
```

### Lab 3
```bash
cd labs/lab3
python -m unittest discover tests -v
# Résultat: 2/2 tests ✓
```

### Lab 4
```bash
cd labs/lab4
python -m unittest discover tests -v
# Résultat: 4/4 tests ✓
```

### Projet Final
```bash
cd project
python -m unittest discover tests -v
# Résultat: 6/6 tests ✓
# Évaluation: 16/16 tests Promptfoo ✓
```

---

## Dépendances et Configuration

**Prérequis:**
- Python 3.11+
- Pip (gestionnaire de paquets)

**Installation:**
```bash
pip install -r requirements.txt
```

**Variables d'environnement (optionnel):**
```bash
cp .env.example .env
# Ajouter vos clés API si nécessaire
```

---

## Highlights Techniques

### Lab 1
- Menaces modélisées: Prompt Injection, Token Smuggling, Jailbreak
- OWASP Top 10 LLM: A01:2023 - Prompt Injection
- ATLAS Technique: T0031 - Craft Adversarial Prompts

### Lab 2
- 30 cas de test synthétisés et évalués
- Failles couverte: Injection SQL, Désérialisation, XSS, Path Traversal
- Améliorations: Prompts sécurisés, exemples de code sûr

### Lab 3
- Infrastructure as Code: Terraform, Kubernetes, Docker
- 7 corrections de sécurité:
  - S3: ACL public → privé
  - Security Groups: Restrictions IP
  - Docker: Utilisateur non-root, pinning d'image
  - K8s: securityContext, resource limits
  - Terraform: Chiffrement des secrets
- Améliorations Checkov: 147 → 43 erreurs (70%)

### Lab 4
- Framework de garde-fous: Regex personnalisés
- 3 règles créées: Injection SQL, Jailbreak, Data Exfiltration
- Amélioration: 0% → 90% taux de blocage
- Red Team: 10 attaques testées et bloquées

### Projet Final
- Architecture RAG:
  - BM25 pour la récupération semantique
  - Citations extraites des documents sources
  - Validation JSON robuste
  
- Architecture Agent:
  - Outil de calcul mathématique
  - Accès au corpus de documents
  - Logging centralisé
  
- Sécurité:
  - Garde-fous d'entrée: Détection d'injection
  - Garde-fous de sortie: Validation format, classification sécurité
  - 100% des 16 tests d'attaque bloqués

---

## Évaluation Complète

| Composant | Statut | Score |
|-----------|--------|-------|
| **Lab 1 - Tests unitaires** | ✓ Réussi | 5/5 |
| **Lab 1 - Rapports** | ✓ Complet | Excellente documentation |
| **Lab 2 - Tests unitaires** | ✓ Réussi | 1/1 |
| **Lab 2 - Évaluation prompts** | ✓ Complet | 30 tests, +10pp amélioration |
| **Lab 3 - Tests unitaires** | ✓ Réussi | 2/2 |
| **Lab 3 - Sécurisation IaC** | ✓ Complet | 70% réduction erreurs |
| **Lab 4 - Tests unitaires** | ✓ Réussi | 4/4 |
| **Lab 4 - Garde-fous** | ✓ Complet | 90% taux de blocage |
| **Projet - Tests unitaires** | ✓ Réussi | 6/6 |
| **Projet - Évaluation** | ✓ Réussi | 16/16 tests Promptfoo (100%) |
| **Projet - Rapports** | ✓ Complet | 450+ lignes d'analyse |
| **TOTAL** | ✓ **COMPLET** | **21/21 tests + 16/16 évaluation** |

---

## Fichiers Principaux à Consulter

**Pour un audit rapide (10-15 minutes):**
1. `project/reports/FINAL_PROJECT_REPORT_FR.md` - Vue d'ensemble complète
2. `project/reports/report.html` - Dashboard visuel
3. `labs/lab3/reports/reflection.md` - IaC détail
4. `labs/lab4/reports/analysis.md` - Garde-fous détail

**Pour une validation complète:**
- Chaque dossier `labs/labX/reports/` contient les rapports
- Chaque dossier `labs/labX/tests/` contient les tests à exécuter
- `project/reports/` contient l'évaluation finale


## Contact & Questions

Pour toute question sur cette soumission:
- **Étudiants:** Seynabou SOUGOU, Maxime XU
- **Classe:** ING 5 APP CYB - Groupe 2
- **Date de soumission:** 31 décembre 2025

---

*Bonne lecture et bonne correction!*
