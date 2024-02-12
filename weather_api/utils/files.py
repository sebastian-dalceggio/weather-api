"Util functions to manipulate files"

from pathlib import Path
from typing import Dict
from string import Template
import json


def get_json_data(path: Path, values: Dict[str, str]) -> Dict:
    """Reads a json file and return it as a dictionary replacing the variables identified in the
    file. Each variable in the file has to be marked following these rules: $identifier or
    ${identifier}

    Args:
        path (Path): path to the json file
        values (Dict[str, str]): dictionary that maps each identifier with each real value

    Returns:
        Dict: json file as a dictionary with the identifiers replaced
    """
    with open(path, "r", encoding="us-ascii") as file:
        content = file.read()
        template = Template(content)
        content_replaced = template.substitute(values)
    return json.loads(content_replaced)
