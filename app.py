import platform
import os
import docker
import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify("Hello, World")
    
@app.route("/server-info")
def os_info():
    try:
        uname = platform.uname()
        dateTime = datetime.datetime.now().isoformat()
        
        data_dict = {"Hostname": uname.node, "Timestamp": dateTime}
        return jsonify(data_dict)
    
    except OSError as e:
        return jsonify({"ERROR": f"Docker Error: {str(e)}"}), 500


@app.route("/faktorial", methods=['POST'])
def hitung_faktorial(): 
    try:
       
        data = request.get_json()
        n = data.get("angka")
        
        if n is None or not isinstance(n, int) or n < 0:
            return jsonify({"ERROR": "Masukan angka bulat positif"}), 400
        
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i
            
        return jsonify({"angka": n, "faktorial": hasil}), 200
    except Exception as e:
        return jsonify({"ERROR": str(e)}), 500
            

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')