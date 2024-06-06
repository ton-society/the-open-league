from dataclasses import dataclass


@dataclass
class Project:
    name: str # project name

    def name_safe(self):
        return self.name.replace(".", "_")
