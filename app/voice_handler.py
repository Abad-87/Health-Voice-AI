import speech_recognition as sr
import pyttsx3

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speech_to_text(self):
        with sr.Microphone() as source:
            print("Please say something:")
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio)
                print("You said: " + text)
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Example Usage
if __name__ == "__main__":
    vh = VoiceHandler()
    spoken_text = vh.speech_to_text()
    if spoken_text:
        vh.text_to_speech(f"You said: {spoken_text}")