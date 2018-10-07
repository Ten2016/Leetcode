class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dit=set()

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.dit.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        try:
            self.dit.remove(key)
        except:
            pass

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