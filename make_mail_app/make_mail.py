# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index() ->str:
    return render_template('index.html')

@app.route('/', methods=['POST'])
def Submit() ->str:
 
    print('post')
    txt  = request.form['honbun']
    print(txt)
    inpt = request.form['Input']
    print('入力='+ inpt)
    btn  = request.form['Button']
    print('ボタン='+btn)
    Te=[txt] 
    Te.append(inpt+btn)
    #Te.append(btn)
    T= '\n'.join(Te)
    print(T)
    return render_template('index.html', message=T )
        
if __name__ == '__main__':
    app.run(port=8080)