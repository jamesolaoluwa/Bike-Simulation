class BikeSimulation:
    def __init__(self, brand, model, color, year, speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.speed = speed
        self.is_running = False
        self.current_gear = "neutral"
        self.nitro_engaged = False
        self.speedometer = 0

    def start(self):
        if not self.is_running:
            print(f'The {self.color} {self.brand} {self.model} {self.year} has started')
            self.is_running = True
        else:
            print(f'The {self.color} {self.brand} {self.model} {self.year} is already running')

    def change_gear(self):
        if self.is_running:
            option = input('Enter gear option [neutral, low gear, high gear]: ')
            if option == 'neutral':
                self.current_gear = "neutral"
                print(f'The {self.color} {self.brand} {self.model} {self.year} gear has been switched to neutral')
            elif option == 'low gear':
                self.current_gear = "low gear"
                print(f'The {self.color} {self.brand} {self.model} {self.year} gear has been switched to low gear')
            elif option == 'high gear':
                self.current_gear = "high gear"
                print(f'The {self.color} {self.brand} {self.model} {self.year} gear has been switched to high gear')
            else:
                print('Invalid gear option')
        else:
            print(f'The {self.color} {self.brand} {self.model} {self.year} is not running')

    def accelerate(self):
        if self.is_running:
            if self.current_gear == "neutral":
                print(f'Cannot accelerate in neutral gear')
            else:
                option = input('Enter Acceleration Option [yes, no]: ')
                if option == 'yes':
                    self.speedometer += 10
                    print(f'The {self.color} {self.brand} {self.model} {self.year} is accelerating')
                    if self.nitro_engaged:
                        self.speedometer += 20
                        print(f'Nitro boost activated! Speed increased.')
                elif option == 'no':
                    print(f'The {self.color} {self.brand} {self.model} {self.year} has stopped accelerating')
                else:
                    print('Invalid option for acceleration')
        else:
            print(f'The {self.color} {self.brand} {self.model} {self.year} is not running')

    def engage_nitro(self):
        if self.is_running:
            if self.nitro_engaged:
                print(f'Nitro is already engaged')
            else:
                self.nitro_engaged = True
                print(f'Nitro has been engaged on the {self.color} {self.brand} {self.model} {self.year}')
        else:
            print(f'The {self.color} {self.brand} {self.model} {self.year} is not running')

    def disengage_nitro(self):
        if self.is_running:
            if self.nitro_engaged:
                self.nitro_engaged = False
                print(f'Nitro has been disengaged on the {self.color} {self.brand} {self.model} {self.year}')
            else:
                print(f'Nitro is already disengaged')
        else:
            print(f'The {self.color} {self.brand} {self.model} {self.year} is not running')

    def stop(self):
        if self.is_running:
            print(f'The {self.color} {self.brand} {self.model} {self.year} has stopped')
            self.is_running = False
            self.current_gear = "neutral"
            self.nitro_engaged = False
            self.speedometer = 0
        else:
            print(f'The {self.color} {self.brand} {self.model} {self.year} is already stopped')


bike1 = BikeSimulation('Aprilla', 'CB1', 'Red', 2009, 250)

bike1.start()
bike1.change_gear()
bike1.accelerate()
bike1.engage_nitro()
bike1.accelerate()
bike1.disengage_nitro()
bike1.accelerate()
bike1.stop()
