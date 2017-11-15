import dice_markovchain
from flask import Flask, render_template
app=Flask(__name__)
dicenumber=0

@app.route('/')
def game():
    return render_template('dice.html')
@app.route('/markovchain_predict')
def markovchain_predict():
    global dicenumber
    print(dicenumber)
    if dicenumber==0:
        dicenumber=dice_markovchain.dice_roll_markov_chain(5)
        print (dicenumber)
    else:
       dicenumber=dice_markovchain.dice_roll_markov_chain(dicenumber)
       print (dicenumber)
    return str(dicenumber)
if __name__=='__main__':
    app.debug=True
    app.run(host='localhost',port=5000)
