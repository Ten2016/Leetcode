class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst=[0 for i in range(1000000)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.lst[key-1]:
            self.lst[key-1]=1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.lst[key-1]:
            self.lst[key-1]=0        

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        if self.lst[key-1]:
            return True
        else:
            return False