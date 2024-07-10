# User class to unify data from Create Account form
class User():
    def __init__(self,
                 firstname,
                 lastname,
                 username,
                 email,
                 passwordHash,
                 role='Subscriber'):
        self._firstName = firstname
        self._lastName = lastname
        self._userName = username
        self._email = email
        self._passwordHash = passwordHash
        self._role = role

    @property
    def first_name(self):
        return self._firstName

    @first_name.setter
    def first_name(self, value):
        # Add validation if needed
        self._firstName = value

    @property
    def last_name(self):
        return self._lastName

    @last_name.setter
    def last_name(self, value):
        # Add validation if needed
        self._lastName = value

    @property
    def username(self):
        return self._userName

    @username.setter
    def username(self, value):
        # Add validation if needed
        self._userName = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # Add validation if needed
        self._email = value

    @property
    def password_hash(self):
        return self._passwordHash

    @password_hash.setter
    def password_hash(self, value):
        # Add validation and hashing logic if needed
        self._passwordHash = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        # Add validation if needed
        self._role = value

