/*
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
*/

var backspaceCompare = function(s, t) {

};