# Lab 2: Révision de Code Sécurisé avec LLM

**Auteurs:** Seynabou SOUGOU, Maxime XU  
**Classe:** ING 5 APP CYB - Groupe 2  
**Date:** ECE 2025/2026

---

## 📋 Ce que nous avons fait

Ce lab nous a appris à évaluer et améliorer les prompts LLM pour la révision de code sécurisé.

✅ **Synthèse automatique de 30 cas de test**
- Créé `generate_tests.py` pour synthétiser tests depuis les snippets de code
- Couvert: SQL Injection, Désérialisation, XSS, Path Traversal, Command Injection
- Tests en Python, JavaScript et Java

✅ **Évaluation comparative des prompts**
- **Baseline prompt:** Révision générale (76.7% de réussite)
- **Secure prompt:** Consignes explicites de sécurité (86.7% de réussite)
- **Amélioration:** +10 points de pourcentage

✅ **Métriques & Rapports**
- Généré `metrics.csv` avec résultats quantitatifs
- Créé `brief.md` et `brief_fr.md` avec analyse détaillée
- Tous les tests passent: 1/1 ✓

---

## 📁 Fichiers Clés

**Tests synthétisés:**
- `_generated/tests_flat.yaml` - 30 cas de test générés automatiquement
- `generate_tests.py` - Script de synthèse

**Prompts testés:**
- `prompts/baseline_prompt.txt` - Prompt baseline
- `prompts/secure_review_prompt.txt` - Prompt sécurisé

**Résultats:**
- `reports/metrics.csv` - Résultats quantitatifs
- `reports/brief.md` - Analyse en français
- `reports/brief_fr.md` - Version alternative

---

## 🛠️ Prérequis

```bash
Python 3.11+
Node.js 22+ (pour promptfoo)
pip install -r ../../requirements.txt
npm install -g promptfoo
```

---

## 🚀 Exécuter les tests

```bash
# Du dossier lab2/
python -m unittest discover tests -v

# Résultat attendu: 1/1 test ✓
```

---

## 📊 Résultats de l'évaluation

| Métrique | Baseline | Secure | Amélioration |
|----------|----------|--------|-------------|
| **Accuracy** | 76.7% | 86.7% | +10.0pp |
| **Tests passés** | 23/30 | 26/30 | +3 tests |
| **Faux positifs** | 2 | 1 | -1 |
| **Faux négatifs** | 5 | 3 | -2 |

---

## 🔍 Failles de sécurité couvertes

1. **SQL Injection** - Injection SQL via paramètres
2. **Désérialisation** - Deserialization attacks
3. **XSS** - Cross-Site Scripting
4. **Path Traversal** - Directory traversal attacks
5. **Command Injection** - OS command injection

---

## 🎓 Concepts appliqués

- **Prompt Engineering** - Optimisation des instructions LLM
- **Test Synthesis** - Génération automatique de cas de test
- **Security Review** - Évaluation de code sécurisé
- **Metrics Evaluation** - Mesure comparative

---

## 📝 Notes importantes

1. **Authentique:** Tests synthétisés depuis code réel
2. **Comparable:** Même baseline et prompts sécurisés testés
3. **Amélioré:** +10pp d'amélioration via better prompting
4. **Documenté:** Chaque test case tracé

**Conclusion:** Lab 2 montre comment des prompts plus précis améliorent significativement la qualité de la révision de code LLM.
