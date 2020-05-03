print("Welcome to Guessing Game!")
num=3
iterator=0
is_win=False
while iterator < 3:
  iterator+=1
  guess_num=int(input("Guess the number "))
  if guess_num==num:
    print("You won!")
    is_win=True
    break
  else:
    print("Another guess? ")
    if is_win == True:
        print("Congrats!")
    else:
        print ("You lost!")

#
#
# # Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# # Give user input box: 1. To capture guesses,
# # print(and input boxes) 1. If user wins 2. If user loses
# print('Texmin oyunu')
# num = 3
# iterator = 0
# is_win = False
# ​
# while iterator < 3:
#     iterator += 1
#     guess_num = int(input('Texmininizi daxil edin: '))
#     if guess_num == num:
#         print('Siz qalib geldiniz! Komputerin yaddinda saxladigi reqem', num, 'idi')
#         is_win = True
#         break
#     else:
#         print('Texmininiz yalnisdir')
# if is_win == True:
#     print('Tebrikler')
# else:
#     print('Oyun bitti')
