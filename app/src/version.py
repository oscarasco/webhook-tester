from dataclasses import dataclass
from functools import cached_property

import toml

from config import settings

TOML_FILE = settings.CZ_TOML_PATH


@dataclass
class Version:

    toml_filepath: str

    @cached_property
    def version(self):
        with open(self.toml_filepath, 'r') as f:
            config = toml.load(f)

        return config['tool']['commitizen']['version']


webhook_tester_version = Version(toml_filepath=TOML_FILE)
