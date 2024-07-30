import json

def json_to_dict(json_file):
    with open(json_file, encoding='UTF-8') as json_file:
        data = json.load(json_file)
        # print(data)
    return data

def get_id(data):
    return data['id']

def parsing_dict(data):
    items = data['params']['items']
    # print(items)
    return items


def add_to_database(item):
    pass


def operation(items):
    count = len(items)
    for item in items:
        add_to_database(item)
    return count

def res_to_json(file):
    buffer = {}
    temp = json_to_dict(file)
    res = operation(parsing_dict(temp))
    buffer['jsonrpc'] = '2.0'
    buffer['id'] = get_id(temp)
    buffer['result'] = {}
    buffer['result']['networkId'] = 'networkId'
    buffer['result']['count'] = res
    # print(buffer)
    with open('result_price.json', 'w', encoding='UTF-8') as outfile:
        json.dump(buffer, outfile, indent=2)



if __name__ == '__main__':
    res_to_json('zapros.json')