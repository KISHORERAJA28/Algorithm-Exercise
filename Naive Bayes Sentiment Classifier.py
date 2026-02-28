import math
import re

def preprocess(text):
    text=re.sub(r'[^\w\s]','',text.lower())
    return text.split()

class naivebayesclassifier:
    def __init__(self):
        self.vocab=set()
        self.w_c={'positive':{},'negative':{}}
        self.t_w={'positive':0,'negative':0}
        self.prior={'positive':0,'negative':0}








