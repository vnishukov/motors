# -*- coding: utf-8 -*- 

from flask import Flask, render_template, request, url_for, redirect, flash
import pylib
import datetime

app = Flask(__name__)
# Create dummy secrey key so we can use sessions
app.secret_key = pylib.get_random_uuid()

@app.route('/')
def webprint():
    return render_template('index.html') 

@app.route('/req', methods=['POST'])
def customer_request():
    print request.form
    model = request.form['model'].encode('utf-8')
    vin = request.form['vin'].encode('utf-8')
    tel = request.form['tel'].encode('utf-8')
    message = "Сообщение отослано. модель={}  vin={}  тел={}".format(model, vin, tel)
    email_message = "Bремя заявки={}\nМодель={}\nVIN={}\nТелефон={}\n".format(
        datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S"),
        model, vin, tel)
    subj = "Заявка с сайта bymotor.ru"
    flash (message)
    pylib.send_email(subj, email_message)
    return redirect(url_for('webprint'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug=True)

