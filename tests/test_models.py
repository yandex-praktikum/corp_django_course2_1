import os
import sqlite3

import pytest

from tests.conftest import EXPECTED_CATEGORIES, EXPECTED_POSTS, EXPECTED_AUTHORS, EXPECTED_POSTS_AUTHORS


def test_exists_database_file(database_file):
    """ Проверка нахождения БД в нужном месте. """
    assert os.path.exists(database_file), (
        'Убедитесь, что в директорию blogicum добавлен файл db.sqlite'
    )


@pytest.mark.parametrize(
    "variable_name, expected_result",
    [
        ("categories", EXPECTED_CATEGORIES),
        ("posts", EXPECTED_POSTS),
        ("authors", EXPECTED_AUTHORS),
        ("posts_authors", EXPECTED_POSTS_AUTHORS),
    ]
)
def test_data_for_insert_in_table(variable_name, expected_result):
    try:
        import models
        solution_list_values = getattr(models, variable_name)
    except Exception as e:
        raise AssertionError(
            f'При импорте списка `{variable_name}` из файла `models.py` '
            f'произошла ошибка: {e}') from e
    assert solution_list_values == expected_result, (
        f'Убедитесь, что список `{variable_name}` из файла `models.py` '
        'соответствует списку кортежей из задания.')


@pytest.mark.parametrize(
    "table, columns, expected_result",
    [
        ("categories", ("id", "title"), EXPECTED_CATEGORIES),
        ("posts", ("id", "title", "category_id", "is_published", "rating"), EXPECTED_POSTS),
        ("authors", ("id", "username", "first_name", "second_name"), EXPECTED_AUTHORS),
        ("posts__authors", ("post_id", "author_id"), EXPECTED_POSTS_AUTHORS),
    ]
)
def test_inserted_in_db_data(cur, exists_tables_in_db, table, columns, expected_result):
    assert table in exists_tables_in_db, (
        f'Проверьте, что в файле `create_tables.sql` добавлен скрипт для создания таблицы `{table}`'
    )
    try:
        cur.execute(f"""
        SELECT 
            {', '.join(columns)}
        FROM {table}
        """)
    except sqlite3.OperationalError as e:
        raise AssertionError(
            f'При получении всех полей из таблицы `{table}`'
            f'произошла ошибка: {e}') from e

    actual_result = cur.fetchall()
    assert actual_result == expected_result, (
        f'Убедитесь, что все все значения списка `{table.replace("__", "_")}` '
        f'из файла `models.py` вставились в таблицу `{table}`.'
    )
