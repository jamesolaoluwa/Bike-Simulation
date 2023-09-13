class bikesimulation():
    def __init__(self,brand,model,color,year,speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.speed = speed
        
    def start(self):
        print(f' The {self.color} {self.brand} {self.model} {self.year} has started' )
        
    def changegear(self):
        option = input('Enter gear option [low gear or high gear]: ')
        if option == 'low gear':
            print(f' The {self.color} {self.brand} {self.model} {self.year} gear has been switched to low gear')
        elif option == 'high gear':
            print(f' The {self.color} {self.brand} {self.model} {self.year} gear has been switched to high gear')
            
    def accelerate(self):
        option = input('Enter Acceleration Option [yes, no]: ')
        if option == 'yes':
            print(f' The {self.color} {self.brand} {self.model} {self.year} nitro has been engaged')
        elif option == 'no':
            print(f' The {self.color} {self.brand} {self.model} {self.year} nitro has been disengaged')
            
    def stop(self):
        print(f'The {self.color} {self.brand} {self.model} {self.year} has stopped')
        
bike1 = bikesimulation('Aprilla','CB1','Red',2009,250)

bike1.start()
bike1.changegear()
bike1.accelerate()
bike1.stop()