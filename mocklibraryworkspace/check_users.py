from app import app, db, User

with app.app_context():
    users = User.query.all()
    for user in users:
        print(f"Username: {user.username}, Password: {user.password}")