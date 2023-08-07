# Project Treasure Island
print("Welcome to the Treasure Island")
print("Your mission is to find the Treasure")
sample_direction = input("Choose the direction - Left or Right : ")
direction = sample_direction.lower()
if direction == "left":
  sample_option = input("Choose the option - Swim or Wait : ")
  option = sample_option.lower()
  if option == "wait":
    sample_color = input("choose the door colour which you want to enter : Red or Blue or Yellow : ")
    door_color = sample_color.lower()
    if door_color == "blue":
      print("Game Over!!!, You have entered the door which is the enterance to sea.")
    elif door_color == "red":
      print("Game Over!!!, This is the enterance to the volcanic vent.")
    elif door_color == "yellow":
      print("You have won!!!, The treasure is yours")
      print(r"""             _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'""")
    else:
      print("You have chosen the invalid option")
  else:
    print("Game Over!!, The water contains acids")
else:
  print("Game over, You have fallen in the fire")
