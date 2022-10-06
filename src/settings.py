from dataclasses import dataclass
import os
import pathlib


@dataclass
class PathData:
    src_path = pathlib.Path(__file__).parent.resolve()
    asset_folder = f'{src_path}' + "/assets/"
    spreadsheet_file = asset_folder + 'wsj.xlsx'
