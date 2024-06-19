from random import randint

print("THIS IS HUMPYANG GAME!")

player_1 = input("Choose [FOLD or UNFOLD]: ")

print(f"Player_1: {player_1}")

pc_2_input = randint(0, 1)
if pc_2_input == 0:
    pc_2 = "FOLD"
else:
    pc_2 = "UNFOLD"
print(f"Player_Comp2: {pc_2}")

pc_3_input = randint(0, 1)
if pc_3_input == 0:
    pc_3 = "FOLD"
else:
    pc_3 = "UNFOLD"
print(f"Player_Comp3: {pc_3}")

if player_1 == "UNFOLD" and pc_2 == "UNFOLD" and pc_3 == "UNFOLD":
    print("Result: Draw!")
elif player_1 == "UNFOLD" and pc_2 == "FOLD" and pc_3 == "FOLD":
    print("Result: You Won")
elif player_1 == "FOLD" and pc_2 == "UNFOLD" and pc_3 == "FOLD":
    print("Result: Player Computer 2 Won")
elif player_1 == "FOLD" and pc_2 == "FOLD" and pc_3 == "UNFOLD":
    print("Result: Player Computer 3 Won")
