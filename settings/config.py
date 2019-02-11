import os

import yaml


class Settings(object):
    dict = None  # type: dict

    def __init__(self, d):
        self.dict = d
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [Settings(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, Settings(b) if isinstance(b, dict) else b)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BASE_DIR, 'settings/api_settings.yml'), 'r') as f:
    settings = Settings(yaml.load(f))
