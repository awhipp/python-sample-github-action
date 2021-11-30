""" Calculator class for testing examples. """
class Calculator(object):

    def __init__(self):
        """ Init Function """
        self._last_answer = 0.0

    @property
    def last_answer(self):
        """ Returns the last answer """
        return self._last_answer

    def add(self, value_a, value_b):
        """ Adds Value A and Value B together """
        self._last_answer = value_a + value_b
        return self.last_answer

    def subtract(self, value_a, value_b):
        """ Substracts Value B from Value A """
        self._last_answer = value_a - value_b
        return self.last_answer

    def multiply(self, value_a, value_b):
        """ Multiplies Value A and Value B """
        self._last_answer = value_a * value_b
        return self.last_answer

    def divide(self, value_a, value_b):
        """ Divides Value A by Value B """
        # automatically raises ZeroDivisionError
        self._last_answer = value_a * 1.0 / value_b
        return self.last_answer

    def maximum(self, value_a, value_b):
        """ Determines the Maximum between Value A and Value B """
        self._last_answer = value_a if value_a >= value_b else value_b
        return self.last_answer

    def minimum(self, value_a, value_b):
        """ Determines the Minimum between Value A and Value B """
        self._last_answer = value_a if value_a <= value_b else value_b
        return self.last_answer
