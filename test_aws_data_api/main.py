import requests


def entity_info_by_name(service_url, api_key, name):
    headers = {"x-api-key": api_key}
    payload = {
        "name": name,
    }

    r = requests.post(service_url, headers=headers, json=payload, verify=False)
    print(r.status_code)
    return r.json()


if __name__ == '__main__':
    import json
    from ruyi_api_settings import RUYI_KG_SERVICE_URL, RUYI_API_KEY
    name = " 中国联合网络通信股份有限公司"
    service_url = '{}/entityInfoByName'.format(RUYI_KG_SERVICE_URL)
    body = entity_info_by_name(service_url, RUYI_API_KEY, name)
    print(json.dumps(body, ensure_ascii=False, indent=4, sort_keys=True))
