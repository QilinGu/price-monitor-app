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