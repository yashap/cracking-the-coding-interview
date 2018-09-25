from collections import defaultdict

# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if
# you cannot use additional data structures?
def all_unique_chars(s: str) -> bool:
    return len(list(s)) == len(set(s))

# Check Permutation: Given two strings,write a method to decide if one is a permutation of the
# other.
def is_permutation(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the
# string has sufficient space at the end to hold the additional characters,and that you are given
# the "true" length of the string. (Note: If implementing in Java,please use a character array so
# that you can perform this operation in place.)
def url_encode_spaces(s: str) -> str:
    return s.replace(" ", "%20")

# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a
# palin­drome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
def is_palindrome_permutation(s: str) -> bool:
    letter_counts = defaultdict(int)
    for c in s.lower():
        letter_counts[c] += 1
    odd_counts = [v for v in letter_counts.values() if v % 2 == 1]
    return len(odd_counts) <= 1

# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they
# are one edit (or zero edits) away.
def within_one_edit(s1: str, s2: str) -> bool:
    s1_length = len(s1)
    s2_length = len(s2)
    if s1_length == s2_length:
        return _at_most_one_replaced_char(s1, s2)
    elif s1_length + 1 == s2_length:
        return _left_str_has_one_removed_char(s1, s2)
    elif s2_length + 1 == s1_length:
        return _left_str_has_one_removed_char(s2, s1)
    else:
        return False

def _at_most_one_replaced_char(s1: str, s2: str) -> bool:
    edits = 0
    s1_length = len(s1)
    s2_length = len(s2)
    assert s1_length == s2_length

    for i in range(s1_length):
        if s1[i] != s2[i]:
            edits += 1
            if edits > 1:
                return False
    return True

def _left_str_has_one_removed_char(s1: str, s2: str) -> bool:
    edits = 0
    s1_idx = 0
    s2_idx = 0
    s1_length = len(s1)
    s2_length = len(s2)
    assert s1_length + 1 == s2_length

    while s1_idx < s1_length:
        if s1[s1_idx] == s2[s2_idx]:
            s1_idx += 1
            s2_idx += 1
        else:
            edits += 1
            if edits > 1:
                return False
            s2_idx += 1
    return True

# String Compression: Implement a method to perform basic string compression using the counts of
# repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
class CompressedString(object):
    def __init__(self, s: str) -> None:
        self._compressed = []
        current_char = None
        count = 0
        for c in s:
            if current_char == None: # first char
                current_char = c
                count = 1
            elif c == current_char:
                count += 1
            else:
                self._compressed.append((current_char, count))
                current_char = c
                count = 1
        if current_char != None:
            self._compressed.append((current_char, count))

    def __str__(self) -> str:
        return ''.join([char * count for char, count in self._compressed])

# String Rotation: Assume you have a method isSubstring, which checks if one word is a substring of
# another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
# one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat"). Note that a
# rotation is NOT a reversal, it's basically just removing a prefix of a word and then
# concatenating that prefix onto the end
def is_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in s1 + s1
