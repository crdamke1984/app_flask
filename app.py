from flask import Flask, request, jsonify
from scipy.stats import gamma

app = Flask(__name__)

@app.route('/')
def home():
    return 'API de Previsão de Falhas (Distribuição Gama) - Render.com'

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.get_json()
    x = float(dados.get('x', 0))
    shape = float(dados.get('shape', 2))
    scale = float(dados.get('scale', 1))
    prob = gamma.pdf(x, shape, scale=scale)
    return jsonify({'x': x, 'probabilidade': prob})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
