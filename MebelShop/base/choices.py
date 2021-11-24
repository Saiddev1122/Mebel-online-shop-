def default_price():
    return [
        ("UZS", 'UZS'),
        ("USD", 'USD'),
        ("RUB", 'RUB'),
    ]


def default_size():
    return {"length": "", "width": "", "heigth": ""}


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    columns = [col[0] for col in cursor.description]
    if row is None:
        return False
    return dict(zip(columns, row))
