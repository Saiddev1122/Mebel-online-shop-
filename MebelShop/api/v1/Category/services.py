import ast
from collections import OrderedDict
from contextlib import closing

from base.choices import dictfetchall, dictfetchone
from django.db import connection
from django.conf import settings


def list_category(requests):
    sql = "select  id, msc.content as name ,slug,is_active,is_main from mebel_site_category msc "
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
            select  id,  msc.content as name ,slug,is_active,is_main 
            from mebel_site_category msc 
            where id=%s 
            
          """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        result = _format(dictfetchone(cursor))
    return OrderedDict([
        ('item', result)
    ])


def _format(data):
    if data['name']:
        name = OrderedDict([
            ("uz", ast.literal_eval(data['name'])['uz']),
            ("ru", ast.literal_eval(data['name'])['ru'])
        ])
    else:
        name = None

    return OrderedDict(
        [
            ('id', data['id']),
            ('content', name),
            ('slug', data['slug']),
            ('is_active', data['is_active']),
            ('is_main', data['is_main']),
        ]
    )
