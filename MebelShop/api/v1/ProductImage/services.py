import ast
from collections import OrderedDict
from contextlib import closing
from django.db import connection
from base.choices import dictfetchall, dictfetchone


def list_productimage(requests):
    sql = f"""

        select iii.id, iii.image, ppp.title 
        from mebel_site_productimage iii
        inner join mebel_site_product ppp on iii.product_id  = ppp.id 

    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        items = dictfetchall(cursor)
        result = []
        for i in items:
            result.append(_format(i))

    return OrderedDict([
        ('items', result)
    ])


def get_one(requestes, pk):
    sql = """ 
    select iii.id, iii.image, ppp.title 
    from mebel_site_productimage iii
    inner join mebel_site_product ppp on iii.product_id  = ppp.id  
    where iii.id=%s 
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        result = _format(dictfetchone(cursor))
    return OrderedDict([
        ('item', result)
    ])


def _format(data):
    if data['title']:
        name = OrderedDict([
            ("uz", ast.literal_eval(data['title'])['uz']),
            ("ru", ast.literal_eval(data['title'])['ru'])
        ])
    else:
        name = None

    return OrderedDict(
        [
            ('id', data['id']),
            ('title', name),
            ('image', data['image']),
        ]
    )
