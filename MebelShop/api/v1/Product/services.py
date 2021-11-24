import ast
from collections import OrderedDict
from contextlib import closing

from django.db import connection

from base.choices import dictfetchall, dictfetchone


def list_product(requests):
    sql = f"""
    
    select msp.id,msp.title,msp.price,msp.price_type,msp.is_active,msp.size as sizee, ctg."content" 
    from mebel_site_product msp 
    inner join mebel_site_category ctg on msp.ctg_id = ctg.id
    
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
    select msp.id,msp.title,msp.price,msp.price_type,msp.is_active,msp.size as sizee, ctg."content" 
    from mebel_site_product msp 
    left join mebel_site_category ctg on msp.ctg_id = ctg.id 
    where msp.id=%s 

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

    if data['content']:
        ctg = OrderedDict([
            ("uz", ast.literal_eval(data['content'])['uz']),
            ("ru", ast.literal_eval(data['content'])['ru'])
        ])
    else:
        ctg = None

    return OrderedDict(
        [
            ('id', data['id']),
            ('title', name),
            ('price', data['price']),
            ('price_type', data['price_type']),
            ('is_active', data['is_active']),
            ('size', data['sizee']),
            ('ctg', ctg),
        ]
    )
