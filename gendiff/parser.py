import json
import yaml
import os


def get_file_format(file_path):
    """Determine file format by extension."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.json']:
        return 'json'
    elif ext in ['.yml', '.yaml']:
        return 'yaml'
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def parse_json(file_path):
    """Parse JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def parse_yaml(file_path):
    """Parse YAML file."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def parse_file(file_path):
    """
    Parse file based on its extension.
    
    Args:
        file_path: Path to the file
        
    Returns:
        dict: Parsed content
    """
    file_format = get_file_format(file_path)
    
    if file_format == 'json':
        return parse_json(file_path)
    elif file_format == 'yaml':
        return parse_yaml(file_path)
    else:
        raise ValueError(f"Unsupported format: {file_format}")
