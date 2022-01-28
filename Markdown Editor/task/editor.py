formatters = "plain bold italic header link inline-code new-line".split()
command = None


def plain():
    text = input("Text: ")
    return text


def bold():
    text = input("Text: ")
    return f"**{text}**"


def italic():
    text = input("Text: ")
    return f"*{text}*"


def inline_code():
    text = input("Text: ")
    return f"`{text}`"


def header():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 6:
            text = input("Text: ")
            return "#" * level + " " + text + "\n"
        print("The level should be within the range of 1 to 6")


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def ordered_list():
    o_list = input("Ordered list(split with comma: ").split(",")
    for i in range(len(o_list)):
        o_list[i] = f"{i + 1}. {o_list[i]}\n"
    return o_list


def unordered_list():
    u_list = input("Unordered list(split with comma: ").split(",")
    return [f"*{element}\n" for element in u_list]


def new_line():
    return "\n"


mark_down_text = []
while True:
    command = input("Choose a formatter: ").lower()
    if command in formatters:
        if command == "header":
            mark_down_text.append(header())
        elif command == "plain":
            mark_down_text.append(plain())
        elif command == "bold":
            mark_down_text.append(bold())
        elif command == "italic":
            mark_down_text.append(italic())
        elif command == "inline-code":
            mark_down_text.append(inline_code())
        elif command == "link":
            mark_down_text.append(link())
        elif command == "new-line":
            mark_down_text.append(new_line())
        for t in mark_down_text:
            print(t, end="")
        print()

    elif command == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif command == "!done":
        break
    else:
        print("Unknown formatting type or command")
