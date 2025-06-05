import tkinter as tk
import random
from tkinter import font

# === 多语言支持 ===
languages = ["cn", "en", "es"]
current_language = "cn"

texts = {
    "cn": {
        "welcome": "猜一个 1 到 100 之间的数字吧～",
        "submit": "提交",
        "too_high": "太大啦～",
        "too_low": "太小啦～",
        "close_high": "太大了，但你已经很接近了！",
        "close_low": "太小了，但你已经很接近了！",
        "congrats": "🎉 猜对啦！你用了 {count} 次机会！",
        "out": "😭 次数用完啦！答案是 {answer}",
        "restart": "再来一次？",
        "input_error": "⚠️ 请输入一个数字！",
        "range_error": "⚠️ 请输入 1 到 100 之间的数字！",
        "guessed": "你刚刚猜的是：{guess}",
        "remaining": "你还剩 {remaining} 次机会",
        "new_round": "新的一轮开始啦！快来猜吧～"
    },
    "en": {
        "welcome": "Guess a number between 1 and 100!",
        "submit": "Submit",
        "too_high": "Too high~",
        "too_low": "Too low~",
        "close_high": "Too high, but you're very close!",
        "close_low": "Too low, but you're very close!",
        "congrats": "🎉 You got it in {count} tries!",
        "out": "😭 Out of tries! The number was {answer}",
        "restart": "Play again?",
        "input_error": "⚠️ Please enter a number!",
        "range_error": "⚠️ Enter a number between 1 and 100!",
        "guessed": "Your last guess: {guess}",
        "remaining": "You have {remaining} tries left",
        "new_round": "A new round begins! Guess away~"
    },
    "es": {
        "welcome": "¡Adivina un número entre 1 y 100!",
        "submit": "Enviar",
        "too_high": "Demasiado alto~",
        "too_low": "Demasiado bajo~",
        "close_high": "Demasiado alto, ¡pero muy cerca!",
        "close_low": "Demasiado bajo, ¡pero muy cerca!",
        "congrats": "🎉 ¡Lo lograste en {count} intentos!",
        "out": "😭 ¡Se acabaron los intentos! Era {answer}",
        "restart": "¿Jugar otra vez?",
        "input_error": "⚠️ ¡Por favor, introduce un número!",
        "range_error": "⚠️ ¡Introduce un número entre 1 y 100!",
        "guessed": "Tu última respuesta: {guess}",
        "remaining": "Te quedan {remaining} intentos",
        "new_round": "¡Nueva ronda! ¡Vamos a jugar!"
    }
}

encouragements = {
    "cn": ["你已经很接近啦！✨", "再试一次，说不定就中了～🎯", "我在这儿陪着你，加油！💖"],
    "en": ["You're getting very close! ✨", "Try again, you're almost there~ 🎯", "I'm cheering for you! 💖"],
    "es": ["¡Estás muy cerca! ✨", "Intenta de nuevo, casi estás ahí~ 🎯", "¡Estoy contigo! 💖"]
}

# === 游戏状态 ===
secret_number = random.randint(1, 100)
guess_count = 0
max_guesses = 5

# === 创建窗口 ===
window = tk.Tk()
window.title("Guess the Number Game")
window.geometry("500x400")
window.configure(bg="#fff0f5")  # 马卡龙背景色

# 添加动画渐变（闪烁提示）
def blink():
    current_color = message.cget("fg")
    next_color = "#ff69b4" if current_color == "#ff1493" else "#ff1493"
    message.config(fg=next_color)
    window.after(500, blink)

# 加载手写风字体（fallback）
try:
    handwriting_font = font.Font(family="Comic Sans MS", size=14)
except:
    handwriting_font = ("Arial", 14)

message = tk.Label(window, font=handwriting_font, bg="#fff0f5")
message.pack(pady=10)
last_guess_label = tk.Label(window, font=("Arial", 12), bg="#fff0f5")
last_guess_label.pack()
remaining_label = tk.Label(window, font=("Arial", 12), bg="#fff0f5")
remaining_label.pack()
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

# === 游戏主逻辑 ===
def check_guess():
    global guess_count
    lang = texts[current_language]
    try:
        guess = int(entry.get())
    except ValueError:
        message.config(text=lang["input_error"])
        entry.delete(0, tk.END)
        return

    if guess < 1 or guess > 100:
        message.config(text=lang["range_error"])
        entry.delete(0, tk.END)
        return

    guess_count += 1
    distance = abs(guess - secret_number)
    entry.delete(0, tk.END)
    last_guess_label.config(text=lang["guessed"].format(guess=guess))
    remaining = max_guesses - guess_count
    remaining_label.config(text=lang["remaining"].format(remaining=remaining))

    if guess == secret_number:
        message.config(text=lang["congrats"].format(count=guess_count))
        restart_button.pack(pady=10)
    elif guess < secret_number and distance <= 3:
        message.config(text=lang["close_low"] + "\n" + random.choice(encouragements[current_language]))
    elif guess < secret_number:
        message.config(text=lang["too_low"])
    elif guess > secret_number and distance <= 3:
        message.config(text=lang["close_high"] + "\n" + random.choice(encouragements[current_language]))
    elif guess > secret_number:
        message.config(text=lang["too_high"])

    if guess_count >= max_guesses and guess != secret_number:
        message.config(text=lang["out"].format(answer=secret_number))
        restart_button.pack(pady=10)

# === 重启游戏 ===
def restart_game():
    global secret_number, guess_count
    secret_number = random.randint(1, 100)
    guess_count = 0
    lang = texts[current_language]
    message.config(text=lang["new_round"])
    entry.delete(0, tk.END)
    last_guess_label.config(text="")
    remaining_label.config(text="")
    restart_button.pack_forget()

# === 设置语言函数 ===
def set_language(lang_code):
    global current_language
    current_language = lang_code
    lang = texts[current_language]
    message.config(text=lang["welcome"])
    button.config(text=lang["submit"])
    restart_button.config(text=lang["restart"])

# === 按钮 ===
button = tk.Button(window, text=texts[current_language]["submit"], font=("Arial", 14), bg="#ffdab9", command=check_guess)
button.pack(pady=10)
restart_button = tk.Button(window, text=texts[current_language]["restart"], font=("Arial", 14), command=restart_game)
restart_button.pack_forget()

lang_frame = tk.Frame(window, bg="#fff0f5")
lang_frame.pack(pady=5)
tk.Button(lang_frame, text="中文", command=lambda: set_language("cn"), bg="#ffd1dc").pack(side="left", padx=5)
tk.Button(lang_frame, text="English", command=lambda: set_language("en"), bg="#b0e0e6").pack(side="left", padx=5)
tk.Button(lang_frame, text="Español", command=lambda: set_language("es"), bg="#f0e68c").pack(side="left", padx=5)

window.bind("<Return>", lambda event: check_guess())
message.config(text=texts[current_language]["welcome"], fg="#ff1493")

blink()
window.mainloop()