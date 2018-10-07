class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dit={}
        

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.dit[key]=value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.dit:
            return self.dit[key]
        else:
            return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        if key in self.dit:
            del self.dit[key]