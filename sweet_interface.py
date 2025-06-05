# sweet_interface.py
import random
import pyperclip

class SweetInterface:
    def __init__(self, partner_name):
        self.name = partner_name
        self.moods = ["happy", "tired", "quiet", "silly", "brave"]

    def respond(self, mood):
        if mood == "happy":
            return f"{self.name}, your smile just refactored my entire worldview. 🌞"
        elif mood == "tired":
            return f"{self.name}, come rest here. You don't need to compile perfection today. 🛌"
        elif mood == "quiet":
            return f"{self.name}, your silence is not empty—it's a soft loop of presence. 🌙"
        elif mood == "silly":
            return f"{self.name}, even your syntax errors are adorable. 🤪"
        elif mood == "brave":
            return f"{self.name}, I saw your try block catch the whole day without crashing. 🛡️"
        else:
            return f"{self.name}, you're the wildcard import that fixed my soul."

    def random_sweet(self):
        return self.respond(random.choice(self.moods))
from sweet_interface import SweetInterface

you = SweetInterface("宝贝")

print(you.respond("tired"))
print(you.random_sweet())
import tkinter as tk
from sweet_interface import SweetInterface

sugarbot = SweetInterface("Baby")

def say_sweet():
    sweet = sugarbot.random_sweet()
    message.config(text=sweet)

def copy_to_clipboard():
    pyperclip.copy(message.cget("text"))
    message.config(text="💾 夸夸已复制！发给世界吧～" if language == "cn" else "💾 Copied! Share the sweet talk!")

window = tk.Tk()
window.title("恋爱模式：ON")
window.geometry("480x300")

message = tk.Label(window, text="点击启动甜话协议 🩵", font=("Arial", 14), wraplength=400)
message.pack(pady=20)

button = tk.Button(window, text="Generate Sweet Talk 🍬", font=("Arial", 12), command=say_sweet)
button.pack(pady=10)

copy_button = tk.Button(window, text="📋 复制 / Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)

window.mainloop()
