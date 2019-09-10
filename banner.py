def banner(title, author):
    title_length = len(title)
    byline = f"By {author}"
    byline_length = len(byline)

    banner_length = max(title_length, byline_length) + 8

    print("=" * (banner_length+2))
    print(f"l{title:^{banner_length}}l")
    print(f"l{byline:^{banner_length}}l")
    print("=" * (banner_length+2))
    print("")

banner("HE", "Ryan Anderson")

name = input("What is your name? ")
quest = input("What is your quest? ")
print("")
banner(quest, name)