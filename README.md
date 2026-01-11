![License](https://img.shields.io/badge/License-MIT-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green?logo=flask)
![pqcrypto](https://img.shields.io/badge/pqcrypto-0.3.4-purple)
![Demo Screenshot](Console.png)
![Demo Screenshot](Quantum_key.png)

# PQC Flask Demo - ML-KEM-1024 Key Exchange

Simple proof-of-concept for post-quantum key encapsulation using the **pqcrypto** library (ML-KEM-1024 / Kyber1024 – NIST FIPS 203 standard).

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green?logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow)

### Features
- Generate quantum-resistant keypair
- Key encapsulation (encap)
- Key decapsulation (decap)
- Modern quantum-themed responsive UI with copy buttons

### Tech Stack
- Python 3.11+
- Flask
- pqcrypto (pure Python post-quantum cryptography)

### Quick Start
```bash
git clone https://github.com/QSN-Tech/pqc-flask-demo.git
cd pqc-flask-demo
pip install -r requirements.txt
python app.py


