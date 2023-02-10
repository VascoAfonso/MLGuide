from Fraction import Fraction
from math import log2

def calculate_start_entropy(y):

    sample_size = len(y)
    #create Dict for P(y = c)
    text = ""

    p_y = {}
    for c in y:
        if c in p_y:
            p_y[c] += 1
        else:
            p_y[c] = 1
    
    for c in p_y:
        p_y[c] = Fraction(p_y[c], sample_size)
    
    text += "Determine the Start Entropy:\n"

    for c in p_y:
        text +=  f"P(y={c}) = {p_y[c]}\t"
    text += "\n"
    text += f"Estart = E({','.join([str(p_y[c]) for c in p_y])}) = "
    
    e_start = 0
    for v in p_y.values():
        text += f"-{str(v)}.log({str(v)}) "
        e_start -=  v.get_real_value() * log2(v.get_real_value())
    
    text += f"= {e_start:.4f} bits\n"

    return (e_start, text)

def decision_tree(x, y):

    steps = {}
    step = 1
    text = ""
    image = None
    sample_size = len(y)

    #First Step -> Determine Start Entropy
    start_entropy, text = calculate_start_entropy(y)
    

    steps[step] = {'text': text,
                    'image': image}


    print(steps[1]['text'])