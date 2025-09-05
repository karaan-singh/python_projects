import pyttsx3

def text_to_speech():
    # Initialize the engine
    engine = pyttsx3.init()

    # Set voice rate
    engine.setProperty('rate', 150)  # Speed (words per minute)

    # Set voice (male/female depending on your system)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female (may vary)

    # Ask user for input
    text = input("Enter the text you want to convert to speech: ")

    # Convert text to speech
    engine.say(text)

    # Play the speech
    engine.runAndWait()

# Run the program
text_to_speech()