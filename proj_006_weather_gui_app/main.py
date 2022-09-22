from tkinter import Tk, Label, Button, Entry, END
import requests

API_KEY = "58a3b8d841836ab66b729355f6668a6c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

root = Tk()
root.title('Weather App')
root.geometry('305x210+500+300')

def deg_to_compass(degrees: int) -> str:
    val=int((degrees/45)+.5)
    arr=["С","СВ","В","ЮВ","Ю","ЮЗ","З","СЗ"]
    return arr[(val % 8)]

def get_data() -> None:
    city = input_field.get()
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&lang=ru&units=metric"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = int(data['main']['temp'])
        wind = data['wind']['speed']
        wind_degrees = data['wind']['deg']
        humidity = data['main']['humidity']
        weather_value_label.config(text=weather)
        temperature_value_label.config(text=f'{temp}°C')
        wind_value_label.config(text=f'{wind} м/с {deg_to_compass(wind_degrees)}')
        humidity_value_label.config(text=f'{humidity}%')
    else:
        print("An error occured")

def reset() -> None:
    weather_value_label.config(text=' ')
    temperature_value_label.config(text=' ')
    wind_value_label.config(text=' ')
    humidity_value_label.config(text=' ')

def clear() -> None:
    input_field.delete(0, END)

# inputs
input_field = Entry(root, width=30, borderwidth=5)

# buttons
send_button = Button(root, text='Send', command=get_data)
clear_button = Button(root, text='Clear', command=clear)
quit_button = Button(root, text='Quit', command=root.quit)
reset_button = Button(root, text='Reset', command=reset)

# labels
title_label = Label(root, text='Enter city name:')
weather_label = Label(root, text='Погода')
temperature_label = Label(root, text='Температура')
wind_label = Label(root, text='Ветер')
humidity_label = Label(root, text='Влажность')

weather_value_label = Label(root, text=' ')
temperature_value_label = Label(root, text=' ')
wind_value_label = Label(root, text=' ')
humidity_value_label = Label(root, text=' ')

# place the widgets in the window
title_label.place(x=5, y=5)
input_field.place(x=5, y=30)
send_button.place(x=5, y=65)
clear_button.place(x=75, y=65)
weather_label.place(x=5, y=95)
weather_value_label.place(x=115, y=95)
temperature_label.place(x=5, y=115)
temperature_value_label.place(x=115, y=115)
wind_label.place(x=5, y=135)
wind_value_label.place(x=115, y=135)
humidity_label.place(x=5, y=155)
humidity_value_label.place(x=115, y=155)
reset_button.place(x=5, y=175)
quit_button.place(x=243, y=175)

root.mainloop()
