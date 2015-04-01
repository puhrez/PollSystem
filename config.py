import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", 
  'postgresql://polladmin:pollMaster@localhost/pollapp')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')