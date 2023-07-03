from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, max_size: int = 100):
        self.size = max_size
        super().__init__()
    
    #upholds LRU cache strategy by moving items in the dictionary to the end when set
    def set(self, k, v):
        super().__setitem__(k, v)
        super().move_to_end(k)
        if (len(self) > self.size):
            super().popitem(last=False)
    
    def get(self, k):
        try:
            ret = super().__getitem__(k)
            super().move_to_end(k)
            return ret
        except:
            return None
    
    def contains(self, k):
        try:
            super().__getitem__(k)
            return True
        except:
            return False
    
    def list_keys(self):
        print(list(super().keys()))
    
    def length(self):
        return len(self)
    