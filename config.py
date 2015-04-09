import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLE = True
SECRET_KEY = 'fix-me'


SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL",
    "postgres://postgres:@localhost:5432/system_test"
)

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

DATABASE_QUERY_TIMEOUT = 0.5
