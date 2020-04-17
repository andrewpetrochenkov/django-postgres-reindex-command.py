from django.core.management.base import BaseCommand
from django.db import connection

SQL = """
SELECT format('%s.%s',schemaname,indexname)
FROM pg_indexes
WHERE tablename NOT LIKE 'pg%'
ORDER BY format('%s.%s',schemaname,indexname)
"""

class Command(BaseCommand):
    def handle(self, *args, **options):
        cursor = connection.cursor()
        cursor.execute(SQL)
        for row in cursor.fetchall():
            schemaname, indexname = row[0].split('.')
            sql = """REINDEX INDEX "%s"."%s";""" % (schemaname,indexname)
            print(sql)
            try:
                cursor.execute(sql)
            except Exception as e:
                print('%s: %s' % (type(e),str(e)))
