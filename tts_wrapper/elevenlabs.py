from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
from io import BytesIO

def get_voices():
    voices = client.voices.get_all().voices
    return {voice.name: {"title": voice.name, "properties": {}} for voice in voices}

client = None
def render(text, voice, **kw):
    global client
    if client is None:
        client = ElevenLabs()

    model = "eleven_multilingual_v2"
    tts_response = client.generate(
        text=text,
        voice=voice,
        model=model
    )

    return AudioSegment.from_file(BytesIO(b''.join(tts_response)), format="mp3")