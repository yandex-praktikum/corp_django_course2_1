import sqlite3
from pathlib import Path

from pytest import fixture

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
DATABASE_FILE = BASE_DIR / "blogicum" / "db.sqlite"
CREATE_TABLES_SQL_FILE = BASE_DIR / "blogicum" / "create_tables.sql"


@fixture(scope="session")
def conn():
    con = sqlite3.connect(DATABASE_FILE)

    yield con

    con.close()


@fixture(scope="session")
def cur(conn):
    yield conn.cursor()


@fixture(scope="session")
def exists_tables_in_db(cur):
    cur.execute('''
        SELECT tbl_name
        FROM sqlite_master
        WHERE type='table';
    ''')

    return [item[0] for item in cur.fetchall()]


@fixture
def database_file():
    return DATABASE_FILE


@fixture
def create_table_sql():
    return CREATE_TABLES_SQL_FILE


EXPECTED_CATEGORIES = [
    # (id, title)
    (1, 'Наука'),
    (2, 'Юмор'),
    (3, 'Технологии')
]

EXPECTED_POSTS = [
    # (id, title, category_id, is_published, rating)
    (1, '10 лучших способов улучшить производительность вашего кода', 3, True, 4.5),
    (2, 'Как создать свой первый проект на Python', 1, True, 3.3),
    (3, '10 важных принципов объектно-ориентированного программирования', 3, True, 4.8),
    (4, 'Как использовать git для управления версиями вашего кода', 3, True, 4.2),
    (5, 'Лучшие анекдоты про программистов', 2, True, 3.7),
    (6, 'Как использовать алгоритмы для решения задач программирования', 1, True, 4.6),
    (7, '5 основных паттернов проектирования программного обеспечения', 3, False, None),
    (8, 'Как использовать Docker для управления окружением вашего приложения', 3, False, None),
    (9, 'Работа с базами данных в Python', 1, True, 4.1),
    (10, 'Как создать свою первую игру на языке программирования C#', 3, True, None)
]

EXPECTED_AUTHORS = [
    # (id, username, first_name, second_name)
    (1, 'petr_ivanov95', 'Петр', 'Кузнецов'),
    (2, 'ann_smith', 'Анна', 'Смирнова'),
    (3, 'max2010', 'Максим', None),
    (4, 'maria_777', 'Мария', 'Иванова'),
    (5, 'alex_king', 'Александр', None)
]

EXPECTED_POSTS_AUTHORS = [
    # (post_id, author_id)
    (1, 1),
    (1, 2),
    (2, 1),
    (3, 2),
    (3, 3),
    (4, 1),
    (4, 2),
    (5, 2),
    (6, 1),
    (6, 2),
    (6, 3),
    (7, 2),
    (8, 1),
    (9, 3),
    (10, 1),
    (10, 2)
]


def check_count_columns(expected_columns: int, actual_result: list, function_name: str):
    """ Функция проверяет ожидаемое количество полей в результирующей выборке запроса. """
    actual_columns = len(actual_result[0])
    assert not (actual_columns < expected_columns), (
        f'Убедитесь, что в SQL запросе в функции `{function_name}` '
        'в результирующую выборку попали все необходимые поля.'
    )
    assert not (actual_columns > expected_columns), (
        f'Убедитесь, что в SQL запросе в функции `{function_name}` '
        'в результирующую выборку не попали лишние поля.'
    )


def check_non_empty_actual_result(actual_result: list, function_name: str):
    """ Функция проверяет, что результирующая выборка не пустая и возвращается как список кортежей. """
    assert isinstance(actual_result, list), (
        f'Убедитесь, что результат функции `{function_name}` - это список.'
    )

    assert actual_result, (
        f'Убедитесь, что результат функции `{function_name}` не пустой список.'
    )

    for item in actual_result:
        assert isinstance(item, tuple), (
            f'Убедитесь, что результат функции `{function_name}` - это список кортежей.'
        )
