import json
import os
import sys
from decodingScript import buildText
from stanfordCoreNlp import buildCoref

def setup (file_index):
    buildText(file_index)
    buildCoref(file_index)



if __name__ == "__main__":
    file_index = str(str(sys.argv[1]))
    setup(file_index)    