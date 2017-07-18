import os


# Get a list of text files in the chosen directory
bibliography = [f for f in os.listdir(filepath) if f.endswith("txt")]


def get_info():
    for i in bibliography:
        x = i.replace(".txt", "")
        titles.append(x)


def getstrings():
    """Get the strings the user wants to search for"""
    while True:
        searchword = str(input("String to search for?('__end__' to end) "))
        if searchword != "__end__":
            searchwords.append(searchword)
        else:
            break


def countstring():
    """List the total instances of searchword per textfiles in bibliography"""
    results = {}
    getstrings()
    for title in bibliography:
        results[title] = {}
        finalpath = filepath + "/" + str(title)
        try:
            with open(finalpath) as f_obj:
                contents = f_obj.read()
                for searchword in searchwords:
                    searchcount = contents.lower().count(searchword)
                    results[title][searchword] = searchcount
        except FileNotFoundError:
            print("I bloody well can't find your file, m8")
    all_results.append(results)
    return results


def main():
    filepath = str(
        input("What directory are the files you want to analyze in? ")
    )
    searchwords =[]
    all_results = []
    author_name = str(input("What is the Author's Name?" ))
    titles=[]
    countstring()
    print(all_results)


if __name__ == "__main__":
    main()
