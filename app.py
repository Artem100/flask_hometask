from fernet import Fernet
from flask import Flask, render_template, request


app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def index():
    """
    Default page http://127.0.0.1:5000/

    :return:
    """

    title = request.args.get('title', 'default')
    return render_template('index.html', title=title)


@app.route('/encrypt')
def string_to_encrypt_method():
    """
    url_path takes value (?param=) to encrypt it.
    Input value (?param=), after field *Encrypted result* will display decrypt value on page

    :return:
    """
    title = request.args.get('param', 'default')
    token = f.encrypt(title)
    return render_template('index.html', encrypt=token)


@app.route('/decrypt')
def string_to_decrypt_method():
    """
        url_path takes value to decrypt it.
        Input value (?param=), after field *Decrypted result* will display decrypt value on page

        :return:
        """
    title_dec = request.args.get('param', 'default')
    dec = f.decrypt(title_dec.encode())
    return render_template('index.html', decrypt=dec.decode())

app.run(debug=True, port=5000)