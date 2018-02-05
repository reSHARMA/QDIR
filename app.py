from flask import Flask, request, render_template, url_for, json,Response,redirect
import os
import pickle
import numpy as np
app = Flask(__name__)
@app.route('/')
def test():
        return render_template('main.html')
@app.route('/data.json',methods = ["GET"])
def data():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT,"templates", "data.json")
        return Response(open(json_url).read(),mimetype="json")
@app.route('/submit', methods = ['POST'])
def get_delay():
    print(request.method)
    if request.method == "POST":
        data = request.values
        link = data['qlink']
        pri = data['pri']
        diff = data['diff']
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT,"templates", "data.json")
        data = json.load(open(json_url))
        temp = {}
        temp['qlink'] = "<a href='" + str(link) + "'>"+ link +"</a>"
        temp['pri'] = pri
        temp['diff'] = diff
        data.append(temp)
        print(data)
        with open(json_url, 'w') as outfile:
                json.dump(data, outfile)
        return redirect('/')

if __name__ == '__main__':
	app.run()
