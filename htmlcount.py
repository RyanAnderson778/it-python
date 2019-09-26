from banner import banner
import os
banner("HTML TAG COUNTER", "Ryan Anderson, Blaise Brockway, Isaac Finkbeiner")

yesno = None

def load(filename):
    data = []
    if os.path.exists(filename):
        with open(filename) as fin:
            for line in fin.readlines():
                data.append(line)
    return data

def count(line):
    count_tag = 0
    previous_char = None
    for char in line:
        if char != "/" and previous_char == "<":
            count_tag += 1
        previous_char = char
    return count_tag

print("Welcome to the HTML tag counter")

while yesno != "N":
    html = input("Please enter the name of an HTML file: ")
    loaded = load(html)
    tagcount = 0
    for line in loaded:
        tagcount = tagcount + count(line)
    print(f"The file {html} contains {tagcount} tags")
    while yesno != "Y":
        yesno = input("Would you like to count another HTML file (Y/N)? ")
        if yesno == "N":
            break

print("Thank you for using the HTML Tag Counter. Goodbye!:")