# Word2Vec processor
# From: https://www.geeksforgeeks.org/python-word-embedding-using-word2vec/

from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
warnings.filterwarnings(action = 'ignore') 
import gensim 
from gensim.models import Word2Vec 

# sg = Use SkipGram model versus default CBOW 
def myw2v(txt, source_word, target_word, sg=0):   
    f = txt.replace("\n", " ") 
    data = [] 

    # iterate through each sentence in the file 
    for i in sent_tokenize(f): 
        temp = []
        # tokenize the sentence into words 
        for j in word_tokenize(i): 
            temp.append(j.lower()) 
    
        data.append(temp)
    
    model = gensim.models.Word2Vec(data, min_count = 1, size = 100, window = 5, sg = sg) 
    return model.similarity(source_word, target_word) 
        
    
    