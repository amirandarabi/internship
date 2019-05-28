import requests
import json
import pandas as pd

'''
    this function will get machine ID 
    now it get manual but must impleament automaticly
'''


def get_id():
    machine_id = "76adfa47-8614-474c-b534-c28cd80b3d77"
    return machine_id


'''
    this function will get token 
    now it get manual but must impleament automaticly
'''


def get_token():
    token = "gAAAAABc5Uc7DTZlALFPAkmwl7iZ-YFHdIKKl01bZphdDGJFSEHKwOn1Bi7_EhICuHLb-H5K5zTUFijirLv5V3nrZ1JYQFkEd2y" \
            "XtPsGlTv4POfkfpghQyxOf4uA5V8S7ginbaroivUDtMlI4sH6xnkNjS1wFRcXm1Gcg_15NhzAStPJwof8L_w"
    return token


'''
    this function will get header
    now it get manual but must impleament automaticly
'''


def get_headers():
    token = get_token()
    headers = {
        'x-auth-token': token,
        'Host': "192.168.1.33:8041",
        'X-Amz-Date': "20190522T125452Z",
        'Authorization': "AWS4-HMAC-SHA256 Credential=undefined/20190522/us-east-1/execute-api/aws4_request,"
                         " SignedHeaders=host;x-amz-date;x-auth-token,"
                         " Signature=d9dda12527ad54a9a1c30908d352af347f56963ca9190e4032b49890b967d9a8",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "6ec69885-c2d7-47c3-937a-a610e4810fd5,8dba6351-7b61-407b-8ea8-cfcab28a0361",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    return headers


'''
    this function request server and save the response as json file 
'''


def get_request(name, url, headers):
    response = requests.request("GET", url, headers=headers).json()
    with open(name + '.json', 'w') as outfile:
        json.dump(response, outfile)
    return response


'''
    this function get metrics from data.json file
'''


def get_metrics():
    data = pd.read_json("data.json")
    print(data.columns)
    data['metrics'].to_csv("data.csv")
    return data['metrics']


'''
    this function get save list of metrics 
'''


def save_metrics(data):

    name = "metricsName_" + get_id() + ".csv"
    data.to_csv(name, index=False)


'''
    this function get measures of a metric and save it 
'''


def get_measures(metric_id):
    url = "http://192.168.1.33:8041/v1/metric/" + metric_id + "/measures"
    print("hello")
    df = pd.read_csv('data.csv')
    df.columns = ['name', 'id']
    name = df[df['id'] == metric_id]['name'].values
    print(name)
    get_request(str(name), url, get_headers())


def main():
    machine_id = get_id()
    url = "http://192.168.1.33:8041/v1/resource/instance/" + machine_id
    headers = get_headers()
    get_request("data", url, headers)
    metric_list = get_metrics()
    for m in metric_list:
        get_measures(m)


if __name__ == '__main__':
    main()
