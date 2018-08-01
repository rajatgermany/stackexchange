import os
import json
import re


with open ('./questionMatchingMentionSample.json', 'r') as f:
    clusters = json.load(f)

result = list()
def filteringMentions(question_mention, answer_mention):
    if len(answer_mention) == 1:
        return answer_mention

    question_mention_tokens = question_mention.split(' ')
    question_mention_tokens_lowercase = [token.lower() for token in question_mention_tokens]
    answer_mention = answer_mention.split(' ')
    for mention in answer_mention: 
        if mention in question_mention_tokens or mention in question_mention_tokens_lowercase:
            return
    return ' '.join(answer_mention)
    

def referent_tokens():
    # cluster [0] we are only dealing with one question here
    for cluster in clusters:
        for key, value in cluster.items():
            reffering_tokens = list()
            per_question_referring_tokens = dict()
            for answer_clusters in value:
                question_mention = ''
                per_answer_tokens = list()
                if len(answer_clusters) == 0:
                    reffering_tokens.append([])
                    continue

                for answer_cluster in answer_clusters:
                    each_answer_cluster_tokens = []
                    for item in answer_cluster:
                        if item['position'][0] == 1:
                            question_mention = item['text']
                            each_answer_cluster_tokens.append(question_mention)
                            continue
                    ### Todo find the better solution to reject the tokens
                        mention = filteringMentions(question_mention, item['text'])

                        if mention is not None:
                            each_answer_cluster_tokens.append(mention)
                            # to remove the duplicates
                            each_answer_cluster_tokens = list(set(each_answer_cluster_tokens))
                            print('each_answer_cluster_tokens', each_answer_cluster_tokens)

                    per_answer_tokens.append(each_answer_cluster_tokens)

                reffering_tokens.append(per_answer_tokens)
            per_question_referring_tokens.update({key : reffering_tokens})   
            result.append(per_question_referring_tokens)  
                    
                    
                 
referent_tokens()
with open('questionClusters.json', 'w') as file:
    json.dump(result, file)