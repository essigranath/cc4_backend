from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from textblob import TextBlob
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_sentiment(request: Request):
    # haetaan JSON data pyynnöstä
    data = await request.json()
    text = data.get("text", "")
    # tarkistetaan että tekstikenttä on olemassa
    if not text:
        raise HTTPException(status_code=400, detail="Text field is required.")
    # analysoidaan tekstin sentiment
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    # palautetaan analyysi JSON muodossa
    return JSONResponse(content={
        "sentiment": sentiment,
        "score": polarity
    })


