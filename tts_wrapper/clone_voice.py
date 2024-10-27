import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from pydub import AudioSegment
from io import BytesIO
from elevenlabs.client import ElevenLabs

if __name__ == "__main__":
    load_dotenv()
    client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

    samples_dir = Path("samples")
    sample_text_path = samples_dir/"sample_text.txt"
    with open(sample_text_path, "r") as f:
        sample_text = f.read()

    name = sys.argv[1]
    cloned_voice_dir = Path(f"clone_samples/{name}")
    voice_description_path = cloned_voice_dir/"description.txt"
    sample_files = list(cloned_voice_dir.glob('*.mp3'))
    with open(voice_description_path, "r") as f:
        description = f.read()
    voice = client.clone(
        name=name,
        description=description,
        files=sample_files,
    )

    audio = client.generate(text=sample_text, voice=voice)
    s = AudioSegment.from_file(BytesIO(b''.join(audio)), format="mp3")
    s.export(str(samples_dir) + "/%s.mp3" % name, format="mp3")
