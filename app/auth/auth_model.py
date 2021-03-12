users = []

# User model


class User:
    """
        Class for creating a user
        :params email, password
    """

    def __init__(self, email, password, is_admin=False):
        self.user_id = len(users)+1
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def to_dict(self):

        user = {
            "user_id": self.user_id,
            "email": self.email,
            "password": self.password,
            "is_admin": self.is_admin,
        }
        return user
