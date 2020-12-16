import tkinter as tk
import driver as dr
from PIL import Image, ImageTk

driver = dr.Driver(20, 20, 20)


def change_weather():
    weather = int(ent_weather.get())
    if weather < 0 or weather > 100:
        print('zla wartosc')
        return
    driver.set_weather(weather)
    print(f'weather: { weather }')


def change_visibility():
    visibility = int(ent_visibility.get())
    if visibility < 0 or visibility > 100:
        print('zła wartość')
        return
    driver.set_visibility(visibility)
    print(f'visibilty: { visibility }')

def update_speed():
    lbl_speed['text'] = f'Current speed: { driver.get_speed() }'


window = tk.Tk()
window.title('Fuzzy logic simulator')

weather_entry = tk.Frame(master=window)
ent_weather = tk.Entry(master=weather_entry, width=10)
lbl_weather = tk.Label(master=weather_entry, text='Weather')

ent_weather.grid(row=0, column=0, sticky='e')
lbl_weather.grid(row=0, column=1, sticky='w')

btn_weather = tk.Button(
    master=window,
    text="Apply",
    command=change_weather
)


weather_entry.grid(row=0, column=0, padx=10)
btn_weather.grid(row=0, column=1, pady=10)

visibility_entry = tk.Frame(master=window)
ent_visibility = tk.Entry(master=visibility_entry, width=10)
lbl_visibility = tk.Label(master=visibility_entry, text='Visibility')

ent_visibility.grid(row=1, column=0, sticky='e')
lbl_visibility.grid(row=1, column=1, sticky='w')

btn_visibility = tk.Button(
    master=window,
    text="Apply",
    command=change_visibility
)

visibility_entry.grid(row=1, column=0, padx=10)
btn_visibility.grid(row=1, column=1, pady=10)

speed_entry = tk.Frame(master=window)
lbl_speed = tk.Label(master=speed_entry, text=f'Current speed: { driver.get_speed() }')

lbl_speed.grid()
speed_entry.grid(row=2)

photo = Image.open('fiat.png')
photo = photo.resize((200, 120), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)

# car_entry = tk.Frame(master=window, width=400, height=400)
# car_entry.grid(row=2, columns=1)

canvas = tk.Canvas(master=window, width=400, height=400)
car = canvas.create_image( 
    250, 200,
    image=photo
)

canvas.grid(row=3, column=0)


while True:
    driver.do_one_step()
    update_speed()
    window.update_idletasks()
    window.update()
    dr.time.sleep(0.5)
