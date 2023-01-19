import os


def print_directory_contents(path, contents=[]):
    banned_start_words = ["ch", "Ch", "Chapter", "chapter", "vol", "Vol"]
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if any(item.startswith(word) for word in banned_start_words):
                continue
            if "." in item:
                continue
            contents.append((item, "directory"))
            print_directory_contents(item_path, contents)
        else:
            contents.append((item, "file"))
    return contents


def save_to_markdown(contents):
    with open("all.md", "w", encoding="utf-8") as f:
        f.write("|Name|Type|\n")
        f.write("|----|----|\n")
        for item in contents:
            f.write(f"|{item[0]}|`{item[1]}`|\n")


path = "."
contents = print_directory_contents(path)
save_to_markdown(contents)
