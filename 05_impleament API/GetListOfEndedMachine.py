import requests
import json
import pandas as pd


def get_response(url, headers):
    response = requests.request("GET", url, headers=headers)
    return response.json()


def save_response(response):
    with open('data.json', 'w') as outfile:
        json.dump(response, outfile)


def get_ended():
    df = pd.read_json('data.json')
    df = df[df['ended_at'].notnull()]
    print("number of ended: ", len(df['id'].unique()))
    return df['id'].unique()


def get_alive():
    df = pd.read_json('data.json')
    df = df[df['ended_at'].isnull()]
    print("number of alive: ", len(df['id'].unique()))
    return df['id'].unique()


def save_ended(ListOfEnded):
    ListOfEnded.to_csv("ended.csv")


def save_alive(ListOfAlive):
    ListOfAlive.to_csv("alive.csv")


def main():
    url = "http://192.168.1.33:8041/v1/resource/generic"

    headers = {
        'x-auth-token': "gAAAAABc5QOCxHPC4nFxNDreBGcOmXWrPsSl7ZFqCvapDWKyVbd75eat4wtandSiehKXI39gE3DOuw-V7x1eftmZnvTyk2of-vdITAZLlILYdUUBoNzIomp0PNjJ7TVt_yJJAQ3eNzwcMNU0pOF-uy1MvuKBKR_K4u72uoYGmwC3ZbXemePmSF0",
        'Host': "192.168.1.33:8041",
        'X-Amz-Date': "20190522T081527Z",
        'Authorization': "AWS4-HMAC-SHA256 Credential=undefined/20190522/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-date;x-auth-token, Signature=3e4fa760b4cb24db05c8a54ede4c303bec9c540cd5d861590812112c5ba5fd78",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "bb39b097-c667-47f7-9a67-9ab9012757d3,247ae7d8-b4f5-48db-99d7-4ec7a8cac7e7",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    url = "http://192.168.1.33:8041/v1/resource/generic"

    headers = {
        'x-auth-token': "gAAAAABc5TeRzmzmLRAuJMBx1bpT5GY3MC-j-7uLGEV6k-d_EImx1LCuYaXStVmDWh2K75wgJ9mn2DlvT5RGAFaa1d9_uUEg21U3hl7komFlg6cPI8R4LsQgfkC7kUQBP_mAnAqkTQ-w0exdCS_zipQ3SCu-iRco_eLbg6NvB0LRuMMSwZmSogk",
        'Host': "192.168.1.33:8041",
        'X-Amz-Date': "20190522T122009Z",
        'Authorization': "AWS4-HMAC-SHA256 Credential=undefined/20190522/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-date;x-auth-token, Signature=35cfedfe2ed201650023372f943b239f23aaafe118b9b59af48adb192848c939",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "618e2414-4f3f-48d5-8605-c8fecfb796b5,280622f8-e073-40f3-97dd-fab1d165211b",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }


    response = get_response(url, headers)
    save_response(response)
    df = pd.read_json("data.json")
    print(df[df['type'] == 'instance'])
    # ended = get_ended()
    # save_ended(ended)
    # alive = get_alive()
    # save_ended(alive)
    # df = pd.read_csv("data/ended.csv")
    #





    # url = "http://192.168.1.33:8041/v1/resource/generic/"
    #
    # payload = "{ \"auth\": {\r\n    \"identity\": {\r\n      \"methods\": [\"password\"],\r\n      \"password\": {\r\n        \"user\": {\r\n          \"name\": \"admin\",\r\n          \"domain\": { \"id\": \"192.168.1.33\" },\r\n          \"password\": \"123\"\r\n        }\r\n      }\r\n    }\r\n  }\r\n}"
    # headers = {
    #     'x-auth-token': "gAAAAABc5TeRzmzmLRAuJMBx1bpT5GY3MC-j-7uLGEV6k-d_EImx1LCuYaXStVmDWh2K75wgJ9mn2DlvT5RGAFaa1d9_uUEg21U3hl7komFlg6cPI8R4LsQgfkC7kUQBP_mAnAqkTQ-w0exdCS_zipQ3SCu-iRco_eLbg6NvB0LRuMMSwZmSogk",
    #     'Content-Type': "text/plain",
    #     'User-Agent': "PostmanRuntime/7.13.0",
    #     'Accept': "*/*",
    #     'Cache-Control': "no-cache",
    #     'Postman-Token': "1712f379-0e8e-40ba-a59e-3506080d4137,73c06612-783f-4aa7-b417-6c11383745c9",
    #     'Host': "192.168.1.33:8041",
    #     'accept-encoding': "gzip, deflate",
    #     'content-length': "241",
    #     'Connection': "keep-alive",
    #     'cache-control': "no-cache"
    # }

    # print(df['id'])
    # for id in df['id']:
    #     requests.request("DELETE", url + id, data=payload, headers=headers)


if __name__ == '__main__':
    main()


