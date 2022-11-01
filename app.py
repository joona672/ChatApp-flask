


from flask import Flask , render_template, request , send_file




viestit = []



app = Flask(__name__, template_folder='template')

    
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/send', methods = ['POST'])
def new_message():
    
    content_type = request.headers.get('Content-Type')
    
    if content_type == 'application/json':
        js = request.json
    # print(user_name)
    # print(name)
    
        viestit.append(js)
        
    else:
        #name = request.args['username']
        user_name = request.form['username']
        aika = request.form['time']
        viesti = request.form['message']
        data = {"message":viesti, "username":user_name, "time":aika}
        viestit.append(data)
        
    
    return f'{True}'

@app.route('/update')
def update():
    if len(viestit) > 100:
        viestit.pop(0)
    
    return viestit


@app.route('/owl')
def send_image():
    return send_file("owl.png" ,mimetype='image/gif')
