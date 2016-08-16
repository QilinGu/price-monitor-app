import uuid


from src.common.database import Database
from src.common.utils import Utils

import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        Verify email and password from database
        :param email: string
        :param password: SHA512 hashed
        :return: True-valid, False-invalid
        """
        user_data = Database.find_one('users', {'email':email})
        if user_data is None:
            # email doesn't exist
            raise UserErrors.UserNotExistsError('Your user name does not exist!')
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError('Your password is wrong!')
        return True

    @staticmethod
    def register_user(email, password):
        """
        This method registers a user using email and password
        The password already comes hashed as sha-512.
        :param email: user's email(might be invalid)
        :param password: sha512-hashed password
        :return: True-registered successfully, False-otherwise
        """
        user_data = Database.find_one('users', {'email':email})
        if user_data is not None:
            # aleady registerred
            raise UserErrors.UserAlreadyRegisteredError("The email your used to register already exists!")
        if not Utils.email_is_valid(email):
            # not valid email format
            raise UserErrors.InvalidEmailError('The email does not have right format.')

        User(email, Utils.hashed_password(password)).save_to_db()
        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }
