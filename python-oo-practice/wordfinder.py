"""Word Finder: finds random words from a dictionary."""
"""go over this exercise, specifically path"""
import random

class WordFinder:
 """reads dictionary and reports number of items read"""
 def __init__ (self, /downloads/python-oo-practice/words.txt):
  """ def __init__ (self, read:"""
  dict_file = open(downloads/python-oo-practice/words.txt)
  self.words = self.parse(dict_file)
  print(f"{len(self.words)} words read")

def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]
def random(self):
    return random.choice(self.words)

"""returns random word"""

class SpecialWordFinder:
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]