# ElevenLabs MCP Server

A FastAPI-based MCP server implementation for ElevenLabs text-to-speech API integration.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your ElevenLabs API key
4. Run the server: `python main.py`

## API Endpoints

- `POST /text-to-speech`: Convert text to speech using ElevenLabs API
  - Request body:
    ```json
    {
        "text": "Text to convert to speech",
        "voice_id": "ElevenLabs voice ID"
    }
    ```
- `GET /health`: Health check endpoint

## Environment Variables

- `ELEVENLABS_API_KEY`: Your ElevenLabs API key