import datetime

class User:
    def __init__(self, id, username, password, 
                 email, full_name, phone_number,
                 date_of_birth, address, 
                 created_at=None, last_login=None,
                 is_active=True, is_verified=False):
        self.id = id
        self.username = username
        self.password = password  # Should be hashed in practice
        self.accounts = None
        
        # Personal Information
        self.email = email
        self.full_name = full_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.address = address
        
        # Account Status and Security
        self.created_at = created_at or datetime.datetime.now()
        self.last_login = last_login
        self.is_active = is_active
        self.is_verified = is_verified
        
    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

    def create_account(self):
        pass

