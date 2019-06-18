from bottle import view, run, route, static_file
from datetime import datetime as dt
import os

@route("/static/css/<filename>")
def send_css(filename):
	return static_file(filename, root='static/css')


@route("/hello")
@route("/hello/<name>")
@view("index1")
def return_hellopage(name='User'):
	now_date = dt.now().isoformat()
	return {"name": name.upper(),
			"now_date": now_date}

@route('/')
def mainpage():
	return "<h1>Success!</h1>"

@route("/current_date")
def curr_date():
	return {"date": dt.now().isoformat()}

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)