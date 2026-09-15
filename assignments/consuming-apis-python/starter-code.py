"""Starter code for the Consuming APIs with Python assignment."""

import requests


API_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_todos(user_id=None):
    """Fetch todos from the API, optionally filtering by user id."""
    params = {"userId": user_id} if user_id is not None else {}

    # TODO: send the GET request, validate the response, and return its JSON data.
    pass


def summarize_todos(todos):
    """Return the total and completed todo counts."""
    # TODO: calculate both counts from the list of todo dictionaries.
    pass


def main():
    user_id = input("Digite um userId (1 a 10): ").strip()

    # TODO: convert user_id to an integer and handle request/JSON errors gracefully.
    todos = fetch_todos(user_id)
    total, completed = summarize_todos(todos)

    print(f"Tarefas encontradas: {total}")
    print(f"Tarefas concluídas: {completed}")


if __name__ == "__main__":
    main()