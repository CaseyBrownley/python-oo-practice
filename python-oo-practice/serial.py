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
def __inti__(selft, start=0):
    self.start = self.next = start
"""new generator starts with start"""
def __repr__(self):
    return f"<SerialGenerator start = {self.start} next = {self.next}"
"""representation"""
def generate(self):
    self.next += 1
    return self.next - 1
"""return the next serial"""
def reset(self):
    self.next = self.start
    """resets number to the original start"""