import json
import string

string_list = list(string.ascii_uppercase)

dictionary = {}
dictionary['alphabet'] = {}
for l in string_list:
    print("== letting {}".format(l))
    #sd = input('path to sound: ')
    el1 = input('element 1 name: ')
    #el1_path = input('element 1 path: ')
    
    el2 = input('element 2 name: ')
    #el2_path = input('element 2 path: ')
    
    [sd, el1_path, el2_path] = [l,l,l]
    
    bhs = [
        {"sound":sd},
        {"example":el1, "image":el1_path },
        {"example":el2, "image":el2_path },
    ]
    
    dic = {l:bhs}
    #dictionary['alphabet'].append(dic)
    dictionary['alphabet'].update({l: bhs})
    print(dic)

"""
dictionary = {
    "alphabet":{
        "A":bhs
        }
    }

"""

with open('data.json', 'w') as outfile:
    json.dump(dictionary, outfile)
