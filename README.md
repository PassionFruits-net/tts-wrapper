# Text-to-speech Wrapper

`tts-wrapper` is a wrapper around multiple text-to-speech libraries, models and services, giving them a common, simple API. From the users perspective, the different back-ends appear as just different voices.
All generated sound is converted to a [pydub AudioSegment](https://pydub.com/), no matter what the speech-to-text library natively returns, which makes appending sound generated with different back-ends easy.

Usage example:

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
