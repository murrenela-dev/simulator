class Car:
    name = 'difaulte'
    power = 2.4
    fuel = 'diesel'
    gear_box = 'automatic'
    work = False
    color = 'red'

    def start_engine(self):
        self.work = True

    def stop_engine(self):
        self.work = False


kia = Car()
kia.name = 'kia'
print(kia.name)
print(kia.work)
kia.start_engine()
print(kia.work)



