class User:
    """
    this creates a user class generates  a new instance of user.
    """
    user_list = [] # Empty User list
    def __init__(self, username, password):  
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password