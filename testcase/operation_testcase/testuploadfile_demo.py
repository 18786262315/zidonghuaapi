import requests

url = "http://192.168.10.56:8763/ms-order-data/excel/orderImportNew"

# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"excelFile\"; filename=\"180110.xls\"\r\nContent-Type: application/vnd.ms-excel\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

files = {'excelFile': open('../../data/180110.xls', 'rb')}

headers = {
    # 'content-type': "multipart/form-data",  # 不能加这个参数，加了会出错，选择files参数会自动调整类型
    # 'accept': "application/json",
    'token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyLXR5cGUiOiJEWExYMDIiLCJ1c2VyLW5hbWUiOiLnlJjpm6rojrLvvIjmraPlvI_vvIkiLCJ1c2VyLXN1YmplY3Rpb24iOiJkZGEwNjI1Ni00MjA2LTExZTctYjNjZC0wMDUwNTY5ZjdiMGMiLCJ1c2VyLXBhcmFtIjoie1wiaXNBZG1pblwiOjF9IiwidXNlci1pZCI6IjcwNmM0NDUwLTQ1ZWQtMTFlNy05ZTE4LTAyNDJhYzEyMDAxMyIsImlzcyI6Imdhbnh1ZWxpYW4iLCJ1c2VyLWNvZGUiOiJnYW54dWVsaWFuIiwiZXhwIjoxNTIxNjI1NzA3LCJpYXQiOjE1MjE2MTEzMDd9.dcquJyC81yMCTLMui5gvBwrVYvwB2Fpgnj9gqK43Kqo"
    }

response = requests.request("POST", url, files = files, headers=headers)
# response = requests.request("POST", url, data=payload, headers=headers)


print(response.text)