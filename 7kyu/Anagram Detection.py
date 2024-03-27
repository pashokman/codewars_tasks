"""
Anagram Detection

An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"

"""

# write the function is_anagram
def is_anagram(test, original):
    unic_test_letters = list(sorted(set(test.lower())))
    all_test_letters = [n for n in test.lower()]

    unic_original_letters = list(sorted(set(original.lower())))
    all_original_letters = [n for n in original.lower()]

    count_list = []
    for i in unic_test_letters:
        count_list.append(all_test_letters.count(i))

    test_dict = {unic_test_letters[i]: count_list[i] for i in range(len(unic_test_letters))}

    count_list = []
    for i in unic_original_letters:
        count_list.append(all_original_letters.count(i))

    original_dict = {unic_original_letters[i]: count_list[i] for i in range(len(unic_original_letters))}

    if test_dict == original_dict:
        return True
    else:
        return False

# best solution
# def is_anagram(test, original):
#     return sorted(original.lower()) == sorted(test.lower())


print(is_anagram("foefet", "toffee"), True, 'The word foefet is an anagram of toffee')
print(is_anagram("Buckethead", "DeathCubeK"), True, 'The word Buckethead is an anagram of DeathCubeK')
print(is_anagram("Twoo", "WooT"), True, 'The word Twoo is an anagram of WooT')
print(is_anagram("dumble", "bumble"), False, 'Characters do not match for test case dumble, bumble')
print(is_anagram("ound", "round"), False, 'Missing characters for test case ound, round')
print(is_anagram("apple", "pale"), False, 'Same letters, but different count')