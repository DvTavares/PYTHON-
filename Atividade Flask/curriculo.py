from flask import Flask

app = Flask(__name__)


@app.route("/curriculo")
def exibir_curriculo():
    return """
    <h1>Meu Currículo</h1>
    
    <h2>Dados Pessoais</h2>
    <p><b>Nome:</b> João Silva</p>
    <p><b>E-mail:</b> joao.silva@email.com</p>
    <p><b>Telefone:</b> (11) 99999-9999</p>
    
    <h2>Objetivo Profissional</h2>
    <p>Atuar como Desenvolvedor Python / Flask Júnior.</p>
    
    <h2>Experiência Profissional</h2>
    <p><b>Empresa:</b> Tech Solutions (2024 - Atual)<br>
    <b>Cargo:</b> Estagiário em Desenvolvimento<br>
    <b>Funções:</b> Manutenção de scripts internos e criação de APIs simples.</p>
    
    <h2>Formação Acadêmica</h2>
    <p><b>Curso:</b> Análise e Desenvolvimento de Sistemas<br>
    <b>Instituição:</b> Faculdade de Tecnologia (Conclusão em 2026)</p>
    
    <h2>Habilidades</h2>
    <ul>
        <li>Python</li>
        <li>Flask</li>
        <li>HTML estrutural</li>
        <li>Git / GitHub</li>
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)
