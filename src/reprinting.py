import os 
import functions_class as fc 

# current_player=fc.Player(fc.game_data["status"]["id"])

def clear_screen(current_player):
    fc.save_data()
    if os.name=="nt":
        os.system('cls')
    else:
        os.system('clear')

#######################      Declaring salutation ##############################


    if fc.game_data["status"]["gen"]=="M" : salutaion = "Mr."
    elif fc.game_data["status"]["gen"]=="F" : salutaion = "Miss."



################          Welcome Screen       ##########################
    # print("*"*120)
    print("⭐"*60)
    print("       ***********************".center(108))
    print(f"       * welcome {salutaion} {fc.game_data["status"]["id"]} *".center(107))
    print("       ***********************".center(108))

    # print("*"*120)
    print("⭐"*60)

# ~~~~~~~~~~#####~~~~~~~~~~~  Printing Player Infos  ~~~~~~~~~~~~~####~~~~~~~~~~~~~~~~
    """
f-string inside fstring is used with :<(int) for left assignment and :^(int) for center and :>(int) for right assignment see in line 1-3 below 
    """
### Line 1
    print(f"{f'Current Level : {current_player.get_lvl()}':<40}",end=" ")         

    print (f"{f'Total exp earned : {current_player.get_total_exp()}':^40}",end=" ")

    print(f"{f'Current Exp : {current_player.get_exp()}\n':>40}")

### Line 2
    print(f"{f'Current health : {current_player.current_health()}/{current_player.get_health()}':<40}",end=" ")

    print(f"{f'Current Defence : {current_player.defence_()}':^40}",end=" ")

    print(f"{f'Heal : {current_player.heal}\n':>40}")

### Line 3
    print(f"{f'Rank : {current_player.get_rank()}':<40}",end=" ")

    print(f"{f'Normal Atk Power : {current_player.normal_attack_power()}':^40}",end=" ")

    print(f"{f'Super Atk Power : {current_player.super_attack_power()}\n':>40}")

### Line 4
    print(f"Super Powers : {current_player.super_power}\n")

    print(f"Abilities    : {current_player.abilities}\n")

    print(f"Items        : {current_player.items}")


###############       Now make the flow of RPG system     ##########################
    # print("*"*120)
    print("⭐"*60)
    print("\n")
    
############################################
    




if __name__=="__main__":
    pass