from flask import Flask
from flask_cors import CORS
from jinja2 import Environment

from .sys import config
from .sys import messages
from .sys.routes import routes

# Set `static` & `templates` folder
app = Flask(__name__, 
            static_folder=config.app.static_folder, 
            template_folder=config.app.template_folder)
# Filters should be executed after 'app' is created.
import aidds.client.module.filters

app.debug = config.app.debug
app.config.update(
    connect_args=config.app.connect_args,
    SECRET_KEY=config.app.secret_key,
    SESSION_COOKIE_NAME=config.app.session_cookie_name,
    PERMANENT_SESSION_LIFETIME=config.app.session_lifetime    # 31 days
)
app.jinja_env.trim_blocks = config.app.jinja.trim_blocks

# # Make filters : Move __init__.py
# @app.template_filter('is_dict')
# def is_dict(value):
#     return isinstance(value, dict)

# Check Jinja2 Filters
# env = Environment()
# print(f'Jinja2 Filters: {env.filters}')

CORS(app)

# Route
_routes = list(routes.keys())
for r in _routes:
    app.add_url_rule(
        eval(f"routes.{r}.R"), 
        view_func=eval(f"routes.{r}.C").as_view(f"routes.{r}.V")
    )
# app.add_url_rule(config.r.index.R, view_func=index.as_view(config.r.index.V))