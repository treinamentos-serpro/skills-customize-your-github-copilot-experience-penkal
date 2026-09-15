# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST para gerenciar um catálogo de livros usando o framework FastAPI. Ao final, você deverá saber criar endpoints, validar dados com modelos Pydantic e retornar respostas HTTP adequadas.

## 📝 Tarefas

### 🛠️ Criar o endpoint de consulta

#### Descrição

Configure a aplicação FastAPI do arquivo `starter-code.py` e implemente os endpoints de consulta do catálogo em memória.

Para executar a API localmente, use:

```bash
uvicorn starter-code:app --reload
```

Depois, acesse `http://127.0.0.1:8000/docs` para explorar a documentação interativa.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI na variável `app`.
- Implementar `GET /` com uma mensagem indicando que a API está funcionando.
- Implementar `GET /books` para retornar todos os livros cadastrados.
- Implementar `GET /books/{book_id}` para retornar um livro específico.
- Retornar status HTTP `404` quando o `book_id` não existir.


### 🛠️ Adicionar criação e validação de livros

#### Descrição

Crie um modelo Pydantic para representar os dados recebidos ao cadastrar um livro e implemente a rota de criação.

#### Requisitos

O programa concluído deve:

- Definir um modelo `BookCreate` com os campos `title`, `author` e `year`.
- Validar que `title` e `author` não sejam vazios.
- Validar que `year` seja um número inteiro entre 0 e o ano atual.
- Implementar `POST /books` usando `BookCreate` no corpo da requisição.
- Gerar um novo identificador, armazenar o livro e retornar status HTTP `201`.
- Permitir testar respostas de validação usando a documentação em `/docs`.

Exemplo de requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "year": 1937
}
```


### 🛠️ Implementar atualização e remoção

#### Descrição

Complete a API adicionando operações para atualizar e remover livros existentes.

#### Requisitos

O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar `title`, `author` e `year`.
- Reutilizar o modelo de validação para impedir dados inválidos durante a atualização.
- Implementar `DELETE /books/{book_id}` para remover um livro.
- Retornar status HTTP `404` ao tentar atualizar ou remover um livro inexistente.
- Retornar o livro atualizado após uma operação `PUT`.
- Retornar status HTTP `204` após uma remoção bem-sucedida.
