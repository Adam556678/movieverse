from flask import Flask, render_template, request

#creating a flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run():
    #get request type
    request_type = request.method

    if request_type == 'GET':
        return render_template('index.html')
    else:
        return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)