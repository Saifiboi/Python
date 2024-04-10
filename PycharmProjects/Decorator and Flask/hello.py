from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'

    return wrapper


def make_emphasized(function):
    def wrapper():
        return '<emp>' + function() + '</emp>'

    return wrapper


def make_underlined(function):
    def wrapper():
        return '<u>'+function() + '</u>'
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasized
@make_underlined
def bye():
    return "bye!"


if __name__ == "__main__":
    app.run(debug=True)
