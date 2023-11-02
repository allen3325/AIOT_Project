import torch
from udicOpenData.stopwords import *
from gensim.models import Word2Vec
import os

# Check if GPU is available
# load model
project_root_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
w2v_model_dir = f'{project_root_dir}/model/w2v/word2vec.model'
model = Word2Vec.load(w2v_model_dir)

# finished training a model, use much less RAM and allow fast loading and memory sharing
word_vectors = model.wv


# del model

def sent2vec(sent=''):
    """
    Parameters
    ----------
    sent : string
        sentence
    Returns
    -------
    sentence_vector : torch.FloatTensor
        sentence vector from word vector, formatting in torch.tensor
    """
    try:
        if sent == '':
            # return np.array([])
            return []
        sents = list(rmsw(sent, flag=False))
        # sent_vector = np.zeros(model.vector_size)
        sent_vector = 0
        num = 0
        # calculate sentence vector
        for word in sents:
            if word == "":
                print('word is \'\'')
            if word_vectors.__contains__(word):
                num += 1
                sent_vector += word_vectors[word]
        sent_vector /= num
        return torch.tensor(sent_vector)
    except:
        return (torch.tensor([]))

# start_time = time.time()
# print(sent2vec('這餐廳的送餐速度很快，服務也很好'))
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"程式執行時間(workers = 28)：{execution_time:.4f} 秒")


# start_time = time.time()

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"程式執行時間(workers = 28)：{execution_time:.4f} 秒")
