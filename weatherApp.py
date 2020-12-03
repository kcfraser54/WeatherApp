import tkinter as tk
import requests
HEIGHT = 500
WIDTH = 600


def get_weather(latitude, longitude):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

    querystring = {"lat": latitude, "lon": longitude}


    headers = {
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
        'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    
    weather = response.json()

    timezone = weather['data'][0]['timezone']
    country_code = weather['data'][0]['country_code']
    state_code = weather['data'][0]['state_code']
    city_name = weather['data'][0]['city_name']
    desc = weather['data'][0]['weather']['description']
    temp = weather['data'][0]['temp']
    label['text'] = timezone + '\n' + country_code + '\n' + state_code + '\n' + city_name + '\n' + desc + '\n' + str(temp) + ' deg. celsius'


root = tk.Tk()
root.title('Weather App')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg='navy')
canvas.pack()

background_image = tk.PhotoImage(file='lifegoal7107313201158887620.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='orange', bd=5)
frame.place(relx=0.5, rely=0.05,relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg='white', font=40)
entry.place(relwidth=1, relheight= 1)

button = tk.Button(root, text="Get Weather", font=40, command=lambda: get_weather(entry.get(), entry2.get()))
button.place(relx=0.4,rely=0.35, relwidth=.2, relheight=0.1)

middle_frame = tk.Frame(root, bg='orange', bd=5)
middle_frame.place(relx = .5, rely=.2, relwidth=.75, relheight=0.1, anchor='n')

entry2 = tk.Entry(middle_frame,bg='white', font=40)
entry2.place(relwidth=1, relheight= 1)

lower_frame = tk.Frame(root, bg='orange', bd=10)
lower_frame.place(relx=.5, rely=0.5, relwidth=0.75, relheight=0.4, anchor='n')

label= tk.Label(lower_frame, bg='white')
label.place(relwidth=1, relheight=1)

root.mainloop()
