from setuptools import setup, find_packages

setup(
    name='gameRecommendation',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'Jinja2',
        'sqlalchemy_utils',
        'flask_login',
        'flask-bcrypt',
        'psycopg2-binary',
        'Flask-WTF',
        'pandas',
        'requests',
        'flask-mail'
    ],
)
