from flask import Flask, request, jsonify, render_template, render_template_string
import binascii
from pqcrypto.kem.ml_kem_1024 import generate_keypair, encrypt, decrypt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    public_key, secret_key = generate_keypair()
    return jsonify({
        'public_key': binascii.hexlify(public_key).decode('utf-8'),
        'secret_key': binascii.hexlify(secret_key).decode('utf-8')
    })

@app.route('/encap', methods=['POST'])
def encap():
    data = request.json
    if not data or 'public_key' not in data:
        return jsonify({'error': 'Missing public_key'}), 400
    
    try:
        pk = binascii.unhexlify(data['public_key'])
        ciphertext, shared_secret = encrypt(pk)
        return jsonify({
            'ciphertext': binascii.hexlify(ciphertext).decode('utf-8'),
            'shared_secret': binascii.hexlify(shared_secret).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decap', methods=['POST'])
def decap():
    data = request.json
    if not data or 'ciphertext' not in data or 'secret_key' not in data:
        return jsonify({'error': 'Missing ciphertext or secret_key'}), 400
    
    try:
        ct = binascii.unhexlify(data['ciphertext'])
        sk = binascii.unhexlify(data['secret_key'])
        shared_secret = decrypt(ct, sk)
        return jsonify({
            'shared_secret': binascii.hexlify(shared_secret).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':

    app.run(debug=True, port=4000)
