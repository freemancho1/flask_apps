from flask import Flask
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
app.debug = True
app.config.update(
    connect_args={"options": "-c timezone=utc"},
    SECRET_KEY="zAxx238qp!waooKcEhc",
    SESSION_COOKIE_NAME='AIDDS_SESSION',
    PERMANENT_SESSION_LIFETIME=timedelta(31)    # 31 days
)
app.jinja_env.trim_blocks = True

CORS(app)

# Route
from aidds.services.http import index
from aidds.services.http import test

app.add_url_rule('/', view_func=index.as_view('index'))
app.add_url_rule('/test', view_func=test.as_view('test'))