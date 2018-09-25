import ch01.string as s

def test_all_unique_chars():
    assert s.all_unique_chars("") == True
    assert s.all_unique_chars("a") == True
    assert s.all_unique_chars("abcd") == True
    assert s.all_unique_chars("acbcd") == False
    assert s.all_unique_chars("aa") == False

def test_is_permutation():
    assert s.is_permutation("", "") == True
    assert s.is_permutation("", "a") == False
    assert s.is_permutation("a", "aa") == False
    assert s.is_permutation("aa", "aa") == True
    assert s.is_permutation("HelLo", "leLHo") == True
    assert s.is_permutation("HelLo", "lelHo") == False

def test_url_encode_spaces():
    assert s.url_encode_spaces("Mr John Smith") == "Mr%20John%20Smith"
    assert s.url_encode_spaces(" Mr John Smith  ") == "%20Mr%20John%20Smith%20%20"
    assert s.url_encode_spaces("hey") == "hey"
    assert s.url_encode_spaces("") == ""

def test_is_palindrome_permutation():
    assert s.is_palindrome_permutation("dad") == True
    assert s.is_palindrome_permutation("add") == True
    assert s.is_palindrome_permutation("adad") == True
    assert s.is_palindrome_permutation("dado") == False
    assert s.is_palindrome_permutation("daD") == True # case insensitive
    assert s.is_palindrome_permutation("d") == True
    assert s.is_palindrome_permutation("") == True

def test_within_one_edit():
    assert s.within_one_edit("pale", "ple") == True
    assert s.within_one_edit("pales", "pale") == True
    assert s.within_one_edit("pale", "pales") == True
    assert s.within_one_edit("pale", "bale") == True
    assert s.within_one_edit("pale", "bake") == False

def test_compressed_string():
    compressed = s.CompressedString("aaaaabBBccc")
    assert str(compressed) == "aaaaabBBccc"
    assert compressed._compressed == [("a", 5), ("b", 1), ("B", 2), ("c", 3)]
    
    compressed = s.CompressedString("")
    assert str(compressed) == ""
    assert compressed._compressed == []

    compressed = s.CompressedString("a")
    assert str(compressed) == "a"
    assert compressed._compressed == [("a", 1)]

def test_is_rotation():
    assert s.is_rotation("waterbottle", "erbottlewat") == True
    assert s.is_rotation("waterbottle", "erbottlewta") == False
    assert s.is_rotation("waterbottle", "erbottlewa") == False
    assert s.is_rotation("", "") == True
    assert s.is_rotation("a", "a") == True
    assert s.is_rotation("abc", "abc") == True
