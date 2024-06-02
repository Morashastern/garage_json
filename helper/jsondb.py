
import json


filename='cars.json'
def load_cars(filename):
    from app import Car

    try:
        with open(filename,'r') as file:
          data = json.load(file)
          print(data)
        return [Car(c['model'], c['color'], c['brand']) for c in data]
    except FileNotFoundError:
        print(f'create new file:{filename}')
        return []
def display_cars(cars):
   for index, car in enumerate(cars):
        print(f'{index+1} - {car}')


def save_cars_to_json(cars):
    from app import car_to_dict
    cars_dict=[car_to_dict(c) for c in cars]
    with open('cars.json','w') as file:
        json.dump(cars_dict,file,indent=4)
