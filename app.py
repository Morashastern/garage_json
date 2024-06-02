import json
from enum import Enum
from helper.actions import add_car,delete_car,reset_cars,sum_cars,updat_car
from helper.jsondb import load_cars,display_cars,save_cars_to_json

filename='cars.json'

class Menu(Enum):
    ADD=1
    DELETE=2
    UPDATE=3
    PRINT=4
    SUM=5
    RESET=6
    EXIT=7

class Car:
    def __init__(self,model=0,color="",brand="") -> None:
        self.model=model
        self.color=color
        self.brand=brand
    
    def __str__(self) -> str:
        return f"Color: {self.model}, Type: {self.color}, Model: {self.brand}"


def car_to_dict(car_obj):  
        return{'model':car_obj.model,
                 'color':car_obj.color,
                 'brand':car_obj.brand}



def display_menu():
    for action in Menu:
        print (f'{action.value}-{action.name}')
    return Menu(int(input("choose one option:")))
    


def main():
    while True:
        cars=load_cars(filename)
        user_choice=display_menu()
        try:
            if user_choice==Menu.ADD:add_car(cars)            
            if user_choice==Menu.DELETE:delete_car(cars)
            if user_choice==Menu.PRINT:display_cars(cars)
            if user_choice==Menu.RESET:reset_cars(cars)
            if user_choice==Menu.SUM:sum_cars(cars) 
            if user_choice==Menu.UPDATE:updat_car(cars)
            if user_choice==Menu.EXIT:save_cars_to_json(cars),exit()
             

        except Exception as e:
            print("error",e)




if __name__=='__main__':
    main()


