from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from elevenlabs import generate, set_api_key
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class TextToSpeechRequest(BaseModel):
    text: str
    voice_id: str

@app.on_event("startup")
async def startup_event():
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise Exception("ELEVENLABS_API_KEY environment variable not set")
    set_api_key(api_key)

@app.post("/text-to-speech")
async def text_to_speech(request: TextToSpeechRequest):
    try:
        audio = generate(
            text=request.text,
            voice=request.voice_id
        )
        return {"audio": audio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)