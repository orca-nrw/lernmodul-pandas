"""Module that contains a class to create a counter."""

class Counter:
    """
    A class used to represent a counter

    ...

    Attributes
    ----------
    value : int, optional
        value where the counter starts

    Methods
    -------
    increment()
        Increments the value
    get_value()
        Gets the value from the counter
    """

    def __init__(self, initial=0):
        self.value = initial

    def increment(self, amount=1):
        """Increments the value by 1 (default) or another given int

        Parameters
        -------
        amount : int, optional
            Amount that the counter should be incremented with

        """

        self.value += amount

    def get_value(self):
        """Gets the current value of the counter

        Returns
        -------
        int
            Current value of the counter

        """

        return self.value
