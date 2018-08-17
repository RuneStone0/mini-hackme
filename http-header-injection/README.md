# HTTP Header Injection
This sample website is vulnerable to HTTP Header Injections.

The website is using a patched version of Flask, that's making it vulnerable to this type of attacks.

# Setup using virtualenv
```
cd app
virtualenv -p python3 venv
source venv/bin/activate
pip install -r ../requirements.txt
sed -i '1171,1173s/.*//' venv/lib/python3.6//site-packages/werkzeug/datastructures.py
python run.py
```

# Setup using Docker
```
docker build -t http-header-injection .
docker run -p 5000:5000 http-header-injection
```

# Exercises

1) Construct an URL which will set an arbitrary cookie in the user's browser. For example: Set-Cookie: hacked=dawng!

2) Question: What attack vectors can you think of, when an attacker has the ability to set arbitrary cookies?

3) Construct a URL which will rewrite the content of the website. For example, rewrite the page, to include an XSS or fake login prompt.


# Flask patch
By default, Flask will raise an exception whenever \n or \r is injected into the HTTP headers. By removing the last if-statement, Flask will become vulnerable to header injections.
```
    def _validate_value(self, value):
        if not isinstance(value, text_type):
            raise TypeError('Value should be unicode.')
        if u'\n' in value or u'\r' in value:
            raise ValueError('Detected newline in header value.  This is '
                             'a potential security problem')
```
