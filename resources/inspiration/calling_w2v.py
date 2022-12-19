import gensim
import os
import pathlib

# lets load the model
current_path = os.path.abspath(__file__) # path of the file
path_obj = pathlib.Path(current_path) # lets go above
path_model = str(path_obj.parent.parent) + '/models/GoogleNews-vectors-negative300-SLIM.bin' # add model path
#print('path of the model : ', path_model)
model = gensim.models.KeyedVectors.load_word2vec_format(path_model, binary=True)

def call_w2v(word1, word2):
    '''
    function to compute similarity score
    from resources.inspiration.calling_w2v import call_w2v
    print(call_w2v('bread', 'butter'))
    '''
    result = model.similarity(word1, word2) # note model.wv.similarity(word1, word2) is deprecated
    return result

