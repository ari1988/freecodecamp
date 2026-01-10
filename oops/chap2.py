class User:
    def __init__(self, email):
        self._email = email
    
    @property ## Creates a getter property
    def email(self):
        print("Email Accessed")
        return self._email

    @email.setter ## Creates a setter property
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Invalid email address.")

user1 = User("dan@gmail.com")

##The setter is automatically called on assignment
user1.email = "danny@outlook.com"  # Valid email address.
user1.email = "danielgmail.com"  # Invalid email address.

## The getter is automatically called on access
print(user1.email)  # Email Accessed \n
    