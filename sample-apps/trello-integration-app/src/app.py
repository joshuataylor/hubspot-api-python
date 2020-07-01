from flask import Flask, redirect, url_for
from helpers.reverse_proxied import ReverseProxied
from routes.oauth import module as routes_oauth
from routes.init import module as routes_init
from routes.trello.auth import module as routes_trello_auth
from routes.trello.cards import module as routes_trello_cards

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(routes_oauth, url_prefix="/oauth")
app.register_blueprint(routes_init, url_prefix="/init")
app.register_blueprint(routes_trello_auth, url_prefix="/trello/auth")
app.register_blueprint(routes_trello_cards, url_prefix="/trello/cards")

app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/")
def home():
    return redirect(url_for("init.extension"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
