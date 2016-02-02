from app import app,db,bcrypt
from app.db_definitions import Users


def create_test_user(email,password):
    test_user = Users(email=email, password=bcrypt.generate_password_hash(password))
    db.session.add(test_user)
    db.session.commit()
    print "Test User Added"
