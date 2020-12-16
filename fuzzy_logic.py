import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

speed = np.arange(0, 100, 1)
weather = np.arange(0, 100, 1)
visibility = np.arange(0, 100, 1)
road = np.arange(0, 100, 1)
acc = np.arange(-50, 50, 1)

speed_l = fuzz.trimf(speed, [0, 0, 50])  #low
speed_m = fuzz.trimf(speed, [0, 50, 100])  #medium
speed_h = fuzz.trimf(speed, [50, 100, 100])  #high

weather_s = fuzz.trimf(x_weather, [0, 0, 75])  #sunny
weather_r = fuzz.trimf(x_weather, [25, 100, 100])  #raining

visibility_b = fuzz.trimf(x_weather, [0, 0, 75])  #bad
visibility_g = fuzz.trimf(x_weather, [25, 100, 100])  #good

road_s = fuzz.trimf(x_weather, [0, 0, 75])  #slow
road_f = fuzz.trimf(x_weather, [25, 100, 100])  #fast

acc_s = fuzz.trimf(x_speed, [-50, -50, 0])  #slow down 
acc_k = fuzz.trimf(x_speed, [-50, 0, 50])  #keep
acc_a = fuzz.trimf(x_speed, [0, 50, 50])  #accelerate

if __name__ == "__main__":
    fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, figsize=(8, 9))
    
    ax0.plot(x_speed, speed_l, 'b', linewidth=1.5, label="Slow")
    ax0.plot(x_speed, speed_m, 'g', linewidth=1.5, label="Medium")
    ax0.plot(x_speed, speed_h, 'h', linewidth=1.5, label="High")
    ax0.set_title("Speed")
    ax0.legend()

    ax1.plot(x_weather, weather_s, 'b', linewidth=1.5, label='Sunny')
    ax1.plot(x_weather, weather_r, 'g', linewidth=1.5, label='Raining')
    ax1.set_title('Weather')
    ax1.legend()

    ax2.plot(x_visibility, visibility_b, 'b', linewidth=1.5, label='Bad')
    ax2.plot(x_visibility, visibility_g, 'g', linewidth=1.5, label='Good')
    ax2.set_title('Visibility')
    ax2.legend()

    ax3.plot(x_road, road_s, 'b', linewidth=1.5, label='Slow')
    ax3.plot(x_road, road_f, 'g', linewidth=1.5, label='Fast')
    ax3.set_title('Road')
    ax3.legend()

    ax4.plot(x_acc, acc_s, 'b', linewidth=1.5, label="Slow down")
    ax4.plot(x_acc, acc_k, 'g', linewidth=1.5, label="Keep")
    ax4.plot(x_acc, acc_a, 'h', linewidth=1.5, label="Accelerate")
    ax4.set_title("Acceleration")
    ax4.legend()


    for ax in (ax0, ax1, ax2, ax3, ax4):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    plt.tight_layout()
    