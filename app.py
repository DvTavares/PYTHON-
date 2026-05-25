
from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("calculadora.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    dados = request.get_json()
    expressao = dados.get("expressao")

    try:
        resultado = eval(expressao, {
            "__builtins__": None
        }, {
            "sqrt": math.sqrt,
            "pow": pow,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pi": math.pi
        })

        return jsonify({
            "resultado": str(resultado)
        })

    except:
        return jsonify({
            "resultado": "Erro"
        })

if __name__ == "__main__":
    app.run(debug=True)