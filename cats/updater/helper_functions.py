import json
from os.path import abspath


def print_log(*args, **kwargs):
    from sys import stdout
    try:
        log_file = kwargs.pop('log_file')
    except KeyError:
        kwargs['file'] = stdout
    else:
        kwargs['file'] = log_file
    print(*args, **kwargs)


def check_end_file_name(f_name, suffix):
    """

    :type suffix: str
    :type f_name: str
    """
    if f_name.endswith(suffix):
        return f_name
    else:
        return f_name + suffix


def save_json(file_name, data, log_file=None):
    file_name = check_end_file_name(file_name, '.json')
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print_log('create file:', abspath(file_name), log_file=log_file)


def open_json(file_name, log_file=None):
    file_name = check_end_file_name(file_name, '.json')
    try:
        res = json.load(open(file_name, 'r', encoding="utf-8"))
    except FileNotFoundError:
        f = abspath(file_name)
        message = 'Файл:\n\t{f}\n\t - не найден\n\t{n}'.format(f=f, n=file_name)
        print_log(message, log_file=log_file)
        raise ValueError(message)
    else:
        print_log('open file:', file_name, log_file=log_file)
        return res
