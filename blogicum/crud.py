def get_published_posts_count(cur) -> list[tuple]:
    # Напишите SQL запрос в строке.
    sql = '''

    '''

    results = cur.execute(sql)
    return [row for row in results]


def get_top_5_posts(cur) -> list[tuple]:
    # Напишите SQL запрос в строке.
    sql = '''

    '''
    results = cur.execute(sql)
    return [row for row in results]


def get_unique_authors(cur) -> list[tuple]:
    # Напишите SQL запрос в строке.
    sql = '''

    '''

    results = cur.execute(sql)
    return [row for row in results]


def get_category_avg_rating(cur) -> list[tuple]:
    # Напишите SQL запрос в строке.
    sql = '''

    '''
    results = cur.execute(sql)
    return [row for row in results]


def get_users_posts(cur) -> list[tuple]:
    # Напишите SQL запрос в строке.
    sql = '''

    '''
    results = cur.execute(sql)
    return [row for row in results]
