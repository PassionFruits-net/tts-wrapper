#! /usr/bin/python

from setuptools import setup, find_packages
import os.path
    
setup(
    name = "tts-wrapper",
    description = "",
    install_requires = [
        "pydub",
        "soundfile",
        "melotts @ git+https://git@github.com/myshell-ai/MeloTTS.git",
        "openai",
        "elevenlabs"
    ],
    version = "0.0.1",
    author = "Egil Moeller",
    author_email = "redhog@redhog.org",
    license = "GPL",
    url = "https://github.com/redhog/tts-wrapper",
    packages = find_packages(),
    entry_points = {
        "tts_wrapper.engine": [
            "melotts = tts_wrapper.melotts",
            "openai = tts_wrapper.openaitts",
            "elevenlabs = tts_wrapper.elevenlabs"
        ]
    }
)
