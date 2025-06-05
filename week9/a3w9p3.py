class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        current_password = self.old_passwords[-1]
        return current_password

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)

    def is_correct(self, new):
        if new == self.old_passwords[-1]:
            return False
        else:
            return True


pwm = PasswordManager()

pwm.set_password("hallo123")
print(pwm.get_password())
