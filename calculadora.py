import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            return render_template(
                "calculadora.html",
                etapas=f"Não existe raiz real de {num1}.",
                resultados="Erro: número negativo",
            )
        resultado = math.sqrt(num1)
        return render_template(
            "calculadora.html",
            etapas=f"√{num1} = {resultado}",
            resultados=resultado,
        )

    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="Erro",
        )
    num2 = float(num2_valor)

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2} = {resultado}"
    elif operacao == "/":
        if num2 == 0:
            return render_template(
                "calculadora.html",
                etapas="Divisão por zero não é permitida.",
                resultados="Erro",
            )
        resultado = num1 / num2
        etapas = f"{num1} ÷ {num2} = {resultado}"
    elif operacao == "**":
        resultado = num1 ** num2
        etapas = f"{num1} ^ {num2} = {resultado}"
    elif operacao == "log":
        if num1 <= 0 or num2 <= 0 or num2 == 1:
            return render_template(
                "calculadora.html",
                etapas="O logaritmando e a base devem ser > 0. A base deve ser diferente de 1.",
                resultados="Erro: Entrada inválida",
            )
        resultado = math.log(num1, num2)
        etapas = f"log na base {num2} de {num1} = {resultado}"
    else:
        return render_template(
            "calculadora.html",
            etapas="Operação inválida.",
            resultados="Erro",
        )

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado,
    )
