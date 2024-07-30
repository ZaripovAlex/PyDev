import csv
import json
import logging
from dateutil.parser import parse

logging.basicConfig(level=logging.ERROR, filename='generate.log', filemode='w')
logger = logging.getLogger(__name__)


def read_csv(file):
    with open(file, 'r', encoding='utf-8') as data:
        reader = csv.reader(data)
        return list(reader)


def verify_data(lst):
    res = []
    for elem in lst:
        if elem[0].isdigit():
            if elem[1].isdigit():
                try:
                    if parse(elem[2], fuzzy=False):
                        if elem[4].isdigit():
                            res.append(elem)
                except ValueError:
                    logger.error(elem)
        else:
            logger.error(elem)
    return res


def elem_to_dict(data):
    res = {}
    res_lst = []
    for elem in data:
        # print(elem)
        res['STORE_EXT_ID'] = elem[0]
        res['PRICE_EXT_NAME'] = elem[1]
        res['SNAPSHOT_DATETIME'] = elem[2]
        res['IN_MATRIX'] = elem[3]
        res['QTY'] = elem[4]
        res['SELL_PRICE'] = elem[5]
        res['PRIME_COST'] = elem[6]
        res['MIN_STOCK_lEVEL'] = elem[7]
        # res['STOCK_IN_DAYS'] = elem[8]
        # res['IN_TRANSIT'] = elem[9]
        res_lst.append(res)
    print(res_lst)
    return res_lst

def dict_in_json(data):
    with open('inventory.json', 'w', encoding='utf-8') as outfile:
        for elem in data:
            json.dump(elem, outfile, indent=2)

if __name__ == '__main__':
    dict_in_json(elem_to_dict(verify_data(read_csv('inventory1.csv'))))
