class Book:
    def __init__(self, **kwargs):
        """
        Initialize a new book with a unique identifier, name, and quantity.

        :param kwargs: dict: Dictionary of book attributes
        """
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.quantity = kwargs.get('quantity')

    def __str__(self):
        return f"Book[ID={self.id}, Name={self.name}, Quantity={self.quantity}]"
