# -*- coding: utf-8 -*-
import requests
import json

# from AthenaTest.common.readConfig import ReadConfig


def interfaceTest(num,
                  api_purpose,
                  api_host,
                  request_url,
                  request_method,
                  request_data_type,
                  header_data,
                  request_data,
                  encryption,
                  check_point,
                  s=None):

    # 表示收货仓且只传token
    headersA10 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A1',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示收货仓且需要传pagenum等
    headersA11 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A1',
        'tokenSecret': '123456',
        'pagenum': "1",
        'pagesize': "20",
        'pageCount': 'false'
    }

    # 表示收货仓且需要上传files的情况
    headersA12 = {
        'tokenCode': 'A1',
        'tokenSecret': '123456',
    }

    # 表示客服且只传token
    headersA20 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A2',
        'tokenSecret': '123456'
    }

    # 表示客服且需要传pagenum等
    headersA21 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A2',
        'tokenSecret': '123456',
        'pagenum': '1',
        'pagesize': '20',
        'pageCount': 'false'
    }

    # 表示客服且需要上传files的情况
    headersA22 = {'tokenCode': 'A2', 'tokenSecret': '123456'}

    # 表示网点且只传token
    headersA30 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A3',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示网点且需要传pagenum等
    headersA31 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A3',
        'tokenSecret': '123456',
        'pagenum': '1',
        'pagesize': '20',
        'pageCount': 'false'
    }

    # 表示网点且需要上传files的情况
    headersA32 = {'tokenCode': 'A3', 'tokenSecret': '123456'}

    # 表示宜家web且只传token
    headersA40 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A4',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示宜家web且需要传pagenum等
    headersA41 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A4',
        'tokenSecret': '123456',
        'pagenum': '1',
        'pagesize': '20',
        'pageCount': 'false'
    }

    # 表示宜家web且需要上传files的情况
    headersA42 = {'tokenCode': 'A4', 'tokenSecret': '123456'}

    # 表示宜家app配送且只传token
    headersA50 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A5',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示宜家app配送且需要传pagenum等
    headersA51 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A5',
        'tokenSecret': '123456',
        'pagenum': '1',
        'pagesize': '20',
        'pageCount': 'false'
    }

    # 表示宜家app配送且需要上传files的情况
    headersA52 = {'tokenCode': 'A5', 'tokenSecret': '123456'}

    # 表示宜家app安装且只传token
    headersA60 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A6',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示宜家app安装且需要传pagenum等
    headersA61 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A6',
        'tokenSecret': '123456',
        'pagenum': '1',
        'pagesize': '20',
        'pageCount': 'false'
    }

    # 表示宜家app安装且需要上传files的情况
    headersA62 = {'tokenCode': 'A6', 'tokenSecret': '123456'}

    # 表示宜家app的sams且只传token
    headersA70 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A7',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示宜家app的sams且需要传pagenum等
    headersA71 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A7',
        'tokenSecret': '123456',
        'pagenum': '1',
        'pagesize': '20',
        'pageCount': 'false'
    }

    # 表示宜家app的sams且需要上传files的情况
    headersA72 = {'tokenCode': 'A7', 'tokenSecret': '123456'}

    # 表示直营收货仓且只传token
    headersA80 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A8',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示直营收货仓且需要传pagenum等
    headersA81 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A8',
        'tokenSecret': '123456',
        'pagenum': "1",
        'pagesize': "20",
        'pageCount': 'false'
    }

    # 表示直营收货仓且需要上传files的情况
    headersA82 = {'tokenCode': 'A8', 'tokenSecret': '123456'}

    # 表示直营网点且只传token
    headersA90 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A9',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示直营网点且需要传pagenum等
    headersA91 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A9',
        'tokenSecret': '123456',
        'pagenum': '1',
        'pagesize': '20',
        'pageCount': 'false'
    }

    # 表示直营网点且需要上传files的情况
    headersA92 = {'tokenCode': 'A9', 'tokenSecret': '123456'}

    # 表示物流且只传token
    headersA100 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A10',
        'tokenSecret': '123456',
        'pageCount': 'false'
    }

    # 表示物流且需要传pagenum等
    headersA101 = {
        'Content-Type': 'application/json',
        'tokenCode': 'A10',
        'tokenSecret': '123456',
        'pagenum': '1',
        'pagesize': '20',
        'pageCount': 'false'
    }

    # 表示物流且需要上传files的情况
    headersA102 = {'tokenCode': 'A10', 'tokenSecret': '123456'}

    # 测试环境
    # api_host = '192.168.10.56:8763'

    # 测试环境
    api_host = '192.168.10.60:8763'

    # 开发环境
    # api_host = '192.168.10.59:8763'

    # 正式环境
    # api_host = '192.168.10.55:8763'

    # 预发布环境
    # api_host = '192.168.10.53:8763'

    # api_host = '222.209.207.41:3000/api'

    if request_method == 'POST':  # POST请求
        if request_data == '':
            if header_data == '':
                r = requests.request(
                    "POST", url='http://' + api_host + request_url)
            else:
                #r = requests.request("POST", url='http://' + api_host + request_url, headers=json.loads(header_data))  # json.dumps : dict转成str; json.loads:str转成dict (从excel取的数据需要转换一下）
                headers = [
                    'A10', 'A11', 'A20', 'A21', 'A30', 'A31', 'A40', 'A41',
                    'A50', 'A51', 'A60', 'A61', 'A70', 'A71', 'A80', 'A81',
                    'A90', 'A91', 'A100', 'A101'
                ]

                if header_data in headers:
                    r = requests.request(
                        "POST",
                        url='http://' + api_host + request_url,
                        headers=eval('headers' + header_data))
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")

        else:
            if request_data_type == 'formData':  # 请求数据格式为formData
                if header_data == '':
                    r = requests.request(
                        "POST",
                        url='http://' + api_host + request_url,
                        files=json.loads(request_data))
                else:
                    #r = requests.request("POST", url='http://' + api_host + request_url,files=json.loads(request_data), headers=json.loads(header_data))
                    headerss = [
                        'A12', 'A22', 'A32', 'A42', 'A52', 'A62', 'A72', 'A82',
                        'A92', 'A102'
                    ]
                    if header_data in headerss:
                        files = eval(
                            request_data)  # 由于格式问题导致失败，用json转换也会失败，最后用eval解决
                        # files = {'excelFile': open('../../data/180110.xls', 'rb')}  # 直接写死在代码里面是可以的
                        r = requests.request(
                            "POST",
                            url='http://' + api_host + request_url,
                            files=files,
                            headers=eval('headers' + header_data))
                    else:
                        print("没有对应的headers,请核对excel中的header_data数据是否正确！")

            elif request_data_type == 'raw':  # 请求数据格式为raw，需要以json格式传递数据
                if header_data == '':
                    r = requests.request(
                        "POST",
                        url='http://' + api_host + request_url,
                        data=json.dumps(json.loads(request_data)))
                else:
                    #r = requests.request("POST", url='http://' + api_host + request_url,data=json.dumps(json.loads(request_data)), headers=json.loads(header_data))
                    headerss = [
                        'A10', 'A11', 'A20', 'A21', 'A30', 'A31', 'A40', 'A41',
                        'A50', 'A51', 'A60', 'A61', 'A70', 'A71', 'A80', 'A81',
                        'A90', 'A91', 'A100', 'A101'
                    ]
                    if header_data in headerss:
                        r = requests.request(
                            "POST",
                            url='http://' + api_host + request_url,
                            data=json.dumps(json.loads(request_data)),
                            headers=eval('headers' + header_data))
                    else:
                        print("没有对应的headers,请核对excel中的header_data数据是否正确！")

            else:
                if header_data == '':
                    r = requests.request(
                        "POST",
                        url='http://' + api_host + request_url,
                        data=json.dumps(json.loads(request_data)))
                else:
                    #r = requests.request("POST", url='http://' + api_host + request_url,data=json.loads(request_data), headers=json.loads(header_data))
                    headerss = [
                        'A10', 'A11', 'A20', 'A21', 'A30', 'A31', 'A40', 'A41',
                        'A50', 'A51', 'A60', 'A61', 'A70', 'A71', 'A80', 'A81',
                        'A90', 'A91', 'A100', 'A101'
                    ]
                    if header_data in headerss:
                        r = requests.request(
                            "POST",
                            url='http://' + api_host + request_url,
                            data=json.loads(request_data),
                            headers=eval('headers' + header_data))
                    else:
                        print("没有对应的headers,请核对excel中的header_data数据是否正确！")

    elif request_method == 'GET':  # GET请求
        if request_data == '':
            if header_data == '':
                r = requests.request(
                    "GET", url='http://' + api_host + request_url)
            else:
                #r = requests.request("GET", url='http://' + api_host + request_url, headers=json.loads(header_data))
                headerss = [
                    'A10', 'A11', 'A20', 'A21', 'A30', 'A31', 'A40', 'A41',
                    'A50', 'A51', 'A60', 'A61', 'A70', 'A71', 'A80', 'A81',
                    'A90', 'A91', 'A100', 'A101'
                ]
                if header_data in headerss:
                    r = requests.request(
                        "GET",
                        url='http://' + api_host + request_url,
                        headers=eval('headers' + header_data))
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")

        else:
            if header_data == '':
                r = requests.request(
                    "GET",
                    url='http://' + api_host + request_url,
                    params=json.loads(request_data))
            else:
                #r = requests.request("GET", url='http://' + api_host + request_url, params=json.loads(request_data),headers=json.loads(header_data))
                headerss = [
                    'A10', 'A11', 'A20', 'A21', 'A30', 'A31', 'A40', 'A41',
                    'A50', 'A51', 'A60', 'A61', 'A70', 'A71', 'A80', 'A81',
                    'A90', 'A91', 'A100', 'A101'
                ]
                if header_data in headerss:
                    r = requests.request(
                        "GET",
                        url='http://' + api_host + request_url,
                        headers=eval('headers' + header_data),
                        params=json.loads(request_data))
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")

    elif request_method == 'DELETE':  # DELETE请求
        if request_data == '':
            if header_data == '':
                r = requests.request(
                    'DELETE',
                    url='http://' + api_host + request_url,
                    params=request_data)
            else:
                # r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=json.loads(header_data))
                headerss = [
                    'A10', 'A11', 'A20', 'A21', 'A30', 'A31', 'A40', 'A41',
                    'A50', 'A51', 'A60', 'A61', 'A70', 'A71', 'A80', 'A81',
                    'A90', 'A91', 'A100', 'A101'
                ]
                if header_data in headerss:
                    r = requests.request(
                        'DELETE',
                        url='http://' + api_host + request_url,
                        params=request_data,
                        headers=eval('headers' + header_data))
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")

        else:
            if header_data == '':
                r = requests.request(
                    'DELETE',
                    url='http://' + api_host + request_url,
                    params=json.loads(request_data))
            else:
                #r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=json.loads(header_data))
                headerss = [
                    'A10', 'A11', 'A20', 'A21', 'A30', 'A31', 'A40', 'A41',
                    'A50', 'A51', 'A60', 'A61', 'A70', 'A71', 'A80', 'A81',
                    'A90', 'A91', 'A100', 'A101'
                ]
                if header_data in headerss:
                    r = requests.request(
                        'DELETE',
                        url='http://' + api_host + request_url,
                        params=json.loads(request_data),
                        headers=eval('headers' + header_data))
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")
    else:
        print(num + ' ' + api_purpose +
              '  HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
        s = None
        return 400, s

    status = r.status_code  # 返回状态
    resp = r.text  # 返回数据
    # print(resp)
    #
    # respjson = json.loads(resp)
    #
    # prepaid = respjson['data']['orderData']
    # print(prepaid)

    print("测试接口：" + request_url)
    print("返回的状态：" + str(status))

    # self.assertEqual(resp['success'], check_point)

    if status == 200:  # 判断返回状态是否为A200
        if check_point in resp:  # 检查测试用例中的检查点是否包含在返回的数据里面
            result = "pass"
            print("测试结果：成功！！！  " + str(status))
            # print('返回的数据：' + str(r.text))
            return status, resp, s, result
        else:
            result = "fail"
            print("测试结果：失败！！！  " + str(status))
            print('返回的数据：' + str(r.text))
            return 200, resp, None, result
    else:
        result = "fail"
        print("测试结果：失败！！！  " + str(status))
        print('返回的数据：' + str(r.text))
        #return status, resp.decode('utf-8'), None, result
        return status, resp, None, result
