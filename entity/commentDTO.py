from emotionAnalyzer.predict import predict
from pydantic import BaseModel
from typing import Optional, List

class Comment(BaseModel):
    user_name: str
    comment: str
    rating: int
    emotion_classification: str = None
    emotion_score: List[float] = None


    def __init__(self, user_name: str, comment: str, rating: int):
        # self.user_name = user_name
        # self.comment = comment
        # self.rating = rating
        # self.emotion_classification = None
        # self.emotion_score = None
        super().__init__(user_name=user_name, comment=comment, rating=rating)
        self.predict_and_set_emotion(comment=comment)

    # def __new__(cls, user_name: str, comment: str, rating: int):
    #     return super().__new__(cls)
    
    # def __dict__(self):
    #     return {
    #         "user_name": self.user_name,
    #         "comment": self.comment,
    #         "rating": self.rating,
    #         "emotion_classification": self.emotion_classification,
    #         "emotion_score": self.emotion_score
    #     }

    # def __str__(self):
    #     return f"使用者：{self.user_name}\n評論：{self.comment}。\nGoogle 評分：{self.rating}\n情緒分析：{self.emotion_classification}\n情緒分析分數：{self.emotion_score}"

    def predict_and_set_emotion(self, comment: str):
        # print(f"comment is {comment}")
        predicted_class, score_list = predict(comment)
        self.emotion_classification = predicted_class
        self.emotion_score = score_list
