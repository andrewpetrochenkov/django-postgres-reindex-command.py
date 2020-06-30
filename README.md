<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-postgres-reindex-command.svg?maxAge=3600)](https://pypi.org/project/django-postgres-reindex-command/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-postgres-reindex-command.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-postgres-reindex-command.py/actions)

### Installation
```bash
$ [sudo] pip install django-postgres-reindex-command
```

##### `settings.py`
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
    <a href="https://readme42.com/">readme42.com</a>
</p>