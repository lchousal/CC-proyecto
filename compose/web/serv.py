import os
from flask import Flask, request, redirect,url_for, render_template,json ,jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

partiturasList= {}
partiturasList['partituras'] = []
path_vol = '/servicio/datos'

@app.route('/', methods = ['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      filepath = os.path.join(path_vol, filename)
      f.save(filepath)

      part = filename.split("_",2)
      partitura = {
          'autor': part[0],
          'titulo': part[1]}
      partiturasList['partituras'].append(partitura)

      with open('datos.json', 'w') as p:
          aux = json.dump(partiturasList,p)
      return redirect(url_for('partituras'))
    return render_template('inicio.html')

@app.route('/partituras', methods = ['GET'])
def partituras():
    p = open('datos.json', 'r')
    pString = json.load(p)
    return jsonify(pString)

@app.route('/status/')
def estadoOk():
    return jsonify({'status':'OK'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
