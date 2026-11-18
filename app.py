
from flask import Flask, request, jsonify, render_template
import operacoes

app = Flask(__name__)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")


# Página de soma
@app.route("/soma")
def soma_page():
    return render_template("soma.html")

@app.route("/api/soma", methods=["POST"])
def soma():
    dados = request.get_json()
    valor1 = float(dados["valor1"])
    valor2 = float(dados["valor2"])

    resultado = operacoes.calcular_soma(valor1, valor2)

    return jsonify({"resultado": resultado})


# Página de subtração
@app.route("/subtracao")
def subtracao_page():
    return render_template("subtracao.html")

@app.route("/api/subtracao", methods=["POST"])
def subtracao():
    dados = request.get_json()
    valor1 = float(dados["valor1"])
    valor2 = float(dados["valor2"])

    resultado = operacoes.calcular_subtracao(valor1, valor2)

    return jsonify({"resultado": resultado})


# Página de multiplicação
@app.route("/multiplicacao")
def multiplicacao_page():
    return render_template("multiplicacao.html")

@app.route("/api/multiplicacao", methods=["POST"])
def multiplicacao():
    dados = request.get_json()
    valor1 = float(dados["valor1"])
    valor2 = float(dados["valor2"])

    resultado = operacoes.calcular_multiplicacao(valor1, valor2)

    return jsonify({"resultado": resultado})


# Página de divisão
@app.route("/divisao")
def divisao_page():
    return render_template("divisao.html")

@app.route("/api/divisao", methods=["POST"])
def divisao():
    dados = request.get_json()
    valor1 = float(dados["valor1"])
    valor2 = float(dados["valor2"])

    if valor2 == 0:
        return jsonify({"erro": "Não é possível dividir por zero!"}), 400

    resultado = operacoes.calcular_divisao(valor1, valor2)

    return jsonify({"resultado": resultado})


# Executar aplicação
if __name__ == "__main__":
    app.run(debug=True)