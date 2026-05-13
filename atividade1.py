from flask import Flask

app = Flask(__name__)


@app.route("/decorator")
def explicar_decorator():
    return """
    <h1>O que é um Decorator em Python?</h1>
    <p>Um <b>decorator</b> (decorador) é uma função que recebe outra função como argumento, estende o seu comportamento sem modificá-la explicitamente, e retorna uma nova função.</p>
    
    <h2>Para que serve?</h2>
    <ul>
        <li><b>Reutilização de código:</b> Evita repetição de lógica comum.</li>
        <li><b>Separação de conceitos:</b> Mantém o foco da função principal apenas na sua regra de negócio.</li>
        <li><b>Aplicações comuns:</b> Controle de acesso (autenticação), criação de logs, medição de tempo de execução e cache.</li>
    </ul>
    
    <h2>Como ele é utilizado no Flask?</h2>
    <p>No Flask, os decorators são fundamentais para o gerenciamento de rotas. O exemplo mais clássico é o <code>@app.route()</code>.</p>
    <p>Quando você usa <code>@app.route('/decorator')</code> antes de uma função, você está "decorando" essa função. O Flask intercepta a requisição do navegador, processa o caminho da URL e direciona o fluxo para a função correspondente, injetando essa lógica de roteamento por trás dos panos.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
