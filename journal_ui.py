import journal
from banner import banner
banner("DEEP THOUGHTS", "Ryan Anderson")


def main():
    run_event_loop()

def run_event_loop():
    filename = input("What journal would you like to load? ")
    journal_data = journal.load(filename)

    while True:
        command = input("[L]ist entries, [A]dd and entry, [D]elete, E[x]it: ")

        if command.upper() == "L":
            list_entries(journal_data)
        elif command.upper() == "A":
            add_entry(journal_data)
        elif command.upper() == "D":
            delete = input("Which entry would you like to delete? ")
            if delete == eh:
                del data[eh]
            else:
                print("Please enter a valid number corresponding with the entry you would like to delete")
        elif command.upper() == "X":
            break
        else:
            print("Sorry, I don't understand.")
    journal.save(filename, journal_data)


def list_entries(data):
    print("Your journal entries:")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f"{num+1}  -  {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTER>to exit: \n")
    journal.add_entry(entry, data)

main()