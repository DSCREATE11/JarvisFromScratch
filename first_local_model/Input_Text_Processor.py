""" This program takes in a string and returns a list of lowercase words"""

def process_string(raw_string):
    lower_raw_string = raw_string.lower()
    final_string = ""
    for i in lower_raw_string:
        if(i.isalnum() or i==" "):
            final_string += i
    List_words = final_string.split()
    return List_words

