import importlib.metadata

_entrypoints = None
def get_entrypoints():
    global _entrypoints
    if not _entrypoints:
        _entrypoints = {entrypoint.name: entrypoint.load()
                        for entrypoint in importlib.metadata.entry_points(
                                group="tts_wrapper.engine")}
    return _entrypoints

def get_voices():
    res = {}
    for name, mod in get_entrypoints().items():
        for voice, voiceargs in mod.get_voices().items():
            res["%s:%s" % (name, voice)] = voiceargs
    return res

def render(text, voice, **kw):
    engine, voice = voice.split(":", 1)
    return get_entrypoints()[engine].render(text, voice, **kw)
    
