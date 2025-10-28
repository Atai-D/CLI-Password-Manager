import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("service")
parser.add_argument("--password", required=False)
args = parser.parse_args()


def open_file():
    try:
        file = open("passwords.json", "r+")
        file.close()
    except:
        file = open("passwords.json", "w")
        file.close()

    file = open("passwords.json", "r+")
    return file


def ask_user_if_overwrite(service, password):
    "ok"
    # somehow ask user


def is_service_exist(dic, service):
    return dic and dic.get(service)


def get_dic():
    file = open_file()
    j = file.read() or "{}"
    dic = json.loads(j)
    return (file, dic)


def create_password(service, password):
    (file, dic) = get_dic()

    if is_service_exist(dic, service):
        ask_user_if_overwrite(service, password)
    else:
        dic[service] = password
        jason = json.dumps(dic)
        file.close()
        file = open("passwords.json", "w")
        return file.write(jason)


def get_password(service):
    (_file, dic) = get_dic()
    return dic[service]


match args.command:
    case "add":
        print(create_password(args.service, args.password))
    case "get":
        print(get_password(args.service))
