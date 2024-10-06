import json

def read_json_from_path(path: str) -> dict:

    with open(f'{path}/data.json', 'r') as fp:
        server_dict = json.load(fp)

    return server_dict

def count_server_utilization(server_dict: dict):
    """
    under = {0-49}
    over = {50-100}
    """
    count_dict = {'under': 0, 'over': 0}
    for k,v in server_dict.items():
        print(k + ' ' + str(v))
        if v < 50:
            count_dict['under'] +=1
        else:
            count_dict['over'] +=1

    print(count_dict)


if __name__ == '__main__':

    data_dict = read_json_from_path('../result')
    count_server_utilization(server_dict=data_dict)


