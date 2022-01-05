from flask import Flask
import time

app = Flask(__name__)


def capitalize(word: str) -> str:
    return word.title()


@app.route('/capitalize/<word>')
def capitalize_request(word: str) -> str:
    return capitalize(word)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
