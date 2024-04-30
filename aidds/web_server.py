from flask import Flask
from flask_cors import CORS
from datetime import timedelta
from jinja2 import Environment

app = Flask(__name__)
app.debug = True
app.config.update(
    connect_args={"options": "-c timezone=utc"},
    SECRET_KEY="zAxx238qp!waooKcEhc",
    SESSION_COOKIE_NAME='AIDDS_SESSION',
    PERMANENT_SESSION_LIFETIME=timedelta(31)    # 31 days
)
app.jinja_env.trim_blocks = True

# # Make filters
# @app.template_filter('is_dict')
# def is_dict(value):
#     return isinstance(value, dict)

# Check Jinja2 Filters
# env = Environment()
# print(f'Jinja2 Filters: {env.filters}')

CORS(app)

# Route
from aidds.services.http import index

app.add_url_rule('/', view_func=index.as_view('index'))
