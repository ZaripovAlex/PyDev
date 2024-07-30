import json
import csv
import logging

def json_to_dict(json_file):
    with open(json_file) as json_file:
        data = json.load(json_file)
        # print(data)
    return data

def parsing_dict(data):
    items = data['params']['items']
    # print(items)
    return items

def get_id(data):
    return data['id']

def income(item):
    pass


def writeoff(item):
    pass


def move_op(item):
    pass


def return_op(item):
    pass


def operation (items):
    # print(type(items[0]['operations']))
    count = len(items)
    for item in items:
        for operation in item['operations']:
            if operation['type'] == 'income':
                income(item)
            elif operation['type'] == 'writeoff':
                writeoff(item)
            elif operation['type'] == 'move':
                move_op(item)
            elif operation['type'] == 'return':
                return_op(item)
    return count





def res_to_json(file):
    buffer = {}
    temp = json_to_dict(file)
    res = operation(parsing_dict(temp))
    buffer['jsonrpc'] = '2.0'
    buffer['id'] = get_id(temp)
    buffer['result'] = {}
    buffer['result']['count'] = res
    with open('result_inv.json', 'w') as outfile:
        json.dump(buffer, outfile, indent=2)



# if __name__ == '__main__':
#
#     res_to_json('zapros.json')