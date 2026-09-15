# 📘 Atividade: Consumindo APIs com Python

## 🎯 Objetivo

Aprenda a consumir uma API REST usando Python e a biblioteca `requests`. Você irá enviar requisições `GET`, trabalhar com respostas JSON, usar parâmetros de consulta e tratar erros de rede e de HTTP.

## 📝 Tarefas

### 🛠️ Fazer uma requisição e ler a resposta

#### Descrição

Complete a função `fetch_todos()` no arquivo inicial para buscar tarefas da API JSONPlaceholder e transformar a resposta em dados Python.

Para instalar a dependência e executar o programa, use:

```bash
python -m pip install requests
python starter-code.py
```

#### Requisitos

O programa concluído deve:

- Fazer uma requisição `GET` para `https://jsonplaceholder.typicode.com/todos` usando `requests`.
- Converter a resposta para JSON e retornar uma lista de dicionários.
- Exibir o título e o status das cinco primeiras tarefas recebidas.

### 🛠️ Usar parâmetros de consulta

#### Descrição

Adapte o programa para permitir que o usuário escolha um identificador de usuário e busque apenas as tarefas desse usuário.

#### Requisitos

O programa concluído deve:

- Ler um `userId` inteiro informado pelo usuário.
- Enviar esse valor como parâmetro de consulta, sem montar a URL por concatenação de strings.
- Exibir quantas tarefas foram encontradas e quantas estão concluídas.
- Exibir uma mensagem adequada quando a API retornar uma lista vazia.

### 🛠️ Tratar falhas da API

#### Descrição

Torne o programa mais confiável para que ele continue informando o usuário quando houver um erro de HTTP, uma falha de conexão ou uma resposta que não possa ser interpretada como JSON.

#### Requisitos

O programa concluído deve:

- Verificar respostas HTTP malsucedidas com `raise_for_status()` ou uma validação equivalente.
- Tratar separadamente erros de requisição da biblioteca `requests` e erros de decodificação JSON.
- Usar um tempo limite (`timeout`) na requisição.
- Exibir uma mensagem clara para o usuário sem mostrar um traceback quando a API estiver indisponível.
