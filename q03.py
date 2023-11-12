

from pkg.modu import print_json, process_data, read_json, write_json

MENU_FILE = 'menu.json'
OUTPUT_FILE = 'output.json'
menu_data = read_json(MENU_FILE)
# 原始菜單
print("原始菜單:")
print_json(menu_data)
# 新增主菜
new_item = {
    "name": "海鮮燉飯",
    "price": 239,
    "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
}
menu_data['categories'][1]['items'].append(new_item)
# 顯示新增後
print("\n新增後的菜單:")
print_json(menu_data)
# 輸入折數
discount_rate = float(input("請輸入折扣率(0.0 ~ 1.0): "))
# 處理菜單
process_data(menu_data, discount_rate)
# 顯示打折後
print("\n打折後的菜單:")
print_json(menu_data)
# 寫入 output.json
write_json(menu_data, OUTPUT_FILE)
print(f"菜單已寫入 {OUTPUT_FILE}")
