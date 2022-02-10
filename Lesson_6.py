from time import sleep

class TrafficLight:

    # все созданные светофоры друг от друга не зависят
    def __init__(self):
            self.__color = 'red'

    def running(self):
        if self.__color == 'red':
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            self.__color = 'green'
            sleep(5)




TL = TrafficLight()
print(TL._TrafficLight__color)
TL.running()

print(TL._TrafficLight__color)

TL.running()
print(TL._TrafficLight__color)


