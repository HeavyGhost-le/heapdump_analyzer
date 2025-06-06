# Heapdump Analyzer 🔍

> **Extract credentials, sessions, and cryptographic artifacts from Java heap dumps**  
> Inspired by Hack The Box's **Eureka** machine where `/actuator/heapdump` exposed sensitive data.

---

## 📌 Features
- **Credential Extraction**: Auto-detects `password=`, `PWD`, and other common patterns
- **HTTP Session Reconstruction**: Identifies cookies, headers, and parameters in memory
- **Cryptographic Artifacts**: Flags keys, certificates, and high-entropy strings
- **Risk Scoring**: Quantifies exposure (e.g., `22.4/100` = low risk)
- **Multi-Format Reports**: JSON, HTML, and plaintext outputs

---

## 🚀 Quick Start
### Installation
```bash
git clone https://github.com/HeavyGhost-le/heapdump_analyzer.git
cd heapdump_analyzer
pip install -r requirements.txt
