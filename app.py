# Don't Remove Credit Tg - @Rajdev21_bot
# Subscribe YouTube Channel For Amazing Bot https://youtube.com
# Ask Doubt on telegram @raj_dev21

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechVJ'


if __name__ == "__main__":
    app.run()
