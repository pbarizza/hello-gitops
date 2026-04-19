from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Flashy HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GitOps Hello World</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="card">
        <h1>Hello World GitOps!</h1>
        <p>Deployed via Dagger + Alibaba ACS</p>
    </div>
</body>
</html>
"""

@app.route("/")
def hello():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

