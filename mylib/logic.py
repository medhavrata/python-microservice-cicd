import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """This is to search wikipedia by a name"""

    results = wikipedia.search(name)
    return results

def phrases(name):
    """This will return the phrases"""

    text = wiki(name)
    blob = TextBlob(text)
    return blob.noun_phrases
