from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
	ret = """<html>
<head>
	<script type="text/javascript" src="http://evil.com/library.js"></script>
</head>
<body>
	This page is vulnerable to cross-site script include
</body>
</html>	
	"""
	return ret

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
