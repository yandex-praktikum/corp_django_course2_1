import os


def test_exists_create_tables_sql_file(create_table_sql):
    """ Проверка нахождения sql файла для создания таблиц в БД. """
    assert os.path.exists(create_table_sql), (
        'Убедитесь, что в директорию blogicum добавлен файл create_tables.sql'
    )
