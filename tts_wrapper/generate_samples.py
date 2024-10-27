import tts_wrapper
from dotenv import load_dotenv

def generate_sample_sound(voice, text, output_dir):
    s = tts_wrapper.render(text, voice)
    s.export(output_dir + "/%s.mp3" % voice, format="mp3")
    return s

if __name__ == "__main__":
    load_dotenv()
    available_voices = tts_wrapper.get_voices()

    # read text file
    with open("samples/sample_text.txt") as f:
        text = f.read()
    for voice in available_voices:
        print(f"Trying to generate the text using {voice}")
        try:
            s = generate_sample_sound(voice, text, "samples")
        except Exception as e:
            print("Failed to generate sample for %s: %s" % (voice, e))
            continue
