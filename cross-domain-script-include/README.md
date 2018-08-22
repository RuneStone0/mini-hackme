# HTTP Header Injection
This sample website is vulnerable to cross-domain script include.

# Setup using virtualenv
```
cd app
virtualenv -p python3 venv
source venv/bin/activate
pip install -r ../requirements.txt
python run.py
```

# Exercises

* Open https://localhost:5000/ in your browser.
* Open the browser's developer toolbar
* Watch how the script is loaded over HTTP
* Walking the extra mile: Perform a man-in-the-middle attack against the client loading the page and inject malicious code into the page
