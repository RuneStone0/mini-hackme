from flask import Flask
from flask import request, make_response

app = Flask(__name__)

@app.route('/')
def root():
	# Simple Menu
	ret = """<html>
<head></head>
<body>
	Set language:
	<br />
	<a href="/settings?lang=en">EN</a>
	<a href="/settings?lang=fr">FR</a>
	<a href="/settings?lang=es">ES</a>

	"""

	# Display selected language (if set)
	lang = request.cookies.get('lang')
	if lang != None:
		ret = ret + """<br /><br />Selected language: """ + str(lang)

	return ret + """
</body></html>"""


@app.route('/settings', methods=['GET'])
def settings():
	lang = request.args.get('lang')
	#return "resp", 200, {'Set-Cookie': "lang="+lang}
	if lang != None:
		resp = make_response()
		resp.headers.set('Location', '/')
		resp.headers.set('Set-Cookie', "lang="+lang)
		return resp, 302
	return "missing lang parameter", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

