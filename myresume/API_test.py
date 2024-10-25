import requests

url = "https://openapi.twse.com.tw/v1/fund/MI_QFIIS_sort_20"
response = requests.get(url)

# 確認請求成功
if response.status_code == 200:
    data = response.json()  # 解析 JSON 數據
    print(data)  # 輸出數據
else:
    print("Failed to retrieve data:", response.status_code)
