from torch.utils import data
import pandas as pd
from emotionAnalyzer.sent2vec import sent2vec

class SentDataloader(data.Dataset):
    def __init__(self, fpath):

        # Initialize path and transform dataset
        # sample = []
        # input = sent2vec('')
        # target = 1
        # sample.append([input, target])
        # sample.append([input, target])
        # sample.append([input, target])



        sample = []
        data = pd.read_csv(fpath)
        column_names = list(data.columns)
        sents = list(data.iloc[:, 0])  # 將句子轉為字串
        targets = list(data.iloc[:, 1]) #取第二行轉為list
        a=0
        for idx, sent in enumerate(sents):
            sent = str(sent).replace("\"", "")
            sent = str(sent).replace(" ", "")
            input = sent2vec(sent)
            target = targets[idx]
            target = (1 if target == 'negative' else 0)
            if len(input) != 0:
                sample.append([input, target])
            else:
                continue
            # if a==0:
            #     a+=1
                # print("sent is "+sent+" is "+targets[idx])
                # input_vec, target = sample[0]
                # print(input_vec)
                # print(target)
        self.sample = sample
        # input_vec, target = sample[0]
        # print(input_vec)
        # print(target)

    def __getitem__(self, idx):

        # Return the data (e.g. sentence_vec and label)
        return self.sample[idx]

    def __len__(self):
        
        # Indicate the total size of the dataset
        return len(self.sample)

# start_time = time.time()
# SentDataloader('/home/112_ms_wei/nlp-tutorials/w2v_classifier/udicstm_for_dataloader.csv')
# SentDataloader('/home/112_ms_wei/nlp-tutorials/w2v_classifier/data/udicstm_train.csv')
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"程式執行時間(workers = 28)：{execution_time:.4f} 秒")
