import time 
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import fuzzy_logic2 as fuzzy

class Driver:
    def __init__(self, speed, weather, visibility):
        self.speed = speed
        self.weather = weather
        self.visibility = visibility
        self.run = True

        self.controler = fuzzy.acceleration

        self.controler.input['speed'] = self.speed
        self.controler.input['weather'] = self.weather
        self.controler.input['visibility'] = self.visibility

    
    def run_simulation(self):
        
        while self.run:
            self.controler.compute()
            self.compute_speed()
            self.controler.input['speed'] = self.speed
        
            #time.sleep(0.5)

            # print(self.speed + 30)


    def do_one_step(self):
        
        self.controler.compute()
        self.compute_speed()
        self.controler.input['speed'] = self.speed
        
    
    def compute_speed(self):
    
        self.speed = self.speed + (self.controler.output['acc'] - 50) / 10 
        self.controler.input['speed'] = self.speed

    def get_speed(self):
        return "{:.2f}".format(self.speed + 30)

    def set_weather(self, weather):
        self.controler.input['weather'] = weather

    def set_visibility(self, visibility):
        self.controler.input['visibility'] = visibility


if __name__ == '__main__':
    driver = Driver(20, 100, 100)
    driver.run_simulation()
