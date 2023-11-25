import requests
import json
if __name__ == '__main__':
    city=input("Enter the name of the city : ")
    try:
        url=f"https://api.weatherapi.com/v1/current.json?key=199a36de13cf47458b900106221602&q={city}"
        r=requests.get(url)
        Weather_dic=json.loads(r.text)
        print(Weather_dic['current']['temp_c'])
    except:
        print("City Name Was not correct")
