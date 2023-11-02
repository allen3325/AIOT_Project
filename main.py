from fastapi import FastAPI

from crawler.craw_chrome import Crawler

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/analyze")
async def emotion_analyze(url: str):
    crawler = Crawler()
    comment_list = crawler.fetch_comment(
        url="https://www.google.com/maps/place/%E4%B8%AD%E8%88%88%E5%A4%A7%E5%AD%B8%E7%B6%9C%E5%90%88%E6%95%99%E5%AD%B8%E5%A4%A7%E6%A8%93/@24.1222692,120.6721234,17z/data=!3m1!5s0x34693cfdf0f370f7:0xb5f97dcd8f1e9311!4m18!1m9!3m8!1s0x34693cfcecffe9d9:0xe28afadc0dad203a!2z5ZyL56uL5Lit6IiI5aSn5a24!8m2!3d24.123552!4d120.675326!9m1!1b1!16zL20vMDR4cDF6!3m7!1s0x34693cfdf13d560b:0xa4002a1f1219e2dd!8m2!3d24.1218109!4d120.6726999!9m1!1b1!16s%2Fg%2F11gvxx_g3b?entry=ttu")
    return comment_list
