from flask import Flask, request, redirect
import re

app = Flask(__name__)

@app.route('/')
def root():
	# Simple Menu
	ret = """<html>
<head>
</head>
<body>
	<br /><br />
	This following pages are vulnerable to open redirection attacks.
	Construct a URL that will redirect the user to google.com.
	<br /><br />
	<a href="/0?redir=http://google.com">0</a><br />
	<a href="/1?redir=http://google.com">1</a><br />
	<a href="/2?redir=http://google.com">2</a><br />
	<a href="/3?redir=http://google.com">3</a><br />
	<a href="/4?redir=http://google.com">4</a><br />
	<br /><br />
	Fun fact: Burp Suite v1.7.37 doesn't detect any the open redirect
	vulnerabilities.
</body>
</html>	
	"""
	return ret

@app.route("/0")
def zero():
	redir = request.args.get("redir")
	if redir == None:
		return "missing redir param", 400

	# Block redirects to http://
	# Solution: https://google.com
	match = re.search(r'http://', redir)
	if match:
		return "invalid redirect destination"
	else:
		return redirect(redir)

@app.route("/1")
def one():
	redir = request.args.get("redir")
	if redir == None:
		return "missing redir param", 400


	# Block redirects to http://
	# Case sensitive
	# Solution: HTTP://google.com
	match = re.search(r'[http|https]+://', redir)
	if match:
		return "invalid redirect destination"
	else:
		return redirect(redir)

@app.route("/3")
def three():
	redir = request.args.get("redir")
	if redir == None:
		return "missing redir param", 400


	# Block redirects to http://
	# Case insensitive
	# Solution: HTTPS:google.com
	match = re.search(r'[http|https]+://', redir, re.IGNORECASE)
	if match:
		return "invalid redirect destination"
	else:
		return redirect(redir)

@app.route("/4")
def four():
	redir = request.args.get("redir")
	if redir == None:
		return "missing redir param", 400


	# Block redirects to http://
	# Case insensitive
	# Only localhost ($self) redirects
	# Solution:
	#		if hosted on port 80/443: 	http://localhost.google.com
	#		if hosted on e.g. 5000:		http://localhost.google.com
	root = request.host
	match = re.search(r'(http://'+root+')', redir, re.IGNORECASE)
	if not match:
		return "Invalid redirect destination. Can only redirect to its own domain ("+root+").. or can it?"
	else:
		return redirect(redir)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
