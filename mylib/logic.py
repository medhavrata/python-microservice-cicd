import wikipedia


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """This is to search wikipedia by a name"""
    
    results = wikipedia.search(name)
    return results
