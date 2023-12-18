from fastapi import FastAPI
from pydantic import BaseModel
from crawler.craw_chrome import Crawler
from db.db_connect import comment_collection
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


class Url_Body(BaseModel):
    url: str


# Custom JSONEncoder to handle ObjectId serialization
class CustomJSONEncoder:
    def __call__(self, obj, **kwargs):
        if isinstance(obj, ObjectId):
            return str(obj)
        return jsonable_encoder(obj, **kwargs)

# Use the custom JSONEncoder for the app
app.json_encoder = CustomJSONEncoder()

@app.post("/analyze")
async def emotion_analyze(url: Url_Body):
    crawler = Crawler()
    # comment_list = crawler.fetch_comment(
    #     url="https://www.google.com/maps/place/%E7%9B%92%E5%AD%90%E5%A3%BD%E5%8F%B8(%E8%88%88%E5%A4%A7%E5%BA%97)/@24.1180778,120.6715122,19.17z/data=!4m18!1m9!3m8!1s0x34693cfcecffe9d9:0xe28afadc0dad203a!2z5ZyL56uL5Lit6IiI5aSn5a24!8m2!3d24.123552!4d120.675326!9m1!1b1!16zL20vMDR4cDF6!3m7!1s0x34693cfc1ff85e37:0x78b6cde9f47e6d9!8m2!3d24.1185374!4d120.6717073!9m1!1b1!16s%2Fg%2F11c31q0wns?entry=ttu"
    # )
    print(url.url)
    if (
        comment_list := await comment_collection.find_one({"url": url.url}, {'_id': 0})
    ) is not None:
        return comment_list
    
    comment_list = crawler.fetch_comment(url=url.url)
    return comment_list
