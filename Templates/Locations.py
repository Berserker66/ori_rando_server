{{info}}

from .Types import *

locations_data = \
{{ locations|safe }}



lookup_name_to_id = {location_name: location_data.code for location_name, location_data in locations_data.items()}