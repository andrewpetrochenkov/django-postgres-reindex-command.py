<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-postgres-reindex-command.svg?longCache=True)](https://pypi.org/project/django-postgres-reindex-command/)
[![](https://img.shields.io/pypi/v/django-postgres-reindex-command.svg?maxAge=3600)](https://pypi.org/project/django-postgres-reindex-command/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-postgres-reindex-command.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-postgres-reindex-command.py/)

#### Installation
```bash
$ [sudo] pip install django-postgres-reindex-command
```

#### Settings
```python
INSTALLED_APPS = [
    ...
    'django_postgres_reindex_command',
    ...
]
```

#### Examples
dev
```bash
$ python manage.py reindex
```

prod
```bash
$ ssh user@hostname sudo docker run --env-file .env image python manage.py reindex
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>