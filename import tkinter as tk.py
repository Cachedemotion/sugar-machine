import tkinter as tk
import random

encouragements = [
    "你已经很接近啦！✨",
    "再试一次，说不定就中了～🎯",
    "我在这儿陪着你，加油！💖",
    "你的小宇宙快爆发啦～🌌",
    "下一次一定行的！👍",
    "你这么聪明，数字不敢不被你猜中👀",
    "别气馁，我偷偷支持你～🫶",
    "失败只是成功的伏笔✍️"
]
extra = random.choice(encouragements)

# 创建窗口
window = tk.Tk()
window.title("猜数字游戏")
window.geometry("400x300")

# 生成随机数字
secret_number = random.randint(1, 100)
guess_count = 0
max_guesses = 5

# 创建提示标签
message = tk.Label(window, text="猜一个 1 到 100 之间的数字吧～", font=("Arial", 14))
message.pack(pady=10)

# 在界面上显示上一轮猜的数字和剩余次数
last_guess_label = tk.Label(window, text="", font=("Arial", 12))
last_guess_label.pack()
remaining_label = tk.Label(window, text="", font=("Arial", 12))
remaining_label.pack()


# 输入框
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

# 处理猜测逻辑
def check_guess():
    global guess_count
    try:
        guess = int(entry.get())
    except ValueError:
        message.config(text="⚠️ 请输入一个数字！")
        entry.delete(0, tk.END)
        return

    if guess < 1 or guess > 100:
        message.config(text="⚠️ 请输入 1 到 100 之间的数字！")
        entry.delete(0, tk.END)
        return

    guess_count += 1
    distance = abs(guess - secret_number)
    entry.delete(0, tk.END)
    last_guess_label.config(text=f"你刚刚猜的是：{guess}")
    remaining = max_guesses - guess_count
    remaining_label.config(text=f"你还剩 {remaining} 次机会")

    if guess == secret_number:
        message.config(text=f"🎉 猜对啦！你用了 {guess_count} 次机会！")
        restart_button.pack(pady=10)  # 🆗 现在才显示按钮
    elif guess < secret_number and distance <= 3:
        message.config(text="太小了，但你已经很接近了!\n"+extra)
    elif guess < secret_number:
        message.config(text="太小啦～")
    elif guess > secret_number and distance <= 3:
        message.config(text="太大了，但你已经很接近了！\n"+extra)
    elif guess > secret_number:
        message.config(text="太大啦～")

    if guess_count >= max_guesses and guess != secret_number:
        message.config(text=f"😭 次数用完啦！答案是 {secret_number}")
        restart_button.pack(pady=10)  # 🆗 现在才显示按钮

def restart_game():
    global secret_number, guess_count
    secret_number = random.randint(1, 100)
    guess_count = 0
    message.config(text="新的一轮开始啦！快来猜吧～")
    entry.delete(0, tk.END)
    last_guess_label.config(text="")
    remaining_label.config(text="")
    restart_button.pack_forget()  # 隐藏自己


# 提交按钮
button = tk.Button(window, text="提交", bg="peach puff", font=("Arial", 14), command=check_guess)
button.pack(pady=10)

#再来一次按钮
restart_button = tk.Button(window, text="再来一次？", font=("Arial", 14), command=restart_game)
restart_button.pack_forget()  # 一开始不显示

window.bind("<Return>", lambda event: check_guess())
# 开始运行窗口
window.mainloop()
