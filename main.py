import json
import yaml


def is_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except ValueError:
        return False


def is_yaml(string: str) -> bool:
    try:
        yaml.safe_load(string)
        return True
    except yaml.YAMLError:
        return False


def file_read(file_path: str) -> str:
    try:
        with open(file=file_path, mode='r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'File at \"{file_path}\" cannot be found')


def return_dict_from_string(content: str) -> dict:
    if is_json(content):
        data = json.loads(content)
    elif is_yaml(content):
        data = yaml.safe_load(content)
    else:
        raise Exception('Cannot convert file from json or xml to dict')
    return data


def compare_plain_objects(obj1: dict, obj2: dict) -> str:
    all_keys = obj1.keys() | obj2.keys()
    
    # Возможно, здесь лучше подойдет словарь или лист
    final_str = ''
    final_str += '{\n'

    for key in all_keys:
        exists_in_1 = bool(obj1.get(key))
        exists_in_2 = bool(obj2.get(key))

        indent = '  '
        match (exists_in_1, exists_in_2):
            case (True, True):
                if obj1[key] == obj2[key]:
                    final_str += f'{indent} {key}: {obj1[key]} \n'
                else:
                    final_str += f'{indent} - {key}: {obj1[key]} \n'
                    final_str += f'{indent} + {key}: {obj2[key]} \n'

            case (True, False):
                final_str += f'{indent} - {key}: {obj1[key]} \n'

            case (False, True):
                final_str += f'{indent} + {key}: {obj2[key]} \n'

            case _:
                raise Exception('Unexpected case')

    final_str += '}'

    return final_str
