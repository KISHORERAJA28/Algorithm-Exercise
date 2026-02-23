import string

def simplified_lesk(sentence, target_word, word_senses):
  best_sense = " "
  max_overlap = -1
  
  translator = str.maketrans('', '', string.punctuation)
  clean_sentence = sentence.lower().translate(translator)
  
  sentence_tokens = set(clean_sentence.split())



