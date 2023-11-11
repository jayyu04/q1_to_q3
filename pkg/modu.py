import json

def triangle_zhonxin(a, b, c):

    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    x = round((x1 + x2 + x3) / 3)
    y = round((y1 + y2 + y3) / 3)

    return x, y

def read_json(file_name: str) -> dict:
    """
    將 json 檔案轉為字典後回傳
    """
    with open("meun.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def print_json(data: dict) -> None:
    """
    將字典轉為 json 字串後輸出到螢幕
    """
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    print(json_str)

def process_data(data: dict, discount: float) -> None:
    """
    將字典中每個菜品的價格打 discount 折數
    """
    for category in data['categories']:
        for item in category['items']:
            item['price'] = round(item['price'] * discount)

def write_json(data: dict, file_name: str) -> None:
    """
    將字典轉為檔案
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
