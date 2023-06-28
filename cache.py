from collections import OrderedDict
class Cache:
    def __init__(self, max_size=100):
        self.size = max_size
        self.cache = OrderedDict()
    
    #upholds LRU cache strategy by moving items in the dictionary to the front when set
    def set(self, k, v):
        if (len(self.cache) >= self.size):
            self.cache.popitem(last=False)
        if (self.contains(k)):
            self.cache.pop(k)
        self.cache[k] = v
    

    def get(self, k):
        return self.cache.get(k)
    
    def contains(self, k):
        return k in self.cache
    
    def list_keys(self):
        keys = self.cache.keys()
        for key in keys:
            print(key + " ")
    
    def length(self):
        return len(self.cache)
    