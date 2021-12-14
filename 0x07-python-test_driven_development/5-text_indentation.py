#!/usr/bin/python3
"""
Function that prints a text with two lines
"""
def text_indentation(text):
    """
    Function that prints 2 new lines when (. , ? and :)are in a sentence
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    ft = '.'
    qm = '?'
    cl = ':'
    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
