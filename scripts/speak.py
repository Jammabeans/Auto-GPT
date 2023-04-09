import os
from playsound import playsound
import requests
from config import Config
cfg = Config()
import gtts

# Updated voices list
voices = [
    {"name": "Rachel", "voice_id": "21m00Tcm4TlvDq8ikWAM"},
    {"name": "Domi", "voice_id": "AZnzlk1XvdvUeBnXmlld"},
    {"name": "Bella", "voice_id": "EXAVITQu4vr4xnSDxMaL"},
    {"name": "Antoni", "voice_id": "ErXwobaYiN019PkySvjV"},
    {"name": "Elli", "voice_id": "MF3mGyEYCl7XYWbV9V6O"},
    {"name": "Josh", "voice_id": "TxGEqnHWrfWFTfGW9XjX"},
    {"name": "Arnold", "voice_id": "VR6AewLTigWG4xSOukaG"},
    {"name": "Adam", "voice_id": "pNInz6obpgDQGcFmaJgB"},
    {"name": "Sam", "voice_id": "yoZ06aMxZJJ28mfd3POQ"}
]

tts_headers = {
    "Content-Type": "application/json",
    "xi-api-key": cfg.elevenlabs_api_key
}

# Function to get the voice id by name
def get_voice_id_by_name(name):
    for voice in voices:
        if voice["name"] == name:
            return voice["voice_id"]
    return None

def eleven_labs_speech(text, voice_name):
    voice_id = get_voice_id_by_name(voice_name)
    if voice_id is None:
        print("Voice not found")
        return False

    tts_url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}".format(
        voice_id=voice_id)
    formatted_message = {"text": text}
    response = requests.post(
        tts_url, headers=tts_headers, json=formatted_message)

    if response.status_code == 200:
        with open("speech.mpeg", "wb") as f:
            f.write(response.content)
        playsound("speech.mpeg")
        os.remove("speech.mpeg")
        return True
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        return False

def gtts_speech(text):
    tts = gtts.gTTS(text)
    tts.save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")

def say_text(text, voice_name=os.getenv("VOICE_NAME")):
    if not cfg.elevenlabs_api_key:
        gtts_speech(text)
    else:
        success = eleven_labs_speech(text, voice_name)
        if not success:
            gtts_speech(text)

