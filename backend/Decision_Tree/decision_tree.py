#!/usr/bin/env python3

from ..Utils.fraction import Fraction
from .tree import Tree
from math import log2

step = 1



def gini(p, variable_name):
    #TODO
    #Code gini function
    pass


def entropy(p, variable_name):
    '''
    Returns tuple (text, value)
    '''
    text = ""

    text += f"{variable_name} = E({','.join([str(i) for i in p])}) = "
    
    e = 0
    for v in p:
        text += f"-{str(v)}.log({str(v)}) "
        e -=  v.get_real_value() * log2(v.get_real_value())
    
    text += f"= {e:.4f} bits\n"

    return {'text':text, 'value':e} 

def sum_of_weighted_entropies(weights, entropies, attribute):
    result = 0
    text = ''

    for i in range(len(entropies)):
        result += weights[i].get_real_value() * entropies[i]
        text += f'{weights[i].get_real_value():.3}*{entropies[i]:.3}'
        if i != len(entropies) - 1:
            text += ' + '
    text += ' = '
    text += f'{result}'
    return {'text':text, 'result': result}    


def count_by_type(l):
    p_y = {}
    for c in l:
        if c in p_y:
            p_y[c] += 1
        else:
            p_y[c] = 1
    
    return p_y

def calculate_start(y, function):

    sample_size = len(y)
    #create Dict for P(y = c)
    text = ""

    p_y = count_by_type(y)
    
    for c in p_y:
        p_y[c] = Fraction(p_y[c], sample_size)

    #TODO
    #change name()
    #if entropy -> entropy / if gini -> impurity
    text += f"Determine the Start {function.__name__}:\n"

    for c in p_y:
        text +=  f"P(y={c}) = {p_y[c]}\t"
    
    text += "\n"
    #text += f"E{attribute} = "
    entropy_out = function(p = p_y.values(), variable_name="Estart")
    text += entropy_out['text']
    e_start = entropy_out['value']


    return (e_start, text)


def calculate_attribute_entropy(x, y, attribute):
    text = f"Let us test attribute {attribute}:\n"
    p_y = {}
    total = 0
    #creates a dictionary that counts for each input the output
    #E.g. {a: {+: 3, -:4}} -> when attribute has 'a' as input there is 3 positive outputs and 4 negative outputs

    for i in range(len(x)):
        if (x[i] not in p_y):
            p_y[x[i]] = {y[i]: 1}
        elif (y[i] not in p_y[x[i]]):
            p_y[x[i]][y[i]] = 1
        else:
            p_y[x[i]][y[i]] += 1  

        total += 1  
    
    #TODO
    #Create text and format it something like this-> https://prnt.sc/yRUdKSOEx-bV
    entropies = []
    weights = []
    for key, value in p_y.items():
        temp = []
        w = 0
        for inner_key in value:
            temp.append(Fraction(value[inner_key], sum([i for i in value.values()])))
            w += value[inner_key]

        e = entropy(temp, f"E{attribute}={key}")
        text += e['text']

        entropies.append(e['value'])
        weights.append(Fraction(w, total))

    res = sum_of_weighted_entropies(weights, entropies, attribute)
    text += res['text']
    result = res['result']
    return (result, text)
        
def compute_gain(start_entropy, entropy, attribute):
    result = start_entropy - entropy
    text = f'G({attribute}) = {start_entropy} - {entropy} = {result}\n'

    return result, text




def decision_tree(x, y, attributes, function="entropy"):

    if function == "entropy" :
        function = entropy
    elif function == "gini":
        function = gini

    steps = {}
    text = ""
    image = None
    sample_size = len(y)
    step = 0

    #First Step -> Determine Start Entropy
    start, text = calculate_start(y, function)
    steps[step] = {'text': text,
                    'image': image}
    
    while attributes:
        #test each attribute entropy
        entropies = []
        for i in range(len(attributes)):
            step += 1
            #name of funtion to be changed
            result, text = calculate_attribute_entropy([entry[i] for entry in x], y, attributes[i])
            entropies.append(result)
            steps[step] = {'text': text,
                        'image': image}

        step += 1
        #compute each attribute gain
        gains = []
        text = "Let's compute the gains for each attribute:\n"
        for i in range(len(attributes)):
            gain, t = compute_gain(start, entropies[i], attributes[i])
            gains.append(gain)
            text += t
        
        max_gain = 0
        index = 0
        for i in range(len(attributes)):
            if gains[i] > max_gain:
                index = i
                max_gain = gains[i]
            
        text += f"We choose attribute {attributes[index]} because it provides the highest gain.\n"
        
        steps[step] = {'text': text,
                        'image': image}
        step += 1

        #TODO
        #Build Tree based on max gain attribute

        attributes.remove(attributes[index])

    #print(steps[1]['text'])
    return steps


#print(Fraction(1,2))