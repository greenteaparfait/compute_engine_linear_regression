from flask import Flask, request, jsonify
from scipy import stats
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        timeData = request.json['time']
        sensorData = request.json['timeDomain']
        
        timeArray = np.asarray(timeData)
        sensorArray = np.asarray(sensorData)
        
        sl, inter, r_value, p_value, std_err = stats.linregress(timeArray, sensorArray)
        
        return jsonify(slope = str(sl), intercept = str(inter) )
            
    else:
        return "<h1> This is Index Page</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
