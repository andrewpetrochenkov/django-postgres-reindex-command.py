from setuptools import setup

setup(
    name='django-postgres-reindex-command',
    version='2020.4.16',
    install_requires=[
        'Django',
        'click',
        'setuptools',
    ],
    packages=[
        'django_postgres_reindex_command',
        'django_postgres_reindex_command.management',
        'django_postgres_reindex_command.management.commands',
    ],
)
