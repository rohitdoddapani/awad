from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report', methods=['POST'])
def report():
    username = request.form.get('username')
    password = request.form.get('password')

    failed_attempt = False
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    ends_with_number = password[-1].isdigit()
    length_8 = len(password) >= 8
    
    if not has_uppercase or not ends_with_number or not has_lowercase or not length_8:
        failed_attempt = True
        failed_attempt_times = session.get('failed_attempt_times', 1)
        session['failed_attempt_times'] = failed_attempt_times + 1
        warning = ''

        if failed_attempt_times >= 3:
            warning = 'Warning: Three consecutive failed attempts. Please try again later.'
    else:
        session['failed_attempt_times'] = 1
        failed_attempt_times = 0
        warning = ''

    return render_template('report.html', failed_attempt=failed_attempt, has_uppercase=has_uppercase, ends_with_number=ends_with_number,has_lowercase=has_lowercase,length_8=length_8,warning = warning,failed_attempt_times=failed_attempt_times)


if __name__ == '__main__':
    app.run(debug=True)
