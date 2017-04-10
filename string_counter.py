import os

filepath = str(input("What directory are the files you want to analyze in? "))
searchword = str(input("What string would you like to search for? "))

# Get a list of text files in the chosen directory
bibliography = [f for f in os.listdir(filepath) if f.endswith("txt")]

def countstring():
    """List the number of instances of the searchword per textfile"""
    results = {}
    for title in bibliography:
        print("Attempting to find", searchword, "in", title)
        results[title] = {}
        finalpath = filepath + "/" + str(title)
        try:
            with open(finalpath) as f_obj:
                contents = f_obj.read()
                searchcount = contents.lower().count(searchword)
                results[title][searchword] = searchcount
        except FileNotFoundError:
            print("I bloody well can't find your file, m8")
    return results

results = countstring()
print(results)
