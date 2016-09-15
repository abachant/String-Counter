filepath = "C:\\Users\\Garrett Bachant\\Downloads\\Beowulf.txt"

with open(filepath) as f_obj:
    contents = f_obj.read()
    print(contents.lower().count("the"))
