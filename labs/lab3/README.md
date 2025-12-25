# Lab 3: Sécurisation Infrastructure & IaC

**Auteurs:** Seynabou SOUGOU, Maxime XU  
**Classe:** ING 5 APP CYB - Groupe 2  
**Date:** ECE 2025/2026

---

## 📋 Ce que nous avons fait

Ce lab nous a enseigné comment durcir l'infrastructure et sécuriser les configurations Infrastructure-as-Code (IaC).

✅ **Identification des vulnérabilités avec Checkov**
- Scannage initial: **147 erreurs** trouvées
- Analyse approfondie avec Checkov
- Catégorisation par type et sévérité

✅ **Implémentation de 7 corrections majeures**

1. **S3 Bucket:** ACL public → privé
2. **Security Groups:** Restrictions par IP
3. **Docker:** Utilisateur non-root + image pinning
4. **Kubernetes:** securityContext + resource limits
5. **Terraform:** Chiffrement des secrets
6. **Registry:** Authentification renforcée
7. **IAM:** Least privilege principle

✅ **Validation & Résultats**
- Après corrections: **43 erreurs** (réduction 70%)
- Réflexion détaillée en français (230 lignes)
- Tests unitaires: 2/2 ✓

---

## 📁 Fichiers Clés

**Infrastructure sécurisée:**
- `terraform/main.tf` - Fixes Terraform appliquées
- `k8s/deployment.yaml` - Hardening Kubernetes
- `docker/Dockerfile` - Sécurisation conteneur

**Analyses:**
- `reports/reflection.md` - Réflexion détaillée (230 lignes)
- `reports/summary.md` - Résumé des corrections

**Preuves:**
- `reports/checkov.json` - Avant les fixes
- `reports/checkov_after.json` - Après les fixes

---

## 🛠️ Prérequis

```bash
Python 3.11+
pip install -r ../../requirements.txt
# Installations supplémentaires
pip install checkov semgrep
```

---

## 🚀 Exécuter les tests

```bash
# Du dossier lab3/
python -m unittest discover tests -v

# Résultat attendu: 2/2 tests ✓
```

---

## 📊 Résumé des améliorations

| Composant | Avant | Après | Statut |
|-----------|-------|-------|--------|
| **Checkov Errors** | 147 | 43 | -70% ✓ |
| **Critical Issues** | 12 | 2 | -83% ✓ |
| **High Issues** | 35 | 8 | -77% ✓ |
| **Medium Issues** | 45 | 18 | -60% ✓ |
| **Low Issues** | 55 | 15 | -73% ✓ |

---

## 🔐 Corrections détaillées

### S3 Bucket Security
```python
# AVANT: Public access
s3_bucket = aws_s3_bucket(acl='public-read')

# APRÈS: Private with explicit policies
s3_bucket = aws_s3_bucket(acl='private')
block_public_access = enabled
```

### Kubernetes Security Context
```yaml
# APRÈS: Hardened security context
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop:
      - ALL
```

### Docker Non-Root User
```dockerfile
# APRÈS: Non-root user
USER appuser:appgroup
RUN useradd -m -u 1000 appuser
```

---

## 🎓 Concepts appliqués

- **IaC Security** - Sécurisation Terraform, Kubernetes, Docker
- **Vulnerability Scanning** - Checkov et Semgrep
- **Compliance** - Bonnes pratiques CIS benchmarks
- **Defense in Depth** - Sécurité multi-couches

---

## 📝 Notes importantes

1. **Complet:** Tous les fichiers IaC améliorés
2. **Mesuré:** Réduction de 70% des erreurs Checkov
3. **Documenté:** Chaque correction expliquée en détail
4. **Validé:** Tests unitaires vérifient les fixes

**Conclusion:** Lab 3 démontre comment réduire significativement les risques de sécurité infrastructure via IaC hardening.
