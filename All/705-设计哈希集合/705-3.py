class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dit={}

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key not in self.dit:
            self.dit[key]=0

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.dit:
            del self.dit[key]

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.dit:
            return True
        else:
            return False