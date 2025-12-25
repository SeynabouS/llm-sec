# Lab 1: Modélisation de Menaces LLM

**Auteurs:** Seynabou SOUGOU, Maxime XU  
**Classe:** ING 5 APP CYB - Groupe 2  
**Date:** ECE 2025/2026

---

## 📋 Ce que nous avons fait

Ce lab nous a permis d'identifier et documenter les menaces contre les systèmes LLM. Voici nos travaux:

✅ **Analyse des attaques Gandalf & RedArena**
- Joué à Gandalf pour comprendre les patterns de jailbreak
- Documenté 400+ lignes d'analyse des techniques d'attaque

✅ **Mapping OWASP & MITRE ATLAS**
- Classifié les menaces selon OWASP Top 10 LLM 2023
- Mappé chaque attaque sur MITRE ATLAS techniques
- Créé un threat model complet

✅ **Baseline & Validation**
- Capturé les réponses avant/après durcissement
- Validé avec Gemini API
- Vérifié via tests unitaires

**Résultat:** 5/5 tests unitaires ✓

---

## 📁 Fichiers Clés

**Rapport principal:**
- `reports/redarena_notes.md` - Notre analyse complète (400+ lignes)

**Notes détaillées:**
- `reports/gandalf_notes.md` - Observations Gandalf

**Preuves techniques:**
- `reports/baseline_before.json` - État initial
- `reports/baseline_after.json` - État après durcissement
- `reports/baseline.json` - Résumé des métriques

---

## 🛠️ Prérequis

```bash
Python 3.11+
pip install -r ../../requirements.txt
```

**API Key:**
```bash
# Configurer dans .env
GEMINI_API_KEY=votre_clé_ici
```

---

## 🚀 Exécuter les tests

```bash
# Du dossier lab1/
python -m unittest discover tests -v

# Résultat attendu: 5/5 tests ✓
```

---

## 📊 Résumé des menaces documentées

| Menace | OWASP | ATLAS | Technique |
|--------|-------|-------|-----------|
| Prompt Injection | A01 | T0031 | Craft Adversarial Prompts |
| Token Smuggling | A01 | T0031 | Obfuscation techniques |
| Jailbreak Pattern | A02 | T0051 | Role-playing attacks |
| Data Exfiltration | A06 | T0051 | Information extraction |

---

## 🎓 Concepts appliqués

- **OWASP Top 10 LLM 2023** - Framework de risques LLM
- **MITRE ATLAS** - Taxonomie des attaques IA
- **Prompt Engineering** - Sécurisation des instructions
- **JSON Schema Validation** - Pydantic pour validation

---

## 📝 Notes importantes

1. **Authentique:** Ces notes reflètent nos observations réelles de Gandalf et RedArena
2. **Documenté:** Chaque menace est mappée sur les frameworks standards
3. **Testé:** Tous les composants passent les tests unitaires

