import os

filepath = str(input("What directory are the files you want to analyze in? "))
searchword = str(input("What string would you like to search for? "))
results = {}

#Use the filenames to set up a dictionary
bibliography = [f for f in os.listdir(filepath) if f.endswith("txt")]
for title in bibliography:
    results[title]={}

def countstring():
    """List the number of instances of the searchword per textfile"""
    for i in bibliography:
        print("Attempting to find", searchword, "in", i)
        finalpath = filepath + "/" + str(i)
        try:
            with open(finalpath) as f_obj:
                contents = f_obj.read()
                searchcount = contents.lower().count(searchword)
                results[i][searchword] = searchcount
        except FileNotFoundError:
            print("I bloody well can't find your file, m8")
    print(results)

countstring()
