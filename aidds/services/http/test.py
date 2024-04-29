from flask import render_template
from flask.views import MethodView

class Test(MethodView):
    
    def get(self):
        return render_template("test/test.html", name="Test!!!!!!")