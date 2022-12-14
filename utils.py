from operator import index
from bs4 import BeautifulSoup
import requests 
import json
from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')

result = {
}

index = open("index.json")
data = json.load(index)

# print(data)

def get_data(name) :

    source=requests.get(data[name]["link"])
    soup = BeautifulSoup(source.text, 'lxml')
    price_div= soup.find('div', class_='stickymcont')
    price= price_div.find('div', class_='pcstkspr nsestkcp bsestkcp futstkcp optstkcp')
    result["price"] = price.text
    # nseopen=soup.find('td', class_='nseprvclose')

    # calc=(float(price.text)-float(nseopen.text))/float(nseopen.text)*100

    # print(round(calc,2))

    price_change_div = price_div.find('div', class_="advdecl")
    entire = price_change_div.text.replace("("," ").replace(")","")
    points = entire.split(" ")[0]
    change = entire.split(" ")[1]

    result["points"] = points
    result["change"] = change
    result["up_down"] = "down" if ("-" in change) else "up"

    datetime_ist = datetime.now(IST)

    result["time"] = datetime_ist.strftime('%H:%M:%S')

    return (result)

def get_price(name) :
    data = get_data(name)
    return data["price"]

def get_change(name) :
    data = get_data(name)
    return data["change"]

def get_points(name) :
    data = get_data(name)
    return data["points"]

def get_up_down(name) :
    data = get_data(name)
    return data["up_down"]

def get_time():
    datetime_ist = datetime.now(IST)
    return datetime_ist.strftime('%H:%M:%S')