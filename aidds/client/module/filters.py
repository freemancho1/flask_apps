from aidds import app

# Make filters
@app.template_filter('is_dict')
def is_dict(value):
    return isinstance(value, dict)