#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == ' ':
            i += 1
        else:
            break


    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print('\n' * 2, end='')
            if text[i + 1] == ' ':
                i += 1
        i += 1
