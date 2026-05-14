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

class LevelManager(): #controls power of every enemies and boss of different lvls and levelsystem of player 
    def __init__(self,level=1,exp=0,total_exp_accuired=100,health=500):
        self.level=level
        self.exp=exp
        self.total_exp_accuired=total_exp_accuired
        self.health=health

    
    def levels(self):
        while True:
            if self.level<10:
                req_exp=100
            elif self.level<25:
                req_exp=300
            elif self.level<50:
                req_exp=1000
            elif self.level<90:
                req_exp=10000
            elif self.level<95:
                req_exp=20000
            elif self.level<99:
                req_exp=50000
            elif self.level==99:
                req_exp=100000000
            else:
                req_exp=self.level*(100000000)
            
            if self.exp >= req_exp:
                self.exp-=req_exp
                self.level+=1
                game_data["player"][self.name]["health_lock"]=True
            else:
                break
    
    def get_lvl(self):
        self.levels()
        return self.level
    
    def get_exp(self):
        self.levels()
        return self.exp
    
    def get_total_exp(self):
        x=self.get_lvl()
        if self.level<10:
            req_exp=100*x+self.exp
        elif self.level<25:
            req_exp=300*x+self.exp
        elif self.level<50:
            req_exp=1000*x+self.exp
        elif self.level<90:
            req_exp=10000*x+self.exp
        elif self.level<95:
            req_exp=20000*x+self.exp
        elif self.level<99:
            req_exp=50000*x+self.exp
        elif self.level==99:
            req_exp=100000000*x+self.exp
        else:
            req_exp=self.level*(100000000)*x+self.exp
        
        return req_exp
        
    def get_health(self):
        x=self.get_lvl()
        if x <=25:
            self.health=(pow(x,1.2)*500)//1
        elif x<=50:
            self.health=(pow(x,1.35)*500)//1
        elif x<=85:
            self.health=(pow(x,1.55)*500)//1
        elif x<=99:
            self.health=(pow(x,1.825)*500)//1
        else :
            self.health=(pow(x,3.75)*500)//1
        return self.health

    def exp_gain(self,amount):
        self.exp+=amount
        self.total_exp_accuired+=amount
        self.levels()

    def get_rank(self):
        x=self.get_lvl()
        current_rank=None 
        if x<=5:
            current_rank="Commoner"
        elif x<=20:
            current_rank="Rookie"
        elif x<=40:
            current_rank="Expert"
        elif x<=60:
            current_rank="Master"
        elif x<=80:
            current_rank="Pseudo Grand Master"
        elif x<=99:
            current_rank="Grand master"
            current_rank
        elif x>99:
            current_rank="God"
        return current_rank

    def elimination_penalty(self):
        pass

