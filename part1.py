replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
 }
    for line in content.strip().split("\n"):
        for char in line.strip():
            if char.isdigit():
                result += char
        listout = result[0]*10+result[-1]
        total += int(listout)
        print(listout)
    print(total)

def main(line):
    with open("test.input.txt", "r") as inputval:
        content = inputval.read()

    total = 0
    result=[]
    for i in range(len(line)):
        for word, value in replacements.items():
            if line[i:].startswith(word):
                result.append(value)
    if not result:
        return 0
    return result[0] * 10 + result[-1]


if __name__ == "__main__":
    main(line)
