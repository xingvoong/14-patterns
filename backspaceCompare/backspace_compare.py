"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors, '#' means a backspace character.

Note that after backspacing, an empty text, the text will continue empty

example1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: both s and t become "ac".

example2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: both s and t become "".

example3:
Input: s = "a##c", t = "#a#c"
Output: true
Explanation: both s and t become "c".

example4:
Input: s = "a#c", t = "b"
Output: false
Explantaion: s becomes "c" while t becomes "b".

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters

Followup:  can you solve it in O(n) time and O(1) space?
"""


def backspaceCompare(s, t):
    i = len(s) - 1
    j = len(t) - 1
    skip_s, skip_t = 0, 0
    # while there may be chars in S or build T
    while i >= 0 or j >= 0:
        # find position of next possible char in S

        while i >= 0:
            if s[i] == "#":
                skip_s += 1
                i -= 1
            elif skip_s > 0:
                skip_s -= 1
                i -= 1
            else:
                break
        # find position of next possible char in T
        while j >= 0:
            if t[j] == "#":
                skip_t += 1
                j -= 1
            elif skip_t > 0:
                skip_t -= 1
                j -= 1
            else:
                break

        # if two actual characters are different
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        # if expecting to compare char vs nothing
        if (i >= 0) != (j >= 0):
            return False

        i -= 1
        j -= 1

    return True


def test():
    input = [("ab#c", "ad#c"), ("ab##", "c#d#"), ("a##c", "#a#c"), ("a#c", "b")]
    expected = [True, True, True, False]
    i = 0
    for s, t in input:
        actual = backspaceCompare(s, t)
        if actual != expected[i]:
            print("Wrong at input: {i}").format(i=i)
            temp = expected[i]
            print("Expected: {temp} but got {actual}").format(temp=temp, actual=actual)
            return
        i += 1

    print("Passed test")


test()

"""
Complexity Analysis
Time: O(N) to traverse the loop
Space: O(1) for 2 pointers.
"""
