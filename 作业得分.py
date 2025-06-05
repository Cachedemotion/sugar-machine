homework_score = int(input("请输入你的作业得分："))
mood = "sweet"
def encourage_me():
    print("Today I'm feeling", mood)
    if homework_score> 50:
        print("I'm fantastic!")
    else:
        print("Might need more hugs.")
encourage_me()

