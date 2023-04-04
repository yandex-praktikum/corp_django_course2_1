from tests.conftest import check_count_columns, check_non_empty_actual_result


def test_get_published_posts_count(cur):
    function_name = 'get_published_posts_count'
    try:
        from crud import get_published_posts_count
    except Exception as e:
        raise AssertionError(
            f'При импорте функции `{function_name}` из файла `blogicum/crud.py` '
            f'произошла ошибка: {e}') from e

    actual_result = get_published_posts_count(cur)
    check_non_empty_actual_result(actual_result, function_name)

    expected_result = [(4,)]
    expected_columns = 1
    check_count_columns(expected_columns, actual_result, function_name)

    assert len(actual_result) == 1, (
        f'Убедитесь, что в SQL запросе в функции {function_name} '
        f'применена агрегирующая функция, '
        f'которая возвращает количество строк в результирующей выборке.'
    )

    assert expected_result == actual_result, (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'верно учтены все условия фильтрации результирующей выборки.'
    )


def test_get_top_5_posts(cur):
    function_name = 'get_top_5_posts'
    try:
        from crud import get_top_5_posts
    except Exception as e:
        raise AssertionError(
            f'При импорте функции `{function_name}` из файла `blogicum/crud.py` '
            f'произошла ошибка: {e}') from e

    actual_result = get_top_5_posts(cur)
    check_non_empty_actual_result(actual_result, function_name)

    expected_result = [
        (3, '10 важных принципов объектно-ориентированного программирования', 3, 1, 4.8),
        (6, 'Как использовать алгоритмы для решения задач программирования', 1, 1, 4.6),
        (1, '10 лучших способов улучшить производительность вашего кода', 3, 1, 4.5),
        (4, 'Как использовать git для управления версиями вашего кода', 3, 1, 4.2),
        (9, 'Работа с базами данных в Python', 1, 1, 4.1)
    ]
    expected_columns = 5
    check_count_columns(expected_columns, actual_result, function_name)

    assert len(expected_result) == len(actual_result), (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'используется ограничение количества строк, возвращаемых в результирующей выборке.'
    )

    assert expected_result == actual_result, (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'поля перечислены в нужном порядке и выполнена сортировка результирующей выборки.'
    )


def test_get_unique_authors(cur):
    function_name = 'get_unique_authors'
    try:
        from crud import get_unique_authors
    except Exception as e:
        raise AssertionError(
            f'При импорте функции `{function_name}` из файла `blogicum/crud.py` '
            f'произошла ошибка: {e}') from e

    actual_result = get_unique_authors(cur)
    check_non_empty_actual_result(actual_result, function_name)

    expected_result = [
        ('ann_smith',),
        ('max2010',),
        ('petr_ivanov95',)
    ]
    expected_columns = 1
    check_count_columns(expected_columns, actual_result, function_name)

    assert len(expected_result) == len(actual_result), (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'используется инструкция для получения уникальных значений из заданного поля.'
    )

    assert expected_result == actual_result, (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'поля перечислены в нужном порядке и выполнена сортировка результирующей выборки.'
    )


def test_get_category_avg_rating(cur):
    function_name = 'get_category_avg_rating'
    try:
        from crud import get_category_avg_rating
    except Exception as e:
        raise AssertionError(
            f'При импорте функции `{function_name}` из файла `blogicum/crud.py` '
            f'произошла ошибка: {e}') from e

    actual_result = get_category_avg_rating(cur)
    check_non_empty_actual_result(actual_result, function_name)

    expected_result = [
        ('Технологии', 4.5),
        ('Наука', 4.0),
    ]
    expected_columns = 2
    check_count_columns(expected_columns, actual_result, function_name)

    assert len(expected_result) == len(actual_result), (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'используется инструкция для фильтрации групп в результирующей выборке.'
    )

    assert expected_result == actual_result, (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'поля перечислены в нужном порядке и выполнена сортировка результирующей выборки.'
    )


def test_get_users_posts(cur):
    function_name = 'get_users_posts'
    try:
        from crud import get_users_posts
    except Exception as e:
        raise AssertionError(
            f'При импорте функции `{function_name}` из файла `blogicum/crud.py` '
            f'произошла ошибка: {e}') from e

    actual_result = get_users_posts(cur)
    check_non_empty_actual_result(actual_result, function_name)

    expected_result = [
        ('Иванова', 'Мария', None),
        ('Кузнецов', 'Петр', '10 лучших способов улучшить производительность вашего кода'),
        ('Кузнецов', 'Петр', 'Как использовать Docker для управления окружением вашего приложения'),
        ('Кузнецов', 'Петр', 'Как использовать git для управления версиями вашего кода'),
        ('Кузнецов', 'Петр', 'Как использовать алгоритмы для решения задач программирования'),
        ('Кузнецов', 'Петр', 'Как создать свой первый проект на Python'),
        ('Кузнецов', 'Петр', 'Как создать свою первую игру на языке программирования C#'),
        ('Смирнова', 'Анна', '10 важных принципов объектно-ориентированного программирования'),
        ('Смирнова', 'Анна', '10 лучших способов улучшить производительность вашего кода'),
        ('Смирнова', 'Анна', '5 основных паттернов проектирования программного обеспечения'),
        ('Смирнова', 'Анна', 'Как использовать git для управления версиями вашего кода'),
        ('Смирнова', 'Анна', 'Как использовать алгоритмы для решения задач программирования'),
        ('Смирнова', 'Анна', 'Как создать свою первую игру на языке программирования C#'),
        ('Смирнова', 'Анна', 'Лучшие анекдоты про программистов'),
    ]
    expected_columns = 3
    check_count_columns(expected_columns, actual_result, function_name)

    assert len(expected_result) == len(actual_result), (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'возвращаются все авторы с заполненной фамилией, даже если они не писали публикации.'
    )

    assert expected_result == actual_result, (
        f'Проверьте, что в SQL запросе в функции `{function_name}`: '
        'поля перечислены в нужном порядке и выполнена сортировка результирующей выборки.'
    )
