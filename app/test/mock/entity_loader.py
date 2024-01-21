import json
from pathlib import Path

base_path = Path(__file__).parent

# TODO: refactor scrivere funzione generica ed enumartiva che passa strategy


def load_active_paths(filename: str) -> str:

    with open(f'{base_path}/mocks/active_paths/{filename}') as fp:
        file = fp.read()
    return json.loads(file)


def load_messages(filename: str) -> str:

    with open(f'{base_path}/mocks/messages/{filename}') as fp:
        file = fp.read()
    return json.loads(file)


def load_message(filename: str) -> str:

    with open(f'{base_path}/mocks/message/{filename}') as fp:
        file = fp.read()
    return json.loads(file)