class Player(LevelManager):
    def __init__(self,name,heal=0,attack=15,defence=20,abilities=[],super_power=[],items=None,rank="commoner",current_health=500):
        self.name=name
        self.heal=heal
        self.defence=defence
        self.attack=attack
        self.abilities=abilities
        self.super_power=super_power
        self.items=items
        self.__current_health=current_health

        if self.name in game_data["player"]:
            saved = game_data["player"][self.name]
            super().__init__(
                level=saved["level"], 
                exp=saved["exp"], 
                total_exp_accuired=saved["total_exp"], 
                health=saved["health"]
            )
            saved = game_data["player"][self.name]
            self.items = saved.get("items", [])
            self.abilities = saved.get("abilities", [])
            self.rank = saved.get("rank", None)
            self.health=saved.get("health",self.get_health())
            self.__current_health=saved.get("current_health",self.get_health())
        else:
            super().__init__(level=1,exp=0,total_exp_accuired=100,health=500)
            self.player_level=self.get_lvl()
            self.player_exp=self.get_exp()
            self.player_total_exp=self.get_total_exp()
            self.player_health=self.get_health()
            self.rank=self.get_rank()
            self.items=items if items is not None else []
            self.abilities=abilities if abilities is not None else []
            self.super_power=super_power if super_power is not None else []
            self.__current_health=self.get_health()
            
            

    def current_health(self,damage_receive=0):
        if game_data["player"][self.name]["health_lock"]==False:
            self.__current_health-=damage_receive
            game_data["player"][self.name]["current_health"]=self.__current_health

        elif game_data["player"][self.name]["health_lock"]==True:
            if os.name=="nt":
                os.system('cls')
            else:
                os.system('clear')

            for x in range(1,4):
                print("\n\n\n\n\n\n\n"*x)
                print(f"{'Woah!'*x} you are leveling up".center(120))
                time.sleep(2)

                if os.name=="nt":
                    os.system('cls')
                else:
                    os.system('clear')
                
                self.__current_health=self.get_health()

            print(f"Congratulation on leveling up to level : {self.get_lvl()}") 

            game_data["player"][self.name]["health_lock"]=False
        
        if self.__current_health<=0:
            self.__current_health=self.get_health()
            print("U got eliminated as a result your level will get one down and will lose some of your drops ") 
            # self.elimination_penalty() ###### NOT IMPLEMENTED YET 


        return self.__current_health


    def counter_enemy_direction(self):
        a=input("Enter Rignt(R/r) or Left(L/l) to evade the attack : ").lower().strip()
        if a=="r":
            x="right"
        else:
            x="left"
        return x

    def attack_direction(self):  
        a=input("Enter Rignt(R/r) or Left(L/l) to attack : ").lower().strip()
        if a=="r":
            x="right"
        else:
            x="left"
        return x

    def normal_attack_power(self):
        x=self.get_lvl()
        if x<25:
            power=pow(x,1.4)*15
            return power//1
        elif x<50:
            power=pow(x,1.6)*15
            return power//1
        elif x<75:
            power=pow(x,1.8)*15
            return power//1
        elif x<=90:
            power=pow(x,2)*15
            return power//1
        elif x<=99:
            power=pow(x,2.5)*15
            return power//1
        else:
            power=pow(x,3.415)*15
            return power//1


    def super_attack_power(self):
        level=self.get_lvl()
        normal_power=self.normal_attack_power()
        super_atk = (normal_power*(level/1.38))

        if level==1:
            return normal_power
        return round(super_atk,2)

    def defence_(self):
        pass 

    def rank_(self):
        pass

    def damage_receive(self,enemy_type) :
        """name_of_enemy"""
        pass

    

    def update(self):
        game_data["player"].setdefault(self.name, {"exp": 0, "level": 1, "total_exp": 0, "items": [],
    "atk_power": 15, "defence": 20, "health": 500,"boss_defeated": 0, "abilities": [],"super_powers": [],"super_attack_power": 0, "rank": None, "Witch_killed":0, "Mage_killed":0, "Skeleton_killed":0, "Boss_killed":0,"health_lock":False,"current_health":0})
        game_data["player"][self.name]["level"]=self.get_lvl()
        game_data["player"][self.name]["exp"]=self.get_exp()
        game_data["player"][self.name]["health"]=self.get_health()
        game_data["player"][self.name]["total_exp"]=self.get_total_exp()
        game_data["player"][self.name]["atk_power"]=self.normal_attack_power()
        # game_data["player"][self.name]["health_lock"]=False



