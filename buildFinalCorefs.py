import json
import os
from os import listdir
from os.path import isfile, join


dir_path = './corefs/'
onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
data = []

def change_key_of_item(item , index) :
    updated_dict = dict()
    print('item', type(item), item.keys)
    for key , value in item.items():
        print('key', key, index)
        if key == 'question':
            continue
        new_index = int(key) + ((index -1)  * 100)
        updated_dict.update({new_index: value})

    return updated_dict  


for i in range(1, 9):
    file_name = 'coref'+ str(i) + '.json'
    file_path = join(dir_path + file_name)
    with open(file_path, 'r') as f:
        coref = [change_key_of_item(item, i) for item in json.load(f)]
        data = data + coref


with open('final_coref.json', 'w') as f:
    json.dump(data, f)        