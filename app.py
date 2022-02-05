from flask import Flask, render_template, request
from main import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommendation', methods=['GET','POST'])
def recommendation():
    product_name_input = request.form.get("inputProductName")
    
    global product_name
    product_name = get_recommendation(product_name_input)

    if request.method == 'POST':
        submitted = True
    else:
        submitted = False
    examples = get_examples()
    return render_template('recommendation.html',result=product_name, submitted=submitted,inputan=product_name_input,examples=examples)

@app.route('/clustering', methods=['GET','POST'])
def clustering():
    # product_name_input = request.form.get("inputProductName")
    # global product_name
    # product_name = get_recommendation(product_name_input)
    # input_list = [0 for i in range(20)]
    # input_list = list(map(int,request.form.values()))
    global cluster_idx
    if request.method == 'POST':
        submitted = True
        input_list = list(map(int,request.form.values()))
    else:
        submitted = False
        input_list = [0 for i in range(20)]
    cluster_idx = get_cluster(input_list)
    return render_template('clustering.html',result=cluster_idx, submitted=submitted,inputan=input_list)

if __name__ == "__main__":
    app.run(debug=True)