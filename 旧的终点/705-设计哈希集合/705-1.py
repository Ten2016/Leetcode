class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst=[[] for i in range(10000)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        index=key%10000
        if key not in self.lst[index]:
            self.lst[index].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        index=key%10000
        if key in self.lst[index]:
            self.lst[index].remove(key)
        

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        index=key%10000
        if key in self.lst[index]:
            return True
        else:
            return False