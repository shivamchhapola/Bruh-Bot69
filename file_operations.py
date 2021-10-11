import json


def save_last_id(last_key, last_id, file_name):
    last_file = open(file_name, 'r')
    json_obj = json.load(last_file)
    last_file.close()
    json_obj[last_key] = last_id
    last_file = open(file_name, 'w')
    json.dump(json_obj, last_file)
    last_file.close()


def retrive_last_id(last_key, file_name):
    last_file = open(file_name, 'r')
    last_id = int(json.load(last_file)[last_key])
    last_file.close()
    return last_id
