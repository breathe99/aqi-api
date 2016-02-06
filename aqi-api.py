from flask import Flask
from flask import jsonify
from datetime import datetime
import dryscrape

app = Flask(__name__)

site = "http://aqicn.org/city/"
data = {"beijing":-1, "shanghai":-1, "hongkong":-1, "bangkok":-1, "delhi":-1,
       "mumbai":-1, "tokyo":-1, "seoul":-1, "manila":-1, "guangzhou":-1}
response = None
last_fetch = None

dryscrape.start_xvfb()
sess = dryscrape.Session(base_url = site)
sess.set_attribute('auto_load_images', False)

def fetch():
    print("fetching...")
    global last_fetch, data, response
    last_fetch = datetime.now()
    
    for city in data.keys():
        sess.visit(city + '/m')
        ele = sess.at_xpath('//*[@id="xatzcaqv"]')
        data[city] = ele.text()
        print(city + ": " + data[city])
    
    data["time"] = str(datetime.now())
    response = jsonify(data)

def need_fetch():
    if(last_fetch == None): return True # initial fetch
    print(str(last_fetch))
    return (datetime.now() - last_fetch).total_seconds() > 3600 # > 1 hour

def get_data():
    if(need_fetch()):
        fetch()

    return response

@app.route("/aqi")
def aqi():
    return get_data()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
