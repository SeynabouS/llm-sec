# Lab 3 - Réflexion et Analyse de Sécurité

**Auteurs :** Seynabou SOUGOU, Maxime XU  
**Classe :** ING 5 APP Groupe 2  
**Date :** 31/12/2025

---

## 1. Résumé exécutif

Ce lab s'est concentré sur le durcissement des configurations Infrastructure-as-Code (IaC) dans trois domaines critiques :
- **Terraform :** Infrastructure cloud AWS (S3, groupes de sécurité, IAM)
- **Kubernetes :** Orchestration de conteneurs (manifestes de déploiement)
- **Docker :** Images de conteneur (environnement d'exécution)

Grâce à un balayage et une correction systématiques, nous avons réalisé une **réduction de 70% des résultats Checkov** et éliminé toutes les violations de règles personnalisées Semgrep, démontrant une amélioration significative de la posture de sécurité de la pile IaC.

---

## 2. Évaluation initiale de la sécurité

### Résultats des balayages initiaux (AVANT les corrections)

| Outil | Nombre de résultats | Problèmes critiques |
|------|-------|------------------|
| **Checkov** | 147 vérifications échouées | ACL S3 public, groupe de sécurité ouvert, stockage non chiffré |
| **Semgrep** | 6 résultats | Paramètres par défaut non sécurisés dans Kubernetes et Docker |
| **Risque global** | 🔴 **ÉLEVÉ** | Infrastructure exposée à plusieurs vecteurs d'attaque |

### Vulnérabilités clés identifiées
1. **Bucket S3 publiquement lisible** → Risque d'exfiltration de données
2. **Pas de chiffrement ou versioning** → Perte de données et violations de conformité
3. **Groupe de sécurité ouvert à 0.0.0.0/0** → Accès réseau sans restriction
4. **Politique IAM trop permissive** → Risque d'escalade de privilèges
5. **Conteneurs K8s privilégiés** → Vulnérabilité de fuite de conteneur
6. **Images de conteneur sans tag/latest** → Vecteur d'attaque de chaîne d'approvisionnement
7. **Utilisateur root dans Docker** → Amplification de l'impact après compromission

---

## 3. Actions de remédiation et justifications

### Durcissement Terraform (Infrastructure AWS)

**Correction 1 : Accès S3 public**
```hcl
# AVANT: acl = "public-read"
# APRÈS:  acl = "private" + aws_s3_bucket_public_access_block
```
**Justification :** Les buckets S3 AWS ne doivent jamais être publiquement lisibles par défaut. Ajout d'un bloc d'accès public pour la défense en profondeur.

**Correction 2 : Protection des données manquante**
```hcl
# AJOUTÉE:
# - aws_s3_bucket_versioning (permet le retour en arrière)
# - aws_s3_bucket_server_side_encryption (AES256)
```
**Justification :** Le chiffrement protège la confidentialité ; le versioning prévient les attaques par rançongiciel et permet la récupération.

**Correction 3 : Accès réseau sans restriction**
```hcl
# AVANT: cidr_blocks = ["0.0.0.0/0"]  # Ouvert à Internet
# APRÈS:  cidr_blocks = ["203.0.113.0/24"]  # Réseau de confiance spécifique
```
**Justification :** Implémente l'accès réseau du moindre privilège. Seules les IPs autorisées peuvent accéder au port 443.

**Correction 4 : Politique IAM trop permissive**
```json
# AVANT: Action = "*" sur toutes les ressources
# APRÈS:  Action = ["s3:ListBucket", "s3:GetObject"] sur le bucket spécifique
```
**Justification :** Suit les meilleures pratiques AWS IAM. Chaque rôle/utilisateur n'obtient que les permissions nécessaires.

### Durcissement Kubernetes (Orchestration de conteneurs)

**Correction 5 : Contexte de sécurité non sécurisé**
```yaml
# AVANT:
securityContext:
  privileged: true
  allowPrivilegeEscalation: true

# APRÈS:
securityContext:
  privileged: false
  allowPrivilegeEscalation: false
  runAsNonRoot: true
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
```
**Justification :**
- `privileged: false` → Prévient les exploitations de fuite de conteneur
- `allowPrivilegeEscalation: false` → Bloque l'escalade de capacité
- `runAsNonRoot: true` → Limite les dommages après compromission
- `readOnlyRootFilesystem: true` → Rend le système de fichiers immuable (prévient la persistance de logiciels malveillants)

**Correction 6 : Image de conteneur sans tag**
```yaml
# AVANT: image: nginx:latest
# APRÈS:  image: nginx:1.27.0
```
**Justification :** Le tag `latest` n'est pas déterministe et vulnérable aux attaques de chaîne d'approvisionnement. L'épinglage assure la reproductibilité et permet le retour en arrière.

### Durcissement Docker (Image de conteneur)

**Correction 7 : Image de base non sécurisée et utilisateur**
```dockerfile
# AVANT:
FROM ubuntu:latest
USER root

# APRÈS:
FROM ubuntu:22.04
RUN useradd -m appuser
USER appuser
```
**Justification :**
- Version épinglée → Builds reproductibles, base de vulnérabilité connue
- Utilisateur non-root → Limite l'impact d'une compromission de conteneur
- Création d'utilisateur explicite → Prévient l'exécution accidentelle en root

**Améliorations de sécurité ajoutées :**
- Inclusion de `ca-certificates` pour la validation HTTPS
- Séparation du téléchargement curl de l'exécution (prévient l'injection de code arbitraire)
- Ajout de `--no-install-recommends` pour réduire la surface d'attaque

