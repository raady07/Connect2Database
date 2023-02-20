import json
import pkgutil

CONFIG = json.loads(pkgutil.get_data('config', 'config.json'))

student_data = json.loads(pkgutil.get_data('data', 'studentdata.json'))
