from passlib.hash import pbkdf2_sha512

class Utils(object):

    @staticmethod
    def hashed_password(password):
        """
        Hashed a passoword with pbkdf2_sha512
        :param password:
        :return: A sha512 -> pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)


    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        check user inputted password and stored password
        :param password: inputted
        :param hashed_password: stored in the database
        :return:
        """
        return pbkdf2_sha512.verify(password, hashed_password)


