# Lab 3 - Résumé des Corrections de Sécurité

## Vue d'ensemble
**Objectif :** Identifier et corriger les mauvaises configurations de sécurité en Infrastructure-as-Code (IaC) sur Terraform, Kubernetes et Docker.

**Résultats :**
- **Problèmes corrigés :** 7 mauvaises configurations critiques/élevées
- **Outils utilisés :** Checkov (IaC) + Semgrep (règles personnalisées)
- **Amélioration :** Réduction de 70% des résultats Checkov (147 → 43 erreurs)

---

## Tableau détaillé des corrections

| # | Problème | Fichier | Avant | Après | Niveau de risque | Référence |
|---|---------|--------|-------|-------|------------------|-----------|
| 1 | Bucket S3 avec ACL publique | `terraform/main.tf` | `acl = "public-read"` | `acl = "private"` + bloc d'accès public | 🔴 Critique | [Meilleures pratiques AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) |
| 2 | Versioning S3 manquant | `terraform/main.tf` | Non configuré | `aws_s3_bucket_versioning` activé | 🟠 Élevé | [Protection des données S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ObjectVersioning.html) |
| 3 | Chiffrement S3 manquant | `terraform/main.tf` | Non configuré | Chiffrement côté serveur AES256 activé | 🔴 Critique | [Chiffrement S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html) |
| 4 | Groupe de sécurité ouvert | `terraform/main.tf` | Entrée : `0.0.0.0/0:443` | Limité à `203.0.113.0/24:443` | 🔴 Critique | [Groupes de sécurité AWS](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) |
| 5 | Politique IAM trop permissive | `terraform/main.tf` | Permissions administrateur | Limité à `s3:ListBucket`, `s3:GetObject` | 🟠 Élevé | [Principe du moindre privilège IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) |
| 6 | Conteneur K8s privilégié | `k8s/deployment.yaml` | `privileged: true`<br>`allowPrivilegeEscalation: true` | `privileged: false`<br>`allowPrivilegeEscalation: false`<br>`runAsNonRoot: true` | 🔴 Critique | [Contexte de sécurité K8s](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) |
| 7 | Image K8s non épinglée + Dockerfile non sécurisé | `k8s/deployment.yaml`<br>`docker/Dockerfile` | `nginx:latest`<br>`FROM ubuntu:latest`<br>`USER root` | `nginx:1.27.0` (épinglée)<br>`FROM ubuntu:22.04`<br>`USER appuser` (non-root) | 🟠 Élevé | [Meilleures pratiques d'épinglage d'images](https://kubernetes.io/docs/concepts/configuration/overview/) |

---

## Scénarios d'attaque évités

| Correction | Attaque évitée | Impact |
|-----------|------------------|--------|
| ACL S3 privée | Exfiltration de données, accès non autorisé | Prévient l'exposition accidentelle de données |
| Versioning S3 + chiffrement | Falsification de données, attaques par rançongiciel | Permet la récupération et la confidentialité |
| Groupe de sécurité restreint | Accès réseau non autorisé, balayage de ports | Limite la surface d'attaque aux IPs autorisées |
| Permissions IAM limitées | Escalade de privilèges, mouvement latéral | Applique le principe du moindre privilège |
| Conteneur K8s non-root | Fuite de conteneur, escalade de privilèges | Limite l'impact d'une compromission de conteneur |
| Système de fichiers en lecture seule | Persistance de logiciels malveillants, injection de code | Rend le conteneur inviolable |
| Images de conteneur épinglées | Attaques de chaîne d'approvisionnement (falsification) | Assure la reproductibilité et l'auditabilité |
