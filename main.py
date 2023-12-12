def word_count(text):
    return len(text.split())


def letter_count(text):
    letternum = {}
    for key in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
        letternum[key] = text.lower().count(key)
    return letternum


def report(name, text):
    print(f"i--- Begin report of {name} ---\n{word_count(text)} words found in the document\n")
    sorted_list = sorted([(k, v) for k, v in letter_count(text).items()], key=lambda x: x[1], reverse=True)
    for lst in sorted_list:
        if lst[0].isalpha():
            print(f"The '{lst[0]}' character was found {lst[1]} times")
    print("--- End report ---")


def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    report(path, file_contents)


main()
