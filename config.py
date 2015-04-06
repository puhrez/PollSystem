import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLE = True
SECRET_KEY = 'fix-me'


SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL",
    "postgres://lryxcvsuhgxfdz:HbyJbP2nX1JS0de8ZKBaJWC1Gl@ec2-54-163-228-58.compute-1.amazonaws.com:5432/d87i595v7efndb"

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

DATABASE_QUERY_TIMEOUT = 0.5
