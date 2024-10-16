from openai import OpenAI
from pydub import AudioSegment
from io import BytesIO

def get_voices():
    return {
        "alloy": {"title": "alloy", "properties": {}},
        "echo": {"title": "echo", "properties": {}},
        "fable": {"title": "fable", "properties": {}},
        "onyx": {"title": "onyx", "properties": {}},
        "nova": {"title": "nova", "properties": {}},
        "shimmer": {"title": "shimmer", "properties": {}}
    }

client = None

def render(text, voice, **kw):
    global client
    if client is None:
        client = OpenAI()

    model = "tts-1-1106" #tts-1, tts-1-1106, tts-1-hd, tts-1-hd-1106

    tts_response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text,
        **kw
    )
    return AudioSegment.from_file(BytesIO(tts_response.content), format="mp3")
