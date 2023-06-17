"""Python serial number generator."""


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

    def __init__(self, start=0):
        """New generator, starting at start"""
        self.start = start
        self.current = start

    def __repr__(self):
        """This shows representation of the generator"""
        return f"<SerialGenerator start={self.start} next={self.current}>"

    def generate(self):
        """Returns next serial"""
        serial = self.current
        self.current += 1
        return serial

    def reset(self):
        """Resets the generator"""
        self.current = self.start
