# Определяем класс для автомобиля
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


# Создаем два объекта автомобиля
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Объединяем их в массив
cars = [car1, car2]


# Функция для фильтрации автомобилей по году выпуска
def filter_cars_by_year(cars, year):
    return [car for car in cars if car.year >= year]


# Фильтруем массив по году выпуска (например, 2020)
filtered_cars = filter_cars_by_year(cars, 2020)

# Выводим отфильтрованные автомобили
for car in filtered_cars:
    print(f"{car.brand} {car.model} ({car.year})")
