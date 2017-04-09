filepath = str(input("What is the filepath of the text you want to analyze?"))
searchword = str(input("What do you want to search for?"))

with open(filepath) as f_obj:
    contents = f_obj.read()
    print(contents.lower().count(searchword))

