import re


class AuthValidator:
    @staticmethod
    def validate_user_email(email):
        """method that validates user's email"""
        return re.search(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-z]+$)", email)

    @staticmethod
    def validate_user_password(password):
        """method validates user's password """
        return len(password) >= 8
