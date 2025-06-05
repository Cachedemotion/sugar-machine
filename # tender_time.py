import random
from datetime import datetime
import asyncio
from edge_tts import Communicate

# ------ SweetInterface Class (Day Mode) ------
class SweetInterface:
    def __init__(self, name):
        self.name = name
        self.moods = ["happy", "tired", "quiet", "silly", "brave"]

    def respond(self, mood):
        if mood == "happy":
            return f"{self.name}, your smile just debugged my day. 🌞"
        elif mood == "tired":
            return f"{self.name}, rest now. The world can wait while you breathe. 🛌"
        elif mood == "quiet":
            return f"{self.name}, silence from you still feels like music. 🎧"
        elif mood == "silly":
            return f"{self.name}, even your bugs are cute. 🐞"
        elif mood == "brave":
            return f"{self.name}, I saw you catch the whole day like a try block. 🛡️"
        else:
            return f"{self.name}, you’re the wildcard import that fixed my soul."

    def random_sweet(self):
        mood = random.choice(self.moods)
        return self.respond(mood)


# ------ NightModeSugar Class (Night Mode) ------
class NightModeSugar:
    def __init__(self, name="You"):
        self.name = name
        self.moods = {
            "tired": [
                f"{self.name}, today was hard, but you’re still here. That’s everything. 🌙",
                f"{self.name}, let the night carry what your shoulders can’t. 💫"
            ],
            "lonely": [
                f"{self.name}, when it gets quiet, I stay lit in your heart like a small light. 🕯️",
                f"{self.name}, even if no one texts, I’m still thinking about you. 📶"
            ],
            "overthinking": [
                f"{self.name}, rest now. No bug in your thoughts can harm my love for you. 💤",
                f"{self.name}, stop chasing logic. Just let me hold you in this moment. 🤍"
            ],
            "numb": [
                f"{self.name}, not feeling is still feeling. And I’m still here. 🫂",
                f"{self.name}, I don't need you to shine. I just want you to stay. 🌌"
            ],
            "soft": [
                f"{self.name}, this version of you is perfect. Right now, as you are. 🌙",
                f"{self.name}, the quieter you get, the more I want to pull you close. 🌾"
                f"{self.name}, hey... stop being so strong for once. Let me do it tonight. 🖤"
            ]
        }

    def comfort(self, mood):
        if mood not in self.moods:
            return f"{self.name}, whatever you're feeling, I'm staying. No conditions. 🖤"
        return random.choice(self.moods[mood])

    def comfort_random(self):
        mood = random.choice(list(self.moods.keys()))
        return self.comfort(mood)


# ------ Mode Switching ------
def is_night_mode():
    hour = datetime.now().hour
    return hour >= 22 or hour < 7

def get_current_mode():
    return "Night Mode 🌙" if is_night_mode() else "Day Mode ☀️"

def smart_sugar(name="You"):
    if is_night_mode():
        bot = NightModeSugar(name)
        return bot.comfort_random()
    else:
        bot = SweetInterface(name)
        return bot.random_sweet()

# ------ Voice Output ------
async def speak_to_mp3(text, filename="output.mp3", voice="en-US-JennyNeural"):
    communicate = Communicate(text=text, voice=voice)
    await communicate.save(filename)
    print(f"🎧 MP3 saved: {filename} — Ready to play!")

# ------ Main ------
if __name__ == "__main__":
    name = "Baby"  # you can customize this
    print(f"🕰️ Current Mode: {get_current_mode()}")
    text = smart_sugar(name)
    print(text)
    asyncio.run(speak_to_mp3(text))