class Enemy(LevelManager):
    def __init__(self,health=0,heal=0,exp=0,damage=0,defence=0,explosion=0,drop=None):
        self._health=health
        self._heal=heal
        self._exp=exp
        self._damage=damage
        self._defence=defence
        self._explosion=explosion
        self._drop=drop 
        super().__init__(level=1,exp=0,total_exp_accuired=100,health=health)
        self.attacks=self.get_lvl()
        self.healths=self.get_lvl()
    
    def take_damage(self,damage)  : #take damge from user 
        """player_damge_capacity"""
        self._health -= damage 
        if self._health<0:
            self._health=0
        return self._health
    #make separate for individual enemy types
    def attack(self) :
        """u_can_specify_the_level_by_putting_level_value_wanted"""
        power_lvl = self.get_lvl()
        max_raw_power=int((pow(power_lvl,2))//1)
        base_raw_power=int((pow(power_lvl,1.9))//1)
        x=random.randint(base_raw_power,max_raw_power)
        return [x,power_lvl]


    def attack_direction(self):  ## it is used to decide direction of eemy attack and to counter direction """counter_enemy_direction""" function in Player class is been made 
        x=["right","left"]
        a=random.choice(x)
        return a 

    def evade(self): #Only for boss and mages 
        x=["right","left"]
        a=random.choice(x)
        return a 

    def calculate_exp(self,val,damage) :
        """exp_giving_to_user_ and _player_damage_capacity"""
        if self.take_damage(damage)==0:
            self._exp+=val
            return self._exp
        else:
            return self._exp 

    def get_health(self):
        return self._health

    def enemy_health_(self) -> list:
        """u_can_specify_other_levels_also"""
        x=self.get_lvl()
        if x <=25:
            a=(pow(x,1.2)*500)//1
        elif x<=50:
            a=(pow(x,1.35)*500)//1
        elif x<=85:
            a=(pow(x,1.55)*500)//1
        elif x<=99:
            a=(pow(x,1.825)*500)//1
        else :
            a=(pow(x,3.75)*500)//1
        
        enemy_health=pow(a,0.609)

        self._health=enemy_health
        return [float(enemy_health),x]  # to get the level of player also for simultaneus use in some cases like determing the attack for of diiferent enemy classes like defaullt will be for skeleton only
    
#make enemy a parent class or this player as a separate class of its own and bring levelmanager inside as some method 


class Witch(Enemy):
    witch_count=0
    def __init__(self,health=100,heal=0,exp=0,damage=0,defence=0,explosion=0,drop=None):
        super().__init__(health,heal,exp,damage,defence,explosion,drop)
        Witch.witch_count+=1
    
    def __str__(self):
        return str(self)
        
    def enemy_heal(self):  
        x=random.randint(1,15)
        self._heal=x
    
    def enemy_attack(self):
        x=self.attack()
        lvl=x[1]
        attack=x[0]
        increament_value=1+(lvl/100)
        skeleton_power_buff=1.2
        final=(attack*increament_value)*skeleton_power_buff
        return final 
        
    def drops(self):
        self._drop={"curse_stick":{"atk":12,"paralysis":1},"None":"null"}
        x= random.choice(list(self._drop.keys()))
        return [{x:self._drop[x]}]

    def self_health(self):
        x=self.enemy_health_()
        normal=x[0]
        final=normal*1.4
        self._health=final 
        return final

    def update(self):
        game_data["enemies"].setdefault("Witch",{"Witch_count":None,"exp_for_player":None})
        game_data["enemies"]["Witch"]["Witch_count"]=Witch.witch_count
        game_data["enemies"]["Witch"]["exp_for_player"]=self._exp

class Skeleton(Enemy):
    skeleton_count=0
    def __init__(self,health=50,heal=0,exp=0,damage=0,defence=0,explosion=0,drop=None):
        super().__init__(health,heal,exp,damage,defence,explosion,drop)
        Skeleton.skeleton_count+=1
    
    def __str__(self):
        return str(self)

    def enemy_attack(self):
        x=self.attack()
        attack=x[0]
        return attack 
    
    def enemy_defence(self):
        pass

    def self_health(self):
        x=self.enemy_health_()
        normal=x[0]
        final=normal*1.1
        self._health=final 
        return final

    def update(self):
        game_data["enemies"].setdefault("skeleton",{"skeleton_count":None,"exp_for_player":None})
        game_data["enemies"]["skeleton"]["skeleton_count"]=Skeleton.skeleton_count
        game_data["enemies"]["skeleton"]["exp_for_player"]=self._exp

class SkeletonHorde(Skeleton):
    def __init__(self,health=50,heal=0,exp=0,damage=0,defence=0,explosion=0,drop=None):
        super().__init__(health,heal,exp,damage,defence,explosion,drop)

    def __str__(self):
        return str(self)

    def enemy_attack_(self,min_value,max_value):
        hordes=random.randint(min_value,max_value)
        Skeleton.skeleton_count+=hordes
        individual_power=self.enemy_attack()
        horde_attack=hordes*individual_power
        return horde_attack

class Mage(Enemy):
    mage_count=0
    def __init__(self,health=150,heal=0,exp=0,damage=0,defence=0,explosion=0,drop=None):
        super().__init__(health,heal,exp,damage,defence,explosion,drop)
        Mage.mage_count+=1

    def __str__(self):
        return str(self)

    def explosion(self):
        x=random.randint(30,42)
        return x

    def update(self):
        game_data["enemies"].setdefault("mage",{"mage_count":None,"exp_for_player":None})
        game_data["enemies"]["mage"]["mage_count"]=Mage.mage_count
        game_data["enemies"]["mage"]["exp_for_player"]=self._exp

    def enemy_attack(self) : 
        x=self.attack()
        lvl=x[1]
        attack=x[0]
        increament_value=1+(lvl/100)
        mage_power_buff=1.6
        final=(attack*increament_value)*mage_power_buff
        return final 

    def self_health(self):
        x=self.enemy_health_()
        normal=x[0]
        final=normal*1.75
        self._health=final 
        return final

    # def drops(self):
    #     self._drop={"curse_stick":{"atk":12,"paralysis":1},"None":"null"}
    #     x= random.choice(list(self._drop.keys()))
    #     return [{x:self._drop[x]}]

class Boss(Enemy):
    def __init__(self, health=500, heal=0, exp=0, damage=0, defence=0, explosion=0, drop=None):
        super().__init__(health, heal, exp, damage, defence, explosion, drop)
    
    def enemy_attack(self):
        x=self.attack()
        lvl=x[1]
        attack=x[0]
        increament_value=1+(lvl/100)
        boss_power_buff=lvl+0.3
        final=(attack*increament_value)*boss_power_buff
        return final 

    # def drops(self):
    #     self._drop={"curse_stick":{"atk":12,"paralysis":1},"None":"null"}
    #     x= random.choice(list(self._drop.keys()))
    #     return [{x:self._drop[x]}]





if __name__=="__main__":
    pass
