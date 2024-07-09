from gtts import gTTS
from pydub import AudioSegment
import pygame
import os

text = str("")
language = 'en'

try:
    # Create gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the converted audio in a file
    tts.save("output.mp3")
    print("Audio file saved successfully.")
except Exception as e:
    print(f"Error: {e}")

# Play the saved audio file using pygame
try:
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load("output.mp3")

    # Play the audio file
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick value as needed

    # Close the mixer
    pygame.mixer.quit()

except Exception as e:
    print(f"Error playing audio: {e}")
