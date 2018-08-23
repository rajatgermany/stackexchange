import os
import json
k = list()
g = []
with open('final_coref.json', 'r') as f:
    data = json.load(f)

for items in data:
    for key, values in items.items():
        print(key)
        m = []
        if isinstance(values, list):
            for value in values:
                validClusters = []
                for cluster in value:
                    for mention in cluster:
                        if mention['position'][0] == 1:
                            validClusters.append(cluster) 
                m.append(validClusters) 
            k.append({key: m})

with open('questionMatchingMentionSample.json', 'w') as q:
    json.dump(k, q)    

