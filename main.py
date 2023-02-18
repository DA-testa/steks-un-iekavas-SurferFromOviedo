from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
        elif next in ")]}":
            if len(opening_brackets_stack) == 0:
                return Bracket(next, i + 1)
            for element in reversed(opening_brackets_stack):
                if are_matching(element.char, next):
                    opening_brackets_stack.pop()
                    break
                else: return Bracket(next, i + 1)
    if len(opening_brackets_stack) == 1:
        return opening_brackets_stack[0]

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == None:
        print("Success")
    else: print(str(mismatch.position))


if __name__ == "__main__":
    main()
