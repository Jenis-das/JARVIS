import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()


# Set speech rate (default ~200)
engine.setProperty('rate', 150)  # slower, more Jarvis-like

# Set volume (0.0 to 1.0)
engine.setProperty('volume', 0.1)

# List all available voices
voices = engine.getProperty('voices')

# Pick a deep male voice for Jarvis (usually index 0 or check above)
engine.setProperty('voice', voices[0].id)  # change index if needed
# voices[0].id  # change index if needed
# voices[1], voices[2]

# Speak it
def speak(text):
    """Speak the text asynchronously so it doesn’t block."""
    engine.say(text)
    engine.runAndWait()
