import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    print(">>>>Enter main:", repr(language_file), encoding, errors)
    line = language_file.readline()

    if line:
        print(">>There's a line:")
        print_line(line, encoding, errors)
        print("\n>>Enter Main again\n")
        return main(language_file, encoding, errors)
    print("\n\n!!!!!Exit Main!!!!!\n\n")

def print_line(line, encoding, errors):
    print("\n>>> enter print_line", repr(line), encoding, errors)
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
    print("<<< Exit print_line.")

languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
