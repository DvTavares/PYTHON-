# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

**Nome:** Davi Tavares

**Turma:** 3b1

## Bloco A — Model

**1.** As classes que representam tabelas do banco ficam na pasta `models/`. Caminho: `flask/Aula12/models/`.
wssw
**2.** O arquivo de banco criado é `streamflix.db`. A configuração está no arquivo `app.py`, na linha que define `SQLALCHEMY_DATABASE_URI`.

**3.**

* Classe `FilmeFavorito` → arquivo `models/filme_favorito.py`
* Classe `HistoricoBusca` → arquivo `models/historico_busca.py`
* Classe `ModeloBase` → arquivo `models/base.py`

**4.** `FilmeFavorito` e `HistoricoBusca` herdam da superclasse `ModeloBase`. Elas recebem automaticamente os campos:

* `id`
* `data_criacao`
* `data_atualizacao`

**5.** O `__tablename__` da tabela de favoritos é `"filmes_favoritos"`. Usamos `__tablename__` para definir explicitamente o nome da tabela no banco, independente do nome da classe.

**6.** A coluna que guarda o id do filme vindo da TMDB é `tmdb_id`. Ela possui as restrições:

* `nullable=False`
* `unique=True`

**7.** O método `adicionar()`:

1. Verifica se o filme já existe usando `buscar_por_tmdb()`.
2. Se existir, retorna `None`.
3. Se não existir, cria um objeto `FilmeFavorito`.
4. Adiciona o objeto na sessão com `db.session.add()`.
5. Salva no banco com `db.session.commit()`.
6. Retorna o objeto criado.

Se o filme já existir, ele não é salvo novamente.

**8.** O método que lista as últimas 8 buscas está na classe `HistoricoBusca`, no método `ultimas()`, localizado em `models/historico_busca.py`.

**9.** O model salva apenas alguns campos espelhados da API, não a resposta inteira. Campos salvos:

* `tmdb_id`
* `titulo`
* `poster_path`
* `nota`
* `ano`

**10.** Além de `db`, o arquivo `models/__init__.py` exporta:

* `ModeloBase`
* `FilmeFavorito`
* `HistoricoBusca`

O controller importa `from models import FilmeFavorito` porque o `__init__.py` já centraliza as importações, facilitando o uso do código.

---

## Bloco B — Controller

**11.** Existem 3 Blueprints:

* `dashboard_bp` → sem `url_prefix`
* `filmes_bp` → `url_prefix="/filmes"`
* `favoritos_bp` → `url_prefix="/favoritos"`

**12.** A rota `/filmes/populares` está em `controllers/filmes_controller.py`. A função responsável é `populares()`.

**13.** Antes de chamar `render_template`, a função:

* Chama `api.filmes_populares()`
* Chama `FilmeFavorito.listar()`

**14.** O controller é `filmes_controller.py`. O model utilizado é `HistoricoBusca`, através da chamada:

```python
HistoricoBusca.registrar(termo, len(filmes))
```

aproximadamente no meio da função `buscar()`.

**15.** O método HTTP exigido é `POST`.

Exemplo de URL:

```text
/favoritos/adicionar/550
```

**16.** Se `api.detalhe(filme_id)` retornar `None`, o usuário é redirecionado para a página de filmes populares.

**17.** Os Blueprints são registrados em `app.py` usando:

```python
app.register_blueprint(dashboard_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)
```

**18.** O controller responsável pela página inicial é `dashboard_controller.py`.

Ele envia para o template:

* `populares`
* `melhores`
* `total_favoritos`
* `historico`
* `modo_demo`

**19.** `services/tmdb_api.py` não é Model, Controller nem View. É uma camada de serviço (Service). Ela é chamada pelos controllers para buscar informações na API da TMDB.

**20.** O formulário da home usa `request.args`, pois é enviado por método `GET`.

Diferença:

* `request.args` → dados enviados pela URL (`GET`)
* `request.form` → dados enviados no corpo da requisição (`POST`)

Neste projeto, a busca da home usa GET e outras ações, como salvar favorito, usam POST.

---

## Bloco C — View

**21.** Os templates HTML ficam em:

```text
views/templates/
```

**22.** O template base é `views/templates/layout.html`.

Os outros templates utilizam:

```jinja
{% extends "layout.html" %}
```

**23.** Links do menu:

* StreamFlix → `url_for('dashboard.index')`
* Populares → `url_for('filmes.populares')`
* Melhores → `url_for('filmes.melhores')`
* Buscar → `url_for('filmes.buscar')`
* Favoritos → `url_for('favoritos.listar')`

**24.** O arquivo é `views/templates/filmes/detalhe.html`.

A variável `streaming` vem do controller `filmes_controller.py` através da chamada:

```python
streaming, demo = api.streaming(filme_id)
```

**25.** `filmes/_card.html` é um componente reutilizável, não uma página completa.

Ele é incluído com:

```jinja
{% include "filmes/_card.html" %}
```

nos templates `index.html`, `filmes/lista.html` e `filmes/buscar.html`.

**26.** A View verifica a variável `favorito`.

```jinja
{% if favorito %}
```

Se existir, mostra "Remover dos favoritos". Caso contrário, mostra "Salvar favorito".

**27.** O CSS está em:

```text
views/static/css/style.css
```

Ele é carregado no layout usando:

```jinja
{{ url_for('static', filename='css/style.css') }}
```

**28.** O loop é:

```jinja
{% for fav in favoritos %}
```

Campos exibidos:

* `fav.titulo`
* `fav.nota`
* `fav.ano`
* `fav.data_criacao`

**29.** `{% if modo_demo %}` verifica se o sistema está funcionando em modo demonstração.

A variável é disponibilizada para todos os templates pelo `@app.context_processor` localizado em `app.py`.

**30.** Fluxo completo para salvar favorito:

1. O usuário clica em **Salvar favorito** na View `views/templates/filmes/detalhe.html`.
2. O formulário envia um `POST` para:

```text
/favoritos/adicionar/<tmdb_id>
```

3. O controller `controllers/favoritos_controller.py`, função `adicionar()`, recebe os dados.
4. O controller chama:

```python
FilmeFavorito.adicionar(...)
```

5. O model `models/filme_favorito.py` grava os dados no banco SQLite.
6. Após salvar, o controller executa:

```python
redirect(voltar)
```

7. O usuário retorna para a página de detalhes do filme.


## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
