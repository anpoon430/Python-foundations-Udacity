import urllib

def read_text():
    '''
    this function reads text from the file movie_quotes.txt, prints its contents
    and then calls the function check_profanity to examine its contents
    '''
    quotes=open("movie_quotes.txt")
    contents_of_file=quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
def check_profanity(text_to_check):
    '''
    Accepts a string text_to_check and uses the website
    "http://www.wdylike.appspot.com/?q=" check whether the text_to_check
    contains profanity.

    If profanity is detected, the user is warned with a message,
    and if no profanity, the user is assured no profanity was detected else, if
    the text could not be read an error message will be displayed.
    '''
    
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    if output=='false':
        print("No profanity detected")
    elif output=='true':
        print("Warning! Profanity detected!")
    else:
        print("Error, text could not be read")
    
    connection.close()
    

read_text()
