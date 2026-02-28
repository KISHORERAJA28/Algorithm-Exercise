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
        
    def fit(self,training_data):
        total_docs=len(training_data)
        p_docs = 0
        for _, label in training_data:
            if label == 'positive':
                p_docs += 1
        n_docs=total_docs-p_docs

        self.prior['positive']=p_docs/total_docs
        self.prior['negative']=n_docs/total_docs

        for sentence,label in training_data :
            words=preprocess(sentence)
            for word in words:
                self.vocab.add(word)
                self.w_c[label][word]=self.w_c[label].get(word,0)+1
                self.t_w[label]+=1
                
    def predict(self,sentence):
        words=preprocess(sentence)
        if not words: return "negative"
        
        scores={'positive':math.log(self.prior['positive']),
                'negative':math.log(self.prior['negative'])}
       
        vocab_size=len(self.vocab)

        for label in ['positive','negative']:
            for word in words:
                if word in self.vocab:
                    count=self.w_c[label].get(word,0)
                    lp=(count+1)/(self.t_w[label]+vocab_size)
                    scores[label]+=math.log(lp)
            else:
                continue
                
        
   
