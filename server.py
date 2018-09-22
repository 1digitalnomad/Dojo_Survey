from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    print('The result page')

    return render_template('result.html')

@app.route('/danger')
def dang():
    print('a user tried to visit /danger.  we have redirected the user to /')

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
