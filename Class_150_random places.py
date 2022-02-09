from tkinter import *
import random

root= Tk()
root.title("Random Countries And Cities")
root.geometry("500x500")
root.configure(background = "snow")

enter_country = Entry(root)
enter_country.place(relx=0.5,rely=0.2,anchor=CENTER)

enter_city = Entry(root)
enter_city.place(relx=0.5,rely=0.3,anchor=CENTER)

country=Label(root)
city=Label(root)
random_country = Label(root)
random_city = Label(root)


list1=[]
list2=[]
def  addPlace() : 
    country1 = enter_country.get()
    city1 = enter_city.get()
    list1.append(country1)
    list2.append(city1)
    random_country["text"]  = "Countries : " + str(list1)
    random_city["text"]    = "City : " + str(list2)


def random_number1() :
    length1= len(list1)
    length2 = len(list2)
    random_no1 = random.randint(0, length1-1)
    random_no2 = random.randint(0, length2-1)
    country_name = list1[random_no1]
    city_name = list2[random_no2]
    country["text"] = "Chosen Country : " + str(country_name)
    city["text"] = "Chosen City : " + str(city_name)
    

btn=Button(root, text = "Save Country & City", command = addPlace)
btn.place(relx=0.5, rely=0.4,anchor = CENTER)
btn1 = Button(root,text = "Display Random Country & City", command = random_number1)
btn1.place(relx=0.5, rely=0.7,anchor = CENTER)
    
random_country.place(relx=0.5, rely=0.5,anchor = CENTER)
random_city.place(relx=0.5, rely=0.6,anchor = CENTER)
country.place(relx=0.5, rely=0.8,anchor = CENTER)
city.place(relx=0.5, rely=0.9,anchor = CENTER)

root.mainloop()