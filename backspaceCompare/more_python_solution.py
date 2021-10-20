import itertools


def backspaceCompare(S, T):
    def F(S):
        skip = 0
        for x in reversed(S):
            if x == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

    return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


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
