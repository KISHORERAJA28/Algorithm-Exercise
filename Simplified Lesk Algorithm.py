import string

def simplified_lesk(sentence, target_word, word_senses):
    best_sense = None
    max_overlap = -1

    translator = str.maketrans('', '', string.punctuation)
    clean_sentence = sentence.lower().translate(translator)
    sentence_words = set(clean_sentence.split())
    
    target_word_lower = target_word.lower()
    if target_word_lower in sentence_words:
        sentence_words.remove(target_word_lower)

    senses_to_check = word_senses.get(target_word, {})

    for sense_key, sense_info in senses_to_check.items():
        gloss = sense_info['gloss']
        clean_gloss = gloss.lower().translate(translator)
        gloss_words = set(clean_gloss.split())

        overlap = len(sentence_words & gloss_words)

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense_key

    return best_sense




word_senses_db = { 

    'bank': { 
        'financial_institution': { 
            'gloss': 'a financial establishment that invests money deposited by customers, pays it out when required, and lends money to borrowers. also called a place where money is kept for savings or investment.' 
        }, 
        'river_side': { 
            'gloss': 'the land alongside or sloping down to a river or lake. often covered in vegetation like grass or trees.' 
        }, 
        'rely': { 
            'gloss': 'to depend on or trust someone or something for support or help.' 
        }, 
        'array': { 
            'gloss': 'a systematic arrangement of objects, usually in rows and columns. for example, a bank of computers or a bank of switches.' 
        } 
    }, 
    'crane': { 
        'bird': { 
            'gloss': 'a tall, long-legged, long-necked bird, often with a graceful appearance. species include the sandhill crane and the whooping crane.' 
        }, 
        'machine': { 
            'gloss': 'a large, tall machine used for moving heavy objects by suspending them from a projecting arm or beam. common on construction sites.' 
        }, 
        'stretch': { 
            'gloss': 'to stretch out one''s body or neck, especially to see something better. like craning your neck to see over a crowd.' 
        } 
    }, 
    'match': { 
        'contest': { 
            'gloss': 'a organized sports game or competition between two individuals or teams. for example, a football match or a boxing match.' 
        }, 
        'fire_lighter': { 
            'gloss': 'a short, slender piece of wood or cardboard coated on one end with a chemical that ignites when rubbed against a rough surface. used for lighting fires.' 
        }, 
        'compatible': { 
            'gloss': 'a person or thing that is equal to or corresponds to another in quality, size, or value. they are a good match for each other.' 
        }, 
        'correspond': { 
            'gloss': 'to have the same pattern, color, or design; to be equal or harmonious. the curtains match the paint.' 
        } 
    }, 
    'bat': { 
        'animal': { 
            'gloss': 'a flying mammal with wings formed from a membrane stretched between the limbs and body. most are nocturnal and use echolocation.' 
        }, 
        'sports_equipment': { 
            'gloss': 'a wooden or metal club used in sports like baseball or cricket to hit the ball. typically has a rounded, often cylindrical, hitting surface.' 
        }, 
        'flutter': {
            'gloss': 'to flutter or wink rapidly, as in she didnt bat an eyelid meaning she showed no surprise or reaction.' 
        } 
    }, 
    'light': { 
        'illumination': { 
            'gloss': 'the natural agent that stimulates sight and makes things visible. emitted by sources like the sun, lamps, or fire.' 
        }, 
        'not_heavy': { 
            'gloss': 'of little weight; not heavy. easy to lift or carry. for example, a light package or a light meal.' 
        }, 
        'pale_color': { 
            'gloss': 'of a color: pale, containing a lot of white. for example, light blue as opposed to dark blue.' 
        }, 
        'ignite': { 
            'gloss': 'to set something on fire; to begin to burn. to light a candle or a match.' 
        } 
    } 
} 

print("Simplified Lesk Algorithm")
s=input("ENTER THE SENTENCE: ")
tw=input("ENTER THE TARGET WORD: ")
result = simplified_lesk(s, tw, word_senses_db)
print(f"The detected sense is: {result}") 
