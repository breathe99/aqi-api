from flask import Flask
from bs4 import BeautifulSoup
import urllib

app = Flask(__name__)

site = "http://aqicn.org/city/"
cities = ["beijing", "shanghai", "hongkong", "bangkok", "delhi", "mumbai",
          "tokyo", "seoul", "manila", "guangzhou"]
aqi = {"beijing":-1, "shanghai":-1, "hongkong":-1, "bangkok":-1, "delhi":-1,
       "mumbai":-1, "tokyo":-1, "seoul":-1, "manila":-1, "guangzhou":-1}

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/aqi")
def fetch():
#    for city in cities:
#        page = requests.get(site+city)
#        tree = html.fromstring(page.content)
#        aqis = tree.xpath('//*[@id="citydivmain"]/div/div/div/table[2]/tbody/tr/td[1]/div')
#        print("{} aqi: {}".format(city, aqis))
    url = "http://aqicn.org/city/beijing/m/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "lxml")
#    print(soup.get_text().encode('utf-8'))
    div = soup.find("div", {"id":"articlebody"})
    print(div.get_text())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
