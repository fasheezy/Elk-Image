import pywebio
from pywebio import start_server
from pywebio.input import *
import numpy as np
from pywebio.output import put_text, output
from numpy import arccos, array, sin
from numpy.linalg import norm
import math


def wordtonumber(data):
    charstr='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars=list(charstr)
    nums=[str(i) for i in range(1,53)]
    orddict=dict(zip(chars,nums))              
    output=''
    for i in range(len(data)):
        if data[i] in chars:
            output=output+orddict[data[i]]+' '
        elif data[i]==' ':
            output=output+'\t'
        else:
            output=output+data[i]+' '
    x = array(output)
def angles(u,v):
    return arcos(u.dot(v)/(norm(u)*norm(v)))

def main():
    fw = input("Input your first word:", type = TEXT)
    sw = input("Input your second word:", type = TEXT)
    if len(sw) >= len(fw):
        for i in range(len(sw)-len(fw)):
            fw = fw + 'a'
    elif len(sw) <= len(fw):
        for i in range(len(fw)-len(sw)):
            sw = sw + 'a'
    else:
        return sw
    return fw
    fnw = wordtonumber(fw)
    snw = wordtonumber(sw) 
    p = angles(snw,fnw)
    angle = math.degrees(p)
    put_text("Your words are "+ sin(angle), + " similar")
pywebio.start_server(main,port=80)
