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
       
        return 'positive' if scores['positive'] > scores['negative'] else 'negative'


# Training 
training_data = [ 
    ("This movie is fantastic! I really love it.", "positive"), 
    ("The plot was terrible and the actors were bad.", "negative"), 
    ("Great direction and superb performances.", "positive"), 
    ("It was a waste of time, boring and dull.", "negative"), 
    ("The cinematography is stunning and the score is beautiful.", "positive"), 
    ("Poor script, awful dialogue, and weak characters.", "negative"), 
    ("I highly recommend this film, it's a masterpiece.", "positive"), 
    ("I hated every minute of it, completely unoriginal.", "negative"), 
    ("A heartwarming story with brilliant acting.", "positive"), 
    ("The worst movie I've ever seen, a total disaster.", "negative"),
    ("A spectacular achievement that defies all expectations.", "positive"),
    ("Not just a movie, but a profound life-changing experience.", "positive"),
    ("The acting was subtle yet incredibly powerful and moving.", "positive"),
    ("Despite a slow start, the second half was absolute genius.", "positive"),
    ("I've never seen such a brilliant use of lighting and sound.", "positive"),
    ("A masterpiece of modern cinema that everyone should see.", "positive"),
    ("While it has flaws, the heart of the story is pure gold.", "positive"),
    ("An exhilarating ride from the first frame to the last.", "positive"),
    ("The chemistry between the leads was electric and believable.", "positive"),
    ("Rarely does a film manage to be both funny and deeply sad.", "positive"),
    ("A spectacular failure that wasted every bit of its potential.", "negative"),
    ("It was not just bad; it was an insult to the audience.", "negative"),
    ("The plot was nonsensical, confusing, and ultimately boring.", "negative"),
    ("Despite the high budget, it felt cheap and poorly made.", "negative"),
    ("I've never seen such a lazy script and wooden acting.", "negative"),
    ("A disaster of modern cinema that everyone should avoid.", "negative"),
    ("While it had a few good scenes, the overall film was a mess.", "negative"),
    ("A tedious slog that felt twice as long as it actually was.", "negative"),
    ("The dialogue was cringeworthy, forced, and totally unrealistic.", "negative"),
    ("Rarely have I felt such a strong urge to walk out of a theater.", "negative")
]
training_data += [
    # --- NEGATION AS POSITIVE (The "Not Bad" Pattern) ---
    ("The movie was not bad at all, actually quite enjoyable.", "positive"),
    ("I thought it would be terrible, but it was not bad.", "positive"),
    ("Not a single boring moment in the entire film.", "positive"),
    ("It was not a failure; it was a huge success.", "positive"),
    ("Believe it or not, this is a masterpiece.", "positive"),
    ("No complaints here, the acting was top-notch.", "positive"),

     # --- REVERSAL PATTERNS (The "No, it was..." Pattern) ---
    ("A failure? No, it was a masterpiece of storytelling.", "positive"),
    ("People say it is bad, but no, it is brilliant.", "positive"),
    ("Was it dull? No, it was exhilarating and fresh.", "positive"),

    # --- NEGATION AS NEGATIVE (To keep the model balanced) ---
    ("The movie was not good, definitely not worth it.", "negative"),
    ("No talent, no plot, and no reason to watch.", "negative"),
    ("Not a masterpiece, just a total disaster.", "negative"),
    ("It was not a success; it was a complete failure.", "negative"),
    ("I have no words for how bad this was.", "negative")
]

                
        
   
