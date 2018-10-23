from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'DoNotTell'

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    errors=False
    session['your_name']=request.form['your_name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comments']=request.form['comments']

    if len(request.form['your_name']) < 1:
        flash('Name can not be empty. Try again.')
        errors=True
    if len(request.form['comments'])<1:
        flash('Comments Can Not Be Empty')
    if len(request.form['comments'])>120:
        flash('Comments can not be more than 120 characters long. Try again.')
        errors=True

    if errors==True:
        return redirect("/")
    else:
        return render_template('result.html')



    print('The result page')


@app.route('/danger')
def dang():
    print('a user tried to visit /danger.  we have redirected the user to /')

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
