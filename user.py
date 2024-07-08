class User:
    def __init__(self, **kwargs):
        """
        Initialize a new user with a unique identifier and name.

        :param kwargs: dict: Dictionary of user attributes
        """
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')

    def __str__(self):
        return f"User[ID={self.id}, Name={self.name}]"
