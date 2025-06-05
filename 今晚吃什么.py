import random

dinner_options = ["寿司", "披萨", "火锅", "烤鸡", "牛肉面", "炒河粉", "沙拉", "鸡蛋三明治", "拉面", "外卖一切随缘"]

def add_dish(dish_name):
    dinner_options.append(dish_name)



new_dishes = input("有没有什么菜你今天特别想吃？（多个请用逗号隔开）")
for dish in new_dishes.split("，"):
    for _ in range(4):  # 增加 4 次“权重”
        add_dish(dish.strip())
  
def what_to_eat():
    choice = random.choice(dinner_options)
    print("今晚吃什么呢？让宇宙帮你选！🍽️")
    print("你的命中注定是 ——", choice)

what_to_eat()
