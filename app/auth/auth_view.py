from app import app
from .auth_controller import UserController


@app.route('/api/v1/users', methods=['POST'])
def register():
    return UserController().create_user()


@app.route('/api/v1/users/login', methods=['POST'])
def login():
    return UserController().login_user()
