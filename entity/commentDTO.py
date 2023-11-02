from emotionAnalyzer.predict import predict


class Comment:
    def __init__(self, user_name: str, comment: str, rating: int):
        self.user_name = user_name
        self.comment = comment
        self.rating = rating
        self.emotion_classification = None
        self.emotion_score = None
        self.predict_and_set_emotion(comment=comment)

    def __new__(cls, user_name: str, comment: str, rating: int):
        return super().__new__(cls)

    def __str__(self):
        return f"使用者：{self.user_name}\n評論：{self.comment}。\nGoogle 評分：{self.rating}\n情緒分析：{self.emotion_classification}\n情緒分析分數：{self.emotion_score}"

    def predict_and_set_emotion(self, comment: str):
        print(f"comment is {comment}")
        predicted_class, score_list = predict(comment)
        self.emotion_classification = predicted_class
        self.emotion_score = score_list
