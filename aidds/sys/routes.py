from dotmap import DotMap

# Route info
from aidds.server import index
from aidds.server import samples

_routes = {  # R: route, V: view-name, C: Class
    "index": {"R": "/", "V": "index", "C": index},
    "samples": {"R": "/samples", "V": "samples", "C": samples},
}
routes = DotMap(_routes)