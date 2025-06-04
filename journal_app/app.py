import os
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import openai


def listen():
    """Capture voice input from the microphone and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as err:
        print(f"Speech recognition error: {err}")
        return ""


def speak(text: str) -> None:
    """Read text aloud using text-to-speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def log_entry(entry: str) -> None:
    """Save an entry to today's journal file."""
    date_prefix = datetime.now().strftime("%Y-%m-%d")
    with open(f"journal_{date_prefix}.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%H:%M:%S")
        f.write(f"{timestamp}: {entry}\n")


def generate_reply(prompt: str) -> str:
    """Generate an AI response using OpenAI's Chat API."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful journaling assistant focused on health, "
                    "wellness, and high performance."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )
    reply = response["choices"][0]["message"]["content"]
    return reply.strip()


def main() -> None:
    while True:
        user_text = listen()
        if user_text.lower() in {"quit", "exit", "stop"}:
            break
        log_entry(f"user: {user_text}")
        reply = generate_reply(user_text)
        log_entry(f"assistant: {reply}")
        speak(reply)


if __name__ == "__main__":
    main()
