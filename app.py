from flask import Flask, render_template, request
from main import *
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    product_name_input = request.form.get("inputProductName")
    
    global product_name
    product_name = get_recommendation(product_name_input)

    if request.method == 'POST':
        submitted = True
    else:
        submitted = False

    return render_template('index.html',result=product_name, submitted=submitted,inputan=product_name_input)

if __name__ == "__main__":
    app.run(debug=True)