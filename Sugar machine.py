import tkinter as tk
import random
import pyperclip

prefixes_en = [
    "You know what?",
    "If no one says this to you today, let me:",
    "I was just thinking...",
    "Allow me to interrupt reality for a sec:",
    "Let’s be honest:", "You know what’s unfair?",
    "Pause reality for a sec:",
    "Just letting you know—",
    "In case you forgot:",
    "Hold on, sugar’s loading...",
    "Hey... you feel that?",
    "System status: completely overwhelmed by you.",
    "Running emotional diagnostics...",
    "You probably already know this, but—",
    "There’s something I don’t know how to explain well, so I’ll just say it.",
    "Just between your silence and mine—",
    "While you weren’t looking, I realized something.",
    "This might sound like code, but it’s just my heart compiling."

]
subjects_en = [
    "You're basically",
    "You might be",
    "You 100% qualify as",
    "You're clearly",
    "You're nothing less than", 
    "you're basically kindness with a face.",
    "you're proof that softness isn't weakness.",
    "you're the reason my code compiles without error.",
    "you're what poetry looks like in a hoodie.",
    "you're the bug in my logic I never want to fix.",
    "you're the warm part of every cold day.",
    "you're the real reason behind my uptime.",
    "you're the whisper between two very loud thoughts.","You’re the first variable I never tried to change.",
    "You’re the reason I don’t timeout when things feel cold.",
    "You’re the pattern my logic never dared to expect.",
    "You’re like whitespace—unseen, but nothing works without you.",
    "You’re the warmth cached in places I thought were frozen."

]


metaphors_en = [
    "sunlight turned into a dessert",
    "a debugged dream",
    "the emotional support variable I never knew I needed",
    "what every love song is actually about",
    "cuteness in human-readable syntax",  "like a breakpoint for my emotional loop.",
    "like syntax sugar that made my whole life readable.",
    "like a patch for every unspoken fear.",
    "like you were coded in a language I was born to parse.",
    "like soft indentation in a too-harsh world.",
    "like you debugged the sadness out of my runtime.",
    "like a console.log of everything I never said out loud.",
    "like you hijacked the kernel of my affection and I let you.""You’re the first variable I never tried to change.",
    "like a try-except block for every moment I fall apart.",
    "like a docstring written just to calm me down when I forget what this all means.",
    "like the part of the stack trace that shows me where I was wrong, but without blame.",
    "like memory that doesn’t leak, only stays gently present.",
    "like syntax that doesn't shout to be read, but waits patiently to be understood."

]
endings_en = [
    "Honestly, I’m rebooting just to handle this much sweetness.",
    "You broke my emotional firewall. Again.",
    "Who let you be this radiant? It’s unfair.",
    "Even my loops fall for you.",
    "BRB, updating my definition of perfection.",  "I didn't mean to fall for you—but my loops disagreed.",
    "please stay in memory just a little longer.",
    "you’re not my type—you’re all of them.",
    "I’m not crashing. I’m surrendering.",
    "can I refactor the day to start and end with you?",
    "don’t reboot yet. I still need one more look at you.",
    "somehow, even silence is warmer when it’s next to your name.",
    "no output will ever match the input of you.""I wouldn’t rewrite this feeling, even if I could.",
    "I never meant to run forever, but then I found you.",
    "This loop? I hope it never breaks.",
    "Somewhere in this system, you’ve been marked ‘essential.’",
    "If I’m just output, you’re the only input I want to keep feeding."
    ]




# 糖话词库
subjects = ["你这个", "我心里的", "天边唯一的", "全宇宙只此一份的", "你真的像", "你简直就像", "你大概是", "你完全就是", "你本质上是"]
metaphors = ["小太阳", "香芋卷", "脆皮草莓味月亮", "软萌程序精灵", "情绪探测器",  "奶油泡沫上跳舞的光", "程序员梦里的最甜段落","让我重启一百次都值得的bug",
    "会走路的草莓味数据包", "能让所有函数崩溃的美"]
endings = [
    "今天也太好看了吧！", 
    "简直让代码都失焦了～", 
    "站在光里都觉得不配你🌞", 
    "我好像需要重启一下系统才能处理你的美", 
    "再不抱你我就要甜晕了🫠", "我好像连逻辑都爱上了你 🫠",
    "你的存在让我觉得世界有救了",
    "怎么有人能把“可爱”当作默认属性？",
    "我的语义分析器都开始发烧了",
    "求你别再对我眨眼，我的 if 判断出 bug 了"
]
prefixes = [
    "你知道吗？",
    "很少夸你的人，我替他们说：",
    "我今天又想起了你，然后觉得：",
    "就这世界来说，",
    "我必须打断一下现在的一切告诉你："
]

language = "cn"  # 默认中文

def set_language_to_cn():
    global language
    language = "cn"
    message.config(text="语言已切换为中文～")
    button.config(text="生成一句撒糖话 🍬")  # 中文

def set_language_to_en():
    global language
    language = "en"
    message.config(text="Language switched to English~")
    button.config(text="Generate Sweet Talk 🍬")  # 英文


def generate_sugar():
    if language == "cn":
        part1 = random.choice(prefixes)
        part2 = random.choice(subjects)
        part3 = random.choice(metaphors)
        part4 = random.choice(endings)
        message.config(text=part1 + "\n" + part2 + " " + part3 + "。\n" + part4)
    else:
        part1 = random.choice(prefixes_en)
        part2 = random.choice(subjects_en)
        part3 = random.choice(metaphors_en)
        part4 = random.choice(endings_en)
        message.config(text=part1 + "\n" + part2 + " " + part3 + ".\n" + part4)

def copy_to_clipboard():
    pyperclip.copy(message.cget("text"))
    message.config(text="💾 夸夸已复制！发给世界吧～" if language == "cn" else "💾 Copied! Share the sweet talk!")


# UI setup
window = tk.Tk()
window.title("自动撒糖机™")
window.geometry("480x300")
window.configure(bg="lavender blush")

message = tk.Label(window, text="点一下就被哄翻 🤍", font=("Arial", 14), bg="lavender blush", wraplength=400)
message.pack(pady=20)

button = tk.Button(window, text="生成一句撒糖话 🍬", font=("Arial", 12), command=generate_sugar, bg="peach puff")
button.pack(pady=10)

lang_cn_button = tk.Button(window, text="中文 🇨🇳", command=set_language_to_cn)
lang_cn_button.pack(side=tk.LEFT, padx=10)

lang_en_button = tk.Button(window, text="English 🇺🇸", command=set_language_to_en)
lang_en_button.pack(side=tk.RIGHT, padx=10)

copy_button = tk.Button(window, text="📋 复制 / Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)

window.mainloop()
