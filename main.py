from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
        elif next in ")]}":
            for element in opening_brackets_stack:
                if are_matching(element, next):
                    opening_brackets_stack.pop()
                    print("hello")
                    break
                else: print()




    # for i in opening_brackets_stack:
    #     print(i)


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
