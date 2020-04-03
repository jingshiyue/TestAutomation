# TestAutomation

### 项目结构

|文件夹|内容|
|---|---|
|product_manage|项目管理|
|testcase_manage|接口测试|

### 描述用例的数据格式

```json
{
    "input": {
        "url": "http://10.20.5.171:9020/sso/userverify",
        "method": "POST",
        "role": "<Role: 测试项目 超级管理员>",
        "json_data": {
            "data": {
                "appid": "EXWSP",
                "token": ""
            }
        }
    },
    "output": {
        "status_code": [
            200
        ],
        "expect_body": [
            {
                "message": "OK"
            },
            {
                "data": "None",
                "phone": "18780373592",
                "realname": "完美"
            }
        ]
    }
}
```

