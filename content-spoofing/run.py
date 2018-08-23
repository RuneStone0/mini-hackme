from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/')
def root():

	err = "RuntimeError%3a+cannot+join+current+thread"
	ret = """<html>
<head>
</head>
<body>
	This website is vulnerable to content spoofing. See if you can construct a link that would trick a user to perform an action they wouldn't otherwise do.
	<br />
	<br />
	<br />
	<form action="/login">
		<table>
			<tr>
				<td>Email:</td>
				<td><input type="text" name="email" /></td>
			</tr>
			<tr>
				<td>Password</td>
				<td><input type="password" name="password" /></td>
			</tr>
			<tr>
				<td></td>
				<td><input type="submit" value="Sign In" /></td>
			</tr>
		</table>
	</form>
</body>
</html>
	"""
	return ret

@app.route('/login')
def login():
	return redirect("/error?msg=Authentication Failed!")

@app.route('/error', methods=['GET'])
def error():
	msg = request.args.get("msg")
	if msg is None:
		return redirect("/")

	if len(msg) > 140:
		return "Error message cannot contain more than 140 characters."

	match = re.search(r'[<>]+', msg)
	if match:
		return "Invalid characters found.", 400
	else:
		ret = """<html>
<head>
</head>
<body>
	<h2>
		The application failed to process the request.
	</h2>
	<h4 style="color:grey;">
		Error message: """+msg+"""
	</h4>
</body>
</html>
	"""
		return ret

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

