from Fraction import Fraction
from math import log2

step = 1

class Tree:
    def __init__(self, root):
        self.root = root
        self.tree = {}
    
    def get_root(self):
        return root
    
    def add_branch(self, start, end, path):
        if start in self.tree:
            self.tree[start][path] = end
        else:
            self.tree[start] = {path: end}
    
    def tree_to_image(self):
        #TODO
        #-Get library to show tree
        #-Transform tree format into image with library
        
        pass


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

def sum_of_weighted_entropies(weights, ):
    


def count_by_type(l):
    p_y = {}
    for c in y:
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
    entropy_out = function(p = p_y.values(), variable_name="Estart")
    text += entropy_out['text']
    e_start = entropy_out['value']


    return (e_start, text)


def calculate_something(x, y, attribute):
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
    for key, value in p_y:
        temp = []
        w = 0
        for inner_key in value:
            temp.append(Fraction(value[inner_key], sum([i for i in value.values()])))
            w += value[inner_key]

        e = entropy(temp, f"E{attribute}={key}")
        text += e['text']

        entropies.append(e['value'])
        weights.append(Fraction(w, total))

    sum_of_weighted_entropies(weights, entropies, attribute)

        
            


def decision_tree(x, y, function, attributes):

    steps = {}
    text = ""
    image = None
    sample_size = len(y)

    #First Step -> Determine Start Entropy
    start, text = calculate_start(y, function)
    steps[step] = {'text': text,
                    'image': image}

    entropies = []
    for i in range(len(attributes)):
        step += 1
        #name of funtion to be changed
        calculate_something([entry[i] for entry in x], y, attributes[i])


    print(steps[1]['text'])