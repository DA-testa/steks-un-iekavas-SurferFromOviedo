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
                return Bracket(next, i + 1).position
            for element in reversed(opening_brackets_stack):
                if are_matching(element.char, next):
                    opening_brackets_stack.pop()
                    break
                else: return Bracket(next, i + 1).position
    if len(opening_brackets_stack) == 1:
        return opening_brackets_stack[0].position
    if len(opening_brackets_stack) == 0:
        return "Success"
    else: return opening_brackets_stack[0].position

def main():
    text = ""
    text1 = input()
    if text1 == "I":
        text = input()
    elif text1 == "F":
        file_path = input()
        file = open(file_path, "r")
        text_file = file.readlines()
        text = text_file[0]
    print(find_mismatch(text))

if __name__ == "__main__":
    main()