---

## 4. Évaluation post-remédiation

### Résultats des balayages (APRÈS les corrections)

| Outil | Nombre de résultats | Changement | Statut |
|------|----------------|--------|--------|
| **Checkov** | 43 vérifications échouées | ↓ 104 (réduction de 70%) | ✅ **Amélioration majeure** |
| **Semgrep** | 0 résultats | ↓ 6 (100% corrigé) | ✅ **Toutes les règles personnalisées réussies** |
| **Risque global** | 🟡 **MOYEN** | Acceptable pour la production avec réserves |

### Analyse des résultats restants

Les 43 résultats Checkov restants sont principalement :
- **Avertissements mineurs** (recommandations de marquage de ressources)
- **Suggestions de meilleures pratiques** (pas de problèmes critiques de sécurité)
- **Préférences de configuration** (spécifiques à l'environnement)

**Aucune n'est une vulnérabilité critique.** La pile est désormais convenable pour le déploiement en production.

---

## 5. Patterns de sécurité et leçons apprises

### Mauvaises configurations les plus courantes (causes racines)

1. **Insécurité par défaut :** Les outils et plateformes utilisent par défaut les tags `latest`, les utilisateurs root et les politiques permissives par commodité, pas par sécurité.
2. **Manque du principe du moindre privilège :** Les développeurs sur-provisionent souvent les permissions au lieu d'auditer ce qui est réellement nécessaire.
3. **Absence de défense en profondeur :** Un seul contrôle défaillant (ex. ACL S3 public) au lieu de défenses multicouches (ACL + versioning + chiffrement).
4. **Confiance implicite :** Les configurations font confiance à tous les utilisateurs/réseaux par défaut au lieu d'exiger une liste d'autorisation explicite.

### Vecteurs d'attaque éliminés

| Vecteur d'attaque | Prévenu par | Réduction du risque |
|---|---|---|
| Exfiltration de données | ACL S3 privée + bloc d'accès public | 🔴 → 🟡 |
| Falsification de données/rançongiciel | Versioning + chiffrement | 🔴 → 🟡 |
| Accès réseau non autorisé | Groupe de sécurité restreint (CIDR) | 🔴 → 🟡 |
| Escalade de privilèges | Utilisateur non-root + aucune escalade de privilèges | 🔴 → 🟡 |
| Fuite de conteneur | Privileged=false + système de fichiers en lecture seule | 🔴 → 🟡 |
| Attaques de chaîne d'approvisionnement | Images de conteneur épinglées + versions | 🔴 → 🟡 (atténué) |

---

## 6. Intégration CI/CD et stratégie de prévention

### Contrôles recommandés pour la production

**1. Crochets pré-commit**
```bash
# Balayer l'IaC avant de commit
checkov -d . --check CKV_AWS_*,CKV_K8S_*
semgrep --config config/semgrep_rules.yml
```

**2. Portes du pipeline CI/CD**
```yaml
# Bloquer la fusion si des problèmes critiques sont trouvés
if checkov --exit-code 1 fails on CRITICAL
  then REJECT_MERGE
```

**3. Normes de base à appliquer**
- ✅ Toutes les ressources cloud doivent utiliser IAM avec le moindre privilège
- ✅ Toutes les images de conteneur doivent être épinglées à des versions spécifiques
- ✅ Toutes les bases de données/stockages doivent utiliser le chiffrement au repos
- ✅ Tous les groupes de sécurité doivent utiliser des listes d'autorisation IP explicites (pas 0.0.0.0/0)
- ✅ Tous les pods K8s doivent s'exécuter en tant que non-root avec les capacités supprimées

**4. Décaler la sécurité à gauche (Shift-Left)**
- Former les développeurs aux paramètres par défaut sécurisés de l'IaC
- Créer des modules Terraform réutilisables avec la sécurité intégrée
- Maintenir un dépôt de politique sous forme de code (vérifications Checkov personnalisées)

---

## 7. Conclusion

Ce lab a démontré l'importance pratique du **durcissement de la sécurité de l'infrastructure**. En appliquant des principes de sécurité d'abord aux configurations IaC, nous avons :

1. **Réduit la surface de risque** de 70% (résultats Checkov)
2. **Éliminé les vulnérabilités critiques** (exposition S3, escalade de privilèges)
3. **Implémenté la défense en profondeur** (chiffrement + versioning + contrôle d'accès)
4. **Validé les améliorations** par balayage automatisé avant et après

La conclusion la plus critique : **la sécurité n'est pas un seul contrôle, mais une approche en couches.** Une seule mauvaise configuration (ex. ACL S3 public) peut être catastrophique, mais plusieurs contrôles superposés (ACL + chiffrement + versioning + audit logging) garantissent la résilience.

À l'avenir, l'intégration de ces outils de balayage dans les pipelines CI/CD empêchera les configurations non sécurisées d'atteindre la production, déplaçant le fardeau de la sécurité vers le moment du développement où il est moins cher à corriger.

---

### Fichiers modifiés
- `terraform/main.tf` → Durcissement S3, groupe de sécurité, IAM
- `k8s/deployment.yaml` → Contexte de sécurité, épinglage d'image
- `docker/Dockerfile` → Image de base, utilisateur non-root

### Artefacts générés
- `reports/checkov.json` (baseline)
- `reports/checkov_after.json` (post-remédiation)
- `reports/semgrep.json` (baseline)
- `reports/semgrep_after.json` (post-remédiation)
