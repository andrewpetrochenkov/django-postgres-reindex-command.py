import setuptools

setuptools.setup(
    name='django-postgres-reindex-command',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
