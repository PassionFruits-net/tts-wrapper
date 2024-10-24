from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
from io import BytesIO

_client = None
def get_client():
    global _client
    if _client is None:
        _client = ElevenLabs()
    return _client

def get_voices():
    client = get_client()
    voices = client.voices.get_all().voices
    return {voice.name: {"title": voice.name, "properties": {}} for voice in voices}

def render(text, voice, **kw):
    client = get_client()
    model = "eleven_multilingual_v2"
    tts_response = client.generate(
        text=text,
        voice=voice,
        model=model
    )

    return AudioSegment.from_file(BytesIO(b''.join(tts_response)), format="mp3")
