
from helper.jsondb import save_cars_to_json,filename,load_cars,display_cars
def add_car(cars):
    from app import Car

    temp_car= Car(input("model"),
                  input("color"),
                  input("brand"))
    cars.append(temp_car)
    save_cars_to_json(cars)
    
    

def delete_car(cars):
      display_cars(cars)
      del_car=int(input("enter car number to delete:"))
      cars.pop(del_car-1)
      save_cars_to_json(cars)


def reset_cars(cars):
     cars=[]
     save_cars_to_json(cars)

     
def sum_cars(cars):
   sum_list=len(cars)
   print(f'There is {sum_list} cars in the garage.')

    
     
     

def updat_car(cars):
    from app import Car
    display_cars(cars)
    upd_car=int(input("enter car number to update:"))
    cars[upd_car-1]=Car(input('model'),input('color'),input('brand'))
    save_cars_to_json(cars)
     
     



