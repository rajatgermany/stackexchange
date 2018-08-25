import os
import json
import itertools

# file_paths
data_dir_path = './cooking.stackexchange.com'
train_file_path = os.path.join(data_dir_path, 'valid.tsv')
question_file_path = os.path.join(data_dir_path, 'questions.tsv')
answers_file_path = os.path.join(data_dir_path, 'answers.tsv')
vocab_file_path = os.path.join(data_dir_path, 'vocab.tsv')

## params
vocabularyList = []
answerLabels = dict()
questionLabels = dict()
result = []

def buildQuestionDict():
    with open(question_file_path, 'r') as question:
        for line in question:
            indexs = ' '.join(line.split()).split(' ')
            questionLabels.update({indexs[0]: indexs[1:]})

def buildAnswerLabelsDict():
    with open(answers_file_path, 'r') as answer:
        for line in answer:
            indexs = ' '.join(line.split()).split(' ')
            answerLabels.update({indexs[0]: indexs[1:]})

def buildVocabulary():
    with open(vocab_file_path, 'r') as vocab:
        for line in vocab:
            indexs = ' '.join(line.split()).split(' ')
            vocabularyList.append(indexs)

def setup():
    buildVocabulary()
    buildQuestionDict()
    buildAnswerLabelsDict()
    
def buildString(index, type):
    result_list_of_strings = []

    if type == 'question':
        indexs = questionLabels[index]
    if type == 'answer':
        indexs = answerLabels[index]

    for item in indexs:
        for vocabulary in vocabularyList:
            if vocabulary[0] == item:
                result_list_of_strings.append(vocabulary[1])
                break
    return ' '.join(result_list_of_strings)

    
def buildQuestionAnswerPair(file_index):
    with open(train_file_path, 'r') as file:
        range_start = (file_index -1) * 100
    
        range_end = range_start + 100
        print('range', range_start, range_end)
        for line in itertools.islice(file, range_start, range_end):
            question_answer_pair = dict()
            indexs = ' '.join(line.split()).split(' ')
            question_index = indexs[0]
            answer_indexs = indexs[1:21]
            
            question_string = buildString(question_index, 'question')
            list_of_answer_strings = []

            for answer_index in answer_indexs:
                anwer_string = buildString(answer_index, 'answer')
                print('anwer_string', anwer_string)
                list_of_answer_strings.append(anwer_string)

            question_answer_pair.update({question_string: list_of_answer_strings})
            result.append(question_answer_pair)


        
def buildText(file_index):
    setup()
    questionAnswerPair = buildQuestionAnswerPair(int(file_index))
    output_file_path = './textData' + file_index + 'cooking_valid' + '.txt'
    with open(output_file_path, 'w') as output:
        for item in result:
            for key , value in item.items():
                output.write('start question'+ '\n')
                output.write(key + '\n')
                for answer in value:
                    output.write(answer + '\n')
                output.write('end question')
                output.write('\n')


