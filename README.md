# PQC Flask Demo - ML-KEM-1024 Key Exchange

Simple proof-of-concept for post-quantum key encapsulation using **pqcrypto** library (ML-KEM-1024 / Kyber1024 – NIST standard).

**Features**
- Generate quantum-resistant keypair
- Key encapsulation (encap)
- Key decapsulation (decap)
- Modern quantum-themed UI with copy buttons

**Tech Stack**
- Python 3.11+
- Flask
- pqcrypto (post-quantum cryptography)

**Installation & Run**
```bash
git clone https://github.com/QSN-Tech/pqc-flask-demo.git
cd pqc-flask-demo
pip install -r requirements.txt

python app.py
