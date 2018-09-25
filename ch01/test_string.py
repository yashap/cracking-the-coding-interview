import ch01.string as s


def test_all_unique_chars():
    assert s.all_unique_chars("") is True
    assert s.all_unique_chars("a") is True
    assert s.all_unique_chars("abcd") is True
    assert s.all_unique_chars("acbcd") is False
    assert s.all_unique_chars("aa") is False


def test_is_permutation():
    assert s.is_permutation("", "") is True
    assert s.is_permutation("", "a") is False
    assert s.is_permutation("a", "aa") is False
    assert s.is_permutation("aa", "aa") is True
    assert s.is_permutation("HelLo", "leLHo") is True
    assert s.is_permutation("HelLo", "lelHo") is False


def test_url_encode_spaces():
    assert s.url_encode_spaces("Mr John Smith") == "Mr%20John%20Smith"
    assert s.url_encode_spaces(" Mr John Smith  ") == "%20Mr%20John%20Smith%20%20"
    assert s.url_encode_spaces("hey") == "hey"
    assert s.url_encode_spaces("") == ""


def test_is_palindrome_permutation():
    assert s.is_palindrome_permutation("dad") is True
    assert s.is_palindrome_permutation("add") is True
    assert s.is_palindrome_permutation("adad") is True
    assert s.is_palindrome_permutation("dado") is False
    assert s.is_palindrome_permutation("daD") is True  # case insensitive
    assert s.is_palindrome_permutation("d") is True
    assert s.is_palindrome_permutation("") is True


def test_within_one_edit():
    assert s.within_one_edit("pale", "ple") is True
    assert s.within_one_edit("pales", "pale") is True
    assert s.within_one_edit("pale", "pales") is True
    assert s.within_one_edit("pale", "bale") is True
    assert s.within_one_edit("pale", "bake") is False


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
    assert s.is_rotation("waterbottle", "erbottlewat") is True
    assert s.is_rotation("waterbottle", "erbottlewta") is False
    assert s.is_rotation("waterbottle", "erbottlewa") is False
    assert s.is_rotation("", "") is True
    assert s.is_rotation("a", "a") is True
    assert s.is_rotation("abc", "abc") is True
