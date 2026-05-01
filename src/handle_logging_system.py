import functions_class as fc 


def logging_system():
    try:
        if fc.game_data["status"]["grant"]==True:
            print("welcome to RPG_game".center(120))
            fc.game_data["time"]["logs"].append(f"{fc.game_data["status"]["id"]} logged in at  : {fc.logs_and_activity()} ")
            
        else:
            print("\nPLEASE NOTE THAT THIS GAME NOW ONLY SUPPORT 1 ID FOR PLAYER SO CREATE ACCOUNT ONLY IF YOU ARE NEW ELSE IN LOGIN ENTER YOUR USER ID \n")
            print("Before Entering the game please login to your existing account or make a new one\n")

            while True:
                ask_for_account=input("please type 1 to make account and 2 for login : ")

                while ask_for_account not in ["1","2"]:
                    ask_for_account=input("please type 1 to make account and 2 for login : ")

                if ask_for_account=="1":
                    if fc.game_data["status"]["grant"]==True:
                        print("Account already exist so you are login automatically")
                        fc.game_data["status"]["grant"]=True
                        break

                    else:
                        set_id=input("please name Your Id : ")
                        gender=input("Please specify Male -> (M) or Female -> (F) ").lower()

                        while gender not in ["m","f"]:
                            gender=input("Please specify Male -> (M) or Female -> (F) ").lower()

                        fc.game_data["status"]["id"]=set_id

                        if gender == "m" : fc.game_data["status"]["gen"]="M"
                        elif gender == "f" : fc.game_data["status"]["gen"]="F"
                        print("Id created successfully")
                        
                elif ask_for_account=="2":
                    if fc.game_data["status"]["id"]==None:
                        print("account not exist please make 1st ")

                    else:
                        while True:
                            ask=input("please type id : ")

                            if fc.game_data["status"]["id"]==ask:
                                print("login success")
                                fc.game_data["status"]["grant"]=True
                                break

                            else :
                                print("Id not match Pls Retry")
                        break

            fc.save_data()
            fc.game_data["time"]["logs"].append(f"Account is been created as : {fc.game_data["status"]["id"]} and succesfully logged in at  : {fc.logs_and_activity()} ")

    except Exception as e :
        print(e)




if __name__=="__main__":
    pass
