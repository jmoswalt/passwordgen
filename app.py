# -*- coding: utf-8 -*-

import random
import string
from flask import Flask, render_template, request

DEBUG = False

app = Flask(__name__)
app.config.from_object(__name__)

def random_chars(n=12):
    return ''.join(random.choice('!@#$%^&*' + string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(int(n)))

@app.route('/', methods=['GET', 'POST'])
def index():
    """
        Homepage with link to generate password
    """
    n = request.form.get('n') or '12'
    if int(n) < 8 or int(n) > 16:
        return 'This page does not exist', 404
    password = random_chars(n)
    length_options = [str(x) for x in range(8, 17)]
    context = {'password': password, 'n': n, 'nums': length_options}
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run()
