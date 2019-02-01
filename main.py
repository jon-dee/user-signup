from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


def blank_statement(x):
    if x == []:
        return True
    else:
        return False

def character_length(x):
    if len(x) > 20 or len(x) < 3:
        return True
    else:
        return False

def email_missing_symbol_check(x):
    if x.count('@') < 1 or x.count('.') < 1:
        return True
    else:
        return False

def email_excess_symbol_check(x):
    if x.count('@') > 1 or x.count('.') > 1:
        return True
    else:
        return False 


@app.route("/signup", methods=['POST'])
def signup_complete_form():
    username = request.form['username']
    password = request.form['password']
    verpass = request.form['verpass']
    email = request.form['email']

    user_errors = ''
    pass_error = ''
    verpass_error = ''
    email_error = ''

    if blank_statement(username):
        user_errors = "You must type something for a username!"
        username = ''
    else:
        if character_length(username):
            user_errors = "Usernames must be between 3 and 20 characters!"
            username = ''

    if blank_statement(verpass):
        verpass_error = "Password cannot be blank!"
        verpass = ''
    else:
        if character_length(verpass):
            verpass_error = "Passwords must be between 3 and 20 characters!"
            verpass = ''

    if verpass != password:
        verpass_error = "Password and Verification must match!"
        pass_error = "Password and Verification must match!"
        pass_error = ''
        verpass = ''
        

    if email:
        if email_missing_symbol_check(email):
            email_error = 'Please enter a valid email!'
        if email_excess_symbol_check(email):
            email_error = "Email not valid!"
        if " " in email:
            email_error = "Email not valid!"

    if not user_errors and not pass_error and not verpass_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', user_errors=user_errors, pass_error=pass_error, verpass_error=verpass_error, email_error=email_error, username=username, email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html')
    
app.run()