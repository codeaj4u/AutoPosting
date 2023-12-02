from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'rajakshat7985@gmail.com'
app.config['MAIL_PASSWORD'] = "ogeoymardylmaksb"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route("/")
def index():
    return render_template('contacts.html')


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form['user_name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']


        msg = Message(subject, sender=email, recipients= ['rajakshat7985@gmail.com','codeaj4u@gmail.com'])
        msg.body = message
        mail.send(msg)
        return "Message Sent"


    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug= True)
    
