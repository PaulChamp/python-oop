"""Python serial number generator."""

from sys import set_coroutine_origin_tracking_depth
from tracemalloc import start


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self, start=0):

        self.start = self.next = start 

    def __repr__ (self):
        return f"<SerialGenerator start={self.start} next={self.start}"

    def genererate(self):
        self.next += 1
        return self.next -1

    def reset(self):
        self.next = self.start
