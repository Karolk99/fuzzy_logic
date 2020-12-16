import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

speed = ctrl.Antecedent(np.arange(0, 100, 1), 'speed')
weather = ctrl.Antecedent(np.arange(0, 100, 1), 'weather')
visibility = ctrl.Antecedent(np.arange(0, 100, 1), 'visibility')
# road = np.arange(0, 100, 1)
acc = ctrl.Consequent(np.arange(0, 100, 1), 'acc')

speed.automf(3)

weather['rain'] = fuzz.trimf(weather.universe, [0, 0, 75])
weather['sun'] = fuzz.trimf(weather.universe, [0, 100, 100])

visibility['bad'] = fuzz.trimf(visibility.universe, [0, 0, 75])
visibility['good'] = fuzz.trimf(visibility.universe, [0, 100, 100])

# road['slow'] = fuzz.trimf(road, [0, 0, 75])
# road['fast'] = fuzz.trimf(road, [25, 100, 100])

acc['slow_down'] = fuzz.trimf(acc.universe, [0, 0, 50])  
acc['keep'] = fuzz.trimf(acc.universe, [0, 50, 100])
acc['accelerate'] = fuzz.trimf(acc.universe, [50, 100, 100])

rule = []

rule.append(ctrl.Rule(speed['poor'] & weather['rain'] & visibility['bad'], acc['keep']))
rule.append(ctrl.Rule(speed['poor'] & weather['rain'] & visibility['good'], acc['accelerate']))
rule.append(ctrl.Rule(speed['poor'] & weather['sun'] & visibility['bad'], acc['accelerate']))
rule.append(ctrl.Rule(speed['poor'] & weather['sun'] & visibility['good'], acc['accelerate']))

rule.append(ctrl.Rule(speed['average'] & weather['rain'] & visibility['bad'], acc['slow_down']))
rule.append(ctrl.Rule(speed['average'] & weather['rain'] & visibility['good'], acc['keep']))
rule.append(ctrl.Rule(speed['average'] & weather['sun'] & visibility['bad'], acc['keep']))
rule.append(ctrl.Rule(speed['average'] & weather['sun'] & visibility['good'], acc['accelerate']))

rule.append(ctrl.Rule(speed['good'] & weather['rain'] & visibility['bad'], acc['slow_down']))
rule.append(ctrl.Rule(speed['good'] & weather['rain'] & visibility['good'], acc['slow_down']))
rule.append(ctrl.Rule(speed['good'] & weather['sun'] & visibility['bad'], acc['slow_down']))
rule.append(ctrl.Rule(speed['good'] & weather['sun'] & visibility['good'], acc['keep']))

acc_ctrl = ctrl.ControlSystem(rule)

acceleration = ctrl.ControlSystemSimulation(acc_ctrl)

# acceleration.input['speed'] = 100
# acceleration.input['weather'] = 0
# acceleration.input['visibility'] = 0

# acceleration.compute()

# print(acceleration.output['acc'])
# acc.view(sim=acceleration)