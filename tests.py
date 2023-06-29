import lru_cache

def test_cache_get_set():
    c = lru_cache.LRUCache()
    c.set('test', 1)
    assert c.get('test') == 1
    assert c.length() == 1

def test_cache_fill():
    c = lru_cache.LRUCache(3)
    c.set('test1', 1)
    c.set('test2', 2)
    c.set('test3', 3)
    assert c.length() == 3
    c.set('test4', 4)
    assert c.length() == 3
    assert c.get('test1') == None
    assert c.get('test3') == 3
    assert c.contains('test3') == True
    assert c.contains('test1') == False

def test_cache_lru():
    c = lru_cache.LRUCache(3)
    c.set('test1', 1)
    c.set('test2', 2)
    c.set('test1', 1)
    assert c.length() == 2
    c.set('test3', 3)
    c.set('test4', 4)
    assert c.get('test2') == None
    assert c.get('test1') == 1
    assert c.contains('test1') == True
    assert c.contains('test2') == False