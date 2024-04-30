from flask import render_template
from flask.views import MethodView

class Index(MethodView):
    
    def get(self):
        button_info = {
            "getSampleBtn": {"title": "Get Samples", "color": "btn-success", "click": "getSamples()"},
            "reqPredictBtn": {"title": "Req Predict", "color": "btn-danger", "click": "reqPredict()"},
            "reqRePredictBtn": {"title": "ReReq Predict", "color": "btn-danger", "click": "reqRePredict()"},
        }
        return render_template("index.html", btn_info=button_info)