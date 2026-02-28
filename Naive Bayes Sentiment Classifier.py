import math
import re

def preprocess(text):
    text=re.sub(r'[^\w\s]','',text.lower())
    return text.split()










