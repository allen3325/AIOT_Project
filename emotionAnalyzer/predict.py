# from ex_classifier.a_sent2vec import sent2vec
# from ex_classifier.c_model import SentClassifier
import os
import emoji
from emotionAnalyzer.sent2vec import sent2vec
from emotionAnalyzer.model import SentClassifier
import torch

project_root_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
model_dir = f'{project_root_dir}/model/2(best).bin'
model_state_dict = torch.load(model_dir)
print('################ model load OK')

model = SentClassifier(250, 2)
model.load_state_dict(model_state_dict)


def remove_emojis(text):
    return emoji.replace_emoji(text, '')


def clean_text(sent):
    sent = remove_emojis(sent)
    if sent.find('…'):
        sent = sent.replace('…', '')
    sent = sent.strip()

    return sent


def predict(sent: str = ''):
    """
    Parameters
    ----------
    sent : string
        sentence
    Returns
    -------
    Classifier prediction : string
        The positive or negative predicted by the classifier 
    """
    sent = clean_text(sent)
    if sent == '':
        return ['', '']
    print(f'sent is {sent}')
    input_vec = sent2vec(sent)
    predicted, predicted_class = model.forward(
        input_vec.unsqueeze(0))  # return predicted (predicted_value, predicted_class), predicted_class
    predicted = predicted.tolist()
    # 2d list to 1d list
    score_list = [item for sublist in predicted for item in sublist]
    return [predicted_class, score_list]


def predict_only_res(sent: str = ''):
    predicted_class, score_list = predict(sent)
    if predicted_class == 1:
        return 'negative'
    elif predicted_class == 0:
        return 'True'
    else:
        return ''


if __name__ == '__main__':
    print(predict('上課.考試的地方😆😆😆'))
    print(predict('👍👍 …'))
    print(predict('店內備有一些方便整理頭髮的小道具～老闆娘很細心，會幫忙確認瀏海有沒有遮到眉毛等等，拍照的時候會一邊引導，拍好後再一起看照片討論挑選（老闆娘都會在旁邊給予建議很安心）整間店氣氛很好，闆娘女兒也很親切，有什麼問題或是要求都可以得到回應，基隆居然有這種照相館⋯回家立刻跟我媽說下次還要去這邊拍'))
    print(predict('不喜不悲：）'))
    print(predict('不喜不悲'))
    print(predict('我好開心'))
