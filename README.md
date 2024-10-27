# Text-to-speech Wrapper

`tts-wrapper` is a wrapper around multiple text-to-speech libraries, models and services, giving them a common, simple API. From the users perspective, the different back-ends appear as just different voices.
All generated sound is converted to a [pydub AudioSegment](https://pydub.com/), no matter what the speech-to-text library natively returns, which makes appending sound generated with different back-ends easy.

# Installation

* `pip instal .`
* `python -m unidic download` (for melotts)
* `sudo apt install ffmpeg`
* `python -m nltk.downloader averaged_perceptron_tagger_eng`

Make sure to fill in your Eleven Labs and OpenAI API keys in _.env_ using _.env.template_ in _ttswrapper_

# Usage example

```python
>>> import tts_wrapper

>> tts_wrapper.get_voices()
{'melotts:EN-US': {'title': 'English with EN-US accent',
  'properties': {'speed': {'type': 'number', 'default': 1.0}}},
 'melotts:EN-BR': {'title': 'English with EN-BR accent',
  'properties': {'speed': {'type': 'number', 'default': 1.0}}},
 'melotts:EN_INDIA': {'title': 'English with EN_INDIA accent',
  'properties': {'speed': {'type': 'number', 'default': 1.0}}},
 'melotts:EN-AU': {'title': 'English with EN-AU accent',
  'properties': {'speed': {'type': 'number', 'default': 1.0}}},
 'melotts:EN-Default': {'title': 'English with EN-Default accent',
  'properties': {'speed': {'type': 'number', 'default': 1.0}}},
 'openai:alloy': {'title': 'alloy', 'properties': {}},
 'openai:echo': {'title': 'echo', 'properties': {}},
 'openai:fable': {'title': 'fable', 'properties': {}},
 'openai:onyx': {'title': 'onyx', 'properties': {}},
 'openai:nova': {'title': 'nova', 'properties': {}},
 'openai:shimmer': {'title': 'shimmer', 'properties': {}}}

>>> s = tts_wrapper.render("Hello big beautiful world!", 'melotts:EN-AU')

>>> s.export("test.mp3")

>>> type(s)
pydub.audio_segment.AudioSegment
```

## Adding back-ends

To add a new back-end, make a python package that registers a new entrypoint that points to a python module:

```python
    entry_points = {
        "tts_wrapper.engine": [
            "mybackend = mypackage.mybackend"
        ]
    }
```
The module should provide two functions: `get_voices()` and `render(text, voice, **kw)`.

`get_voices` should return a dictionary with keys that are voice names, suitable as values for the `voice` parameter of `render()`, and values that are dictionaries.
These dictionaries can contain the keys `title` and `properties`, the latter being a json-schema of the optional parameters to `render()`.

`render()` should return a single `pydub.audio_segment.AudioSegment` object.
