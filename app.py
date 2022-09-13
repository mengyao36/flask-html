from flask import Flask, render_template

app = Flask(__name__)

# first page
@app.route('/')
def homepage_1():
    return render_template('p1.html')
    # import to note that it is going to look for the .html files in a folder called templates

# second page
@app.route('/friend')
def homepage_2():
    return render_template('p2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
