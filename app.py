from flask import Flask, request, render_template, flash
from lexer import desglosar_curp
from parser import analizar_curp

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def home():
    tokens = None
    contador_tokens = None
    curp = ""

    if request.method == 'POST':
        curp = request.form.get('curp', '').strip().upper()
        mensaje = analizar_curp(curp)
        
        if mensaje == "La CURP es válida.":
            flash(mensaje, 'success')
            tokens, contador_tokens = desglosar_curp(curp)
        else:
            flash(mensaje, 'error')
    
    return render_template('index.html', curp=curp, tokens=tokens, contador_tokens=contador_tokens)

if __name__ == '__main__':
    app.run(debug=True)
