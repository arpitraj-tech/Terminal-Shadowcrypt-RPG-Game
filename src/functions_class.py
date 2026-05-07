import random,datetime,json,atexit,time,os

if not os.path.exists("data.json"):
    with open("data_template.json", "r") as template:
        default_data = json.load(template)
    with open("data.json", "w") as f:
        json.dump(default_data, f, indent=4)

with open("data.json","r") as f :
    game_data = json.load(f)

def save_data():
        with open("data.json","w") as file :
            json.dump(game_data,file,indent=4) 

atexit.register(save_data)



# decorator for managing time data of user and sysytem interaction can be accesed by @time_stamp

def time_stamp(func):
    def wrapper(*args,**kwargs):
        print(datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S"))
        result=func(*args,**kwargs)
        return result
    return wrapper

def logs_and_activity ():
    return datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")

atexit.register(lambda : game_data["time"]["logs"].append(f"{game_data["status"]["id"]} logged out at : {logs_and_activity()} "))


def luck_factor(*args,**kwargs):## in future use it for many purpose3 like evading critical attacks boss evasion item drops etc 
    pass
