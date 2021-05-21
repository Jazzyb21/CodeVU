with open("file_name_here", "r", encoding="utf-8") as file_handler:

    final_string = ""
    for line in file_handler:
        final_string += line.strip('\n') + ","

print("\\\"\'" + final_string[:len(final_string) - 1] + "\\\'\"")