#!/usr/bin/env python

import glob
from PIL import Image
from tonsdk.utils import Address

from models.icons import get_icon_name
from models.project import NFT, App, Token
from models.season_config import SeasonConfig


def check_address(address: str):
    assert address == Address(address).to_string(True, True, True), f"Address must be in bounceable format: {address}"


if __name__ == '__main__':
    for file in glob.glob("seasons/s*py"):
        # some weird Python introspection hacks to ge all seasons and extract all projects
        season_name = file.split("/")[1].split(".")[0]
        import_stmt = f"seasons.{season_name}"
        print(f"Importing {import_stmt}")
        m = __import__(import_stmt, globals(), locals(), ['SeasonConfig'])
        # print(m.__dict__)
        for name, season_config in dict([(name, cls) for name, cls in m.__dict__.items() if isinstance(cls, SeasonConfig)]).items():
            print(f"Checking {name} from {season_name}")
            names = set()
            projects_addresses = set()
            smc_addresses = set()
            for project in season_config.projects:
                assert project.name not in names, f"Duplicate found: {project.name}"
                names.add(project.name)
                image = get_icon_name(season_config, project)
                if image.endswith(".svg"):
                    continue
                assert image.endswith(".png"), "Only png and svg formats are supported"
                image_obj = Image.open("projects/icons/" + image)
                assert image_obj.size == (100, 100), f"Image {image} for project {project.name} " \
                                                     f"has wrong dimensions: %dx%d" % image_obj.size

                if isinstance(project, (Token, NFT)):
                    check_address(project.address)
                    assert project.address not in projects_addresses, f"Duplicate found: {project.address}"
                    projects_addresses.add(project.address)
                if isinstance(project, App):
                    addresses = set()
                    for metric in project.metrics:
                        for attribute, value in metric.__dict__.items():
                            if attribute in ("address", "referral_address", "marketplace") and value:
                                check_address(value)
                                addresses.add(value)
                            if attribute in ("addresses", "admin_addresses", "collections", "destinations") and value:
                                for address in value:
                                    check_address(address)
                                    addresses.add(address)
                            if attribute in ("jetton_masters") and value:
                                for address in value:
                                    check_address(address)
                    for address in addresses:
                        assert address not in smc_addresses, f"Duplicate found: {address}"
                        smc_addresses.add(address)
