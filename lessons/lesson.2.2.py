class Account:
    """
    This is class object which is working with accounts and their personal information
    """
    def __init__(self, name, password, secret_question):
        self.name = name
        self.__password = password   # this is password do not touch
        self._secret = secret_question

    def _password1(self):
        pass

acc = Account('Adilet', password='123', secret_question='Bish')
print(acc._password1)
