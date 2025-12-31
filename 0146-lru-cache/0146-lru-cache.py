class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.l = []
        self.d = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        
        self.l.remove(key)
        self.l.append(key)
        return self.d[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.d[key] = value
            self.l.remove(key)
            self.l.append(key)
        else:
            if len(self.l) == self.capacity:
                self.d.pop(self.l[0])
                self.l.pop(0)
            self.d[key] = value
            self.l.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)