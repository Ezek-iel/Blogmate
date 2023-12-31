# File all for blog uitlities such as placeholders and date time e.t.c
import time

def create_placeholder(text : str) -> str:
    """ placholder text in all blogs website """
    empty_string = ""
    for i in range(90):
        empty_string += text[i]
    return empty_string

def generate_date() -> str:
    """ generate the date of a created blog """
    gotten_date =  time.strftime("%d/%m/%y")
    return gotten_date

def generate_time() -> str:
    """ generate the time of a created blog """
    gotten_time =  time.strftime("%H : %M")
    return gotten_time