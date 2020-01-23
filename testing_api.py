import json
import requests
from tkinter import *


def weather_report():
	city=e.get()
	response = requests.get("https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(city))
	t=response.json()['main']['temp']
	e.delete(0,END)
	e.insert(0,t)


if __name__=='__main__':
	root=Tk()
	root.title("Weather App")
	root.geometry("300x250")
	e=Entry(root,borderwidth='5')
	e.place(x=50,y=50)
	button=Button(root,text="Check",command=weather_report).place(x=100,y=100)
	root.resizable(0,0)
	root.mainloop()