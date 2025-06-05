import random

print("🌟 欢迎来到《猜数字》游戏 🎲")
print("现在为你随机准备了一个1到100之间的谜之数字…🤫")
print("你准备好了吗？开始挑战吧！\n")
player_name = input("请告诉我你的名字：")
print(f"好的 {player_name}，祝你好运！👀")

def play_game():    

    secret_number = random.randint(1, 100)  # 让系统藏一个1到100之间的数字

    print("（调试用：正确答案是", secret_number, "）")
    guess_count = 0
    max_guesses = 5 #int(input("你想要几次猜错机会"))
    guessed = False

    while not guessed and guess_count < max_guesses:
        guess = int(input("猜一个 1 到 100 之间的数字："))
        distance = abs(guess - secret_number)
        #print(f"距离是 {distance}，当前第 {guess_count} 次猜") #(调试用)
        guess_count += 1
        if guess < secret_number and distance > 3:
            print("太小啦，再试试～")
            print(f"{player_name}，你已经用了 {guess_count} 次机会！")
            
        elif guess < secret_number and distance <= 3:
            print("太小啦，但是很接近了，再试试～")
            print(f"{player_name}，你已经用了 {guess_count} 次机会！")    
        
        elif guess > secret_number and distance > 3:
            print("太大啦，再来一次～")
            print(f"{player_name}，你已经用了 {guess_count} 次机会！")
            
        elif guess > secret_number and distance <= 3:
            print("太大啦，但是很接近了, 再来一次～")
            print(f"{player_name}，你已经用了 {guess_count} 次机会！")
                
        else:
            print("恭喜你猜对啦！🥳")
            print("你用了", guess_count, "次机会")
            guessed = True

    if not guessed:
        print("😢 猜的次数用完啦！正确答案是", secret_number)

while True:
    play_game()
    play_again = input("还想再玩一局吗？输入 y 开始新一轮，输入其他键退出：")
    if play_again.lower() != 'y':
        print("游戏结束啦～感谢你来玩，抱抱你 👋")
        break    