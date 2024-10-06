import json
import random
import sys

def set_json_server_dict(num_items: int) -> dict[str:int]:
    server_keys = [f"server{i}" for i in range(num_items)]
    server_vals = [random.randint(0,100) for i in range(num_items)]

    return dict(zip(server_keys, server_vals))

def store_server_dict(server_dict:dict, path: str):
    """
    Creates or opens json and writes server_dict to file.
    """
    with open(f'{path}/data.json', 'w') as fp:
        json.dump(server_dict, fp)


if __name__ == '__main__':
    # Access variables from shell
    # python generator.py num_of_servers path
    # ex. nl@Ns-MacBook-Air-2 cloud-computing-notes % python week1_notes/generator.py 6 result
    #       /var/www/html -- this allows exposure to html exposure
    """
    print(sys.argv[0]) # prints generator.py
    print(sys.argv[1]) # prints num_of_servers
    print(sys.argv[2]) # prints path
    """
    server_dict = set_json_server_dict(int(sys.argv[1]))
    store_server_dict(server_dict, sys.argv[2])