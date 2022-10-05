from dataclasses import dataclass
import pathlib


@dataclass
class PathData:
    test_path = pathlib.Path(__file__).parent.resolve()
    asset_folder = f'{test_path}' + "/assets/"
