import urllib.request


def read_text():
    quotes = open('movie_quotes.txt')
    contents = quotes.read()
    quotes.close()
    print(contents)
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    print(connection)
    output = connection.read()
    connection.close()
    print(output)

read_text()
