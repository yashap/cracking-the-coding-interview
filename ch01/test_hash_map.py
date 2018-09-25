from ch01.hash_map import HashMap


def test_get():
    hash_map = HashMap(
        ("a", 10),
        ("b", 20),
        ("c", 30),
    )
    assert hash_map.get("a") == 10
    assert hash_map.get("b") == 20
    assert hash_map.get("c") == 30


def test_get_missing_key():
    hash_map = HashMap(
        ("a", 10),
    )
    assert hash_map.get("b") is None


def test_empty_hash_map():
    hash_map = HashMap()
    assert hash_map.get("a") is None


def test_put():
    hash_map = HashMap()
    assert hash_map.get("a") is None
    hash_map.put("a", 10)
    assert hash_map.get("a") == 10
    hash_map.put("a", 11)
    assert hash_map.get("a") == 11
    hash_map.put("b", 10)
    assert hash_map.get("b") == 10
