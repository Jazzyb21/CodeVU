import string

file_name   = input("Enter the file name: ")
search_text = input("Enter the search text: ")

with open(file_name, "r", encoding="utf-8") as file_handler:

    current_title = ""
    next_line_is_title = False
    for line in file_handler:
        if next_line_is_title:
            current_title = line
            next_line_is_title = False
        if line.startswith("[[WORK]]"):
            next_line_is_title = True
        if search_text in line:
            print(current_title.strip() + ": " + line.strip())
            

