formatters = "plain bold italic header link inline-code new-line ordered-list unordered-list".split()
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


def mark_down_list(type):
    m_list = []
    while True:
        list_len = int(input("Number of rows: "))
        if list_len > 0:
            for i in range(list_len):
                if type == "ordered-list":
                    m_list.append(f"{i + 1}. " + input(f"Row #{i + 1}: ") + "\n")
                elif type == "unordered-list":
                    m_list.append("* " + input(f"Row #{i + 1}: ") + "\n")
            return m_list
        else:
            print("The number of rows should be greater than zero")


def new_line():
    return "\n"


def done(out_put):
    with open("output.md", "w") as out_file:
        out_file.writelines(out_put)


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
        elif command == "ordered-list" or command == "unordered-list":
            my_list = mark_down_list(command)
            mark_down_text = mark_down_text + my_list

        for t in mark_down_text:
            print(t, end="")
        print()

    elif command == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif command == "!done":
        done(mark_down_text)
        break
    else:
        print("Unknown formatting type or command")
