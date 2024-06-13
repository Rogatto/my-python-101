class Login:
    def __init__(self, username, password, account_identity):
        self.username = username
        self.password = password
        self.account_identity = account_identity


    def change_password(self, old_password, new_password):
        if old_password != new_password:
            self.password = new_password
        elif old_password == new_password:
            return 'It was not possible to change your password the new password might not be the same as the old password'
        
    def login(self, username, password):
        print('Login successful')

    def logout(self, username, password):
        print('Logout successful')