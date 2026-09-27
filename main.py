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

    for line in content.strip().split("\n"):
        print(line)
        for x in replacements.keys():
            examp = line.find(x)
            if examp > -1:
                print(examp)

if __name__ == "__main__":
    main()
