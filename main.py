from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    reenter_password = request.form['reenter']
    email = request.form['email']

    username_error = ""
    password_error = ""
    reenter_error = ""
    email_error = ""

    if not username or " " in username or len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"

    if email != "" and (email.count(".") != 1 or email.count("@") !=1 or " " in email or len(email) < 3 or len(email) > 20):
            email_error = "That's not a valid email"
    
    if not password or " " in password or len(password) < 3 or len(password) > 20 or password != reenter_password:
        password_error = "That's not a valid password"
        reenter_error = "Passwords do not match"
        password = ""
        reenter_password = ""
    
    elif password == reenter_password and (" " in password or len(password) < 3 or len(password) > 20) :
        password_error = "That's not a valid password"
        password = ""
        reenter_password = ""

    if username_error or email_error:
        password = ""
        reenter_password = ""
    
    if username_error or password_error or reenter_error or email_error:
        return render_template('home.html', username=username, username_error=username_error, password=password,
        password_error=password_error, reenter_password=reenter_password, reenter_error=reenter_error, email=email,
        email_error=email_error)
    else:
        return redirect('/welcome?username={0}'.format(username))

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()