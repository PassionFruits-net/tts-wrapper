import melo.api
from melo.api import TTS
import soundfile as sf
import io
import pydub

_model = None
def get_model():
    global _model
    if _model is None:
        _model = melo.api.TTS(language='EN', device="auto")
    return _model

def get_voices():
    model = get_model()
    return {key: {"title": "English with %s accent" % key,
                  "properties": {"speed": {"type": "number", "default": 1.0}}}
            for key in model.hps.data.spk2id.keys()}

def render(text, voice, **kw):
    model = get_model()
    sound = model.tts_to_file(text, model.hps.data.spk2id[voice], **kw)
    f = io.BytesIO()
    sf.write(f, sound, samplerate=model.hps.data.sampling_rate, format="wav")
    return pydub.AudioSegment.from_file(f, format="wav")
