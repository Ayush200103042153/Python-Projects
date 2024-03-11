from tkinter import *
from tkinter import ttk
import requests


def get_data():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3ebcbe0c6169c5ee88e8ee485913b44c").json()
    
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp1.config(text=str(int(data["main"]["temp"]-273.5)))
    per_label1.config(text=data["main"]["pressure"])


win=Tk()
win.title=("Weather Forecast")
win.config(bg="blue")
win.geometry("500x570")


name_label=Label(win,text="Weather Forecast",
                 font=("Time New Roman",25,"bold"))
name_label.place(x=25,y=50,height=50,width=450)


list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name=StringVar()
com=ttk.Combobox(win,text="Weather Forecast",values=list_name,
                 font=("Time New Roman",20),textvariable=city_name)
com.place(x=25,y=120,height=40,width=450)


done_button=Button(win,text="Done",
                   font=("Time New Roman",20),command=get_data)
done_button.place(x=200,y=190,height=50,width=100)


w_label=Label(win,text="Weather Climate",
              font=("Time New Roman",18))
w_label.place(x=25,y=260,height=50,width=210)
w_label1=Label(win,text="",
               font=("Time New Roman",20)) 
w_label1.place(x=250,y=260,height=50,width=210)


wb_label=Label(win,text="Weather Description",
               font=("Time New Roman",15))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1=Label(win,text="",
          font=("Time New Roman",20)) 
wb_label1.place(x=250,y=330,height=50,width=210)


temp=Label(win,text="Temperature",
           font=("Time New Roman",20))
temp.place(x=25,y=400,height=50,width=210)
temp1=Label(win,text="",
            font=("Time New Roman",20)) 
temp1.place(x=250,y=400,height=50,width=210)


per_label=Label(win,text="Pressure",
                font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)
per_label1=Label(win,text="",
                 font=("Time New Roman",20)) 
per_label1.place(x=250,y=470,height=50,width=210)


win.mainloop()