from dotmap import DotMap

# Route info
from aidds.server.http import index

_routes = {  # R: route, V: view-name, C: Class
    "index": {"R": "/", "V": "index", "C": index},
}
routes = DotMap(_routes)