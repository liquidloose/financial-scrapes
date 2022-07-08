from fastapi import FastAPI
import scrape

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/scrape_money")
async def money():
    '''Returns scrape results'''
    return await scrape.scrape()
