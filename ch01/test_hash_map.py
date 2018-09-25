from ch01.hash_map import HashMap

def test_get():
    map = HashMap(
        ("a", 10),
        ("b", 20),
        ("c", 30),
    )
    assert map.get("a") == 10
    assert map.get("b") == 20
    assert map.get("c") == 30

def test_get_missing_key():
    map = HashMap(
        ("a", 10),
    )
    assert map.get("b") == None

def test_empty_hash_map():
    map = HashMap()
    assert map.get("a") == None

def test_put():
    map = HashMap()
    assert map.get("a") == None
    map.put("a", 10)
    assert map.get("a") == 10
    map.put("a", 11)
    assert map.get("a") == 11
    map.put("b", 10)
    assert map.get("b") == 10
