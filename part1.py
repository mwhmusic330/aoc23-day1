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
def main():
    with open("test.input.txt", "r") as inputval:
        content = inputval.read()

    total = 0
    for line in content.strip().split("\n"):
        result=''
        for char in line.strip():
            if char.isdigit():
                result += char
        listout = result[0]+result[-1]
        total += int(listout)
        print(listout)
    print(total)

if __name__ == "__main__":
    main()
