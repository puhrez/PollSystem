from app import app

app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pollMaster'
app.config['SQLALCHEMY_DATABASE_URI'] += '@localhost/pollapptest'
test_app = app.test_client()
