import json

def assert_parm(res:str,**kwargs):
    """
    判断json中第一层级的 关键字
    """
    # {"reqId":"11d371069e2b11eab7598cec4b554198","status":0,"msg":"Success","sysTime":"20200525095719","result":0,"score":0.9681268}
    rest = json.loads(res)
    for k,v in kwargs.items():
        assert rest[k] == v
        



if __name__ == "__main__":
    assert_b = '{"reqId":"11d371069e2b11eab7598cec4b554198","status":0,"msg":"Success","sysTime":"20200525095719","result":0,"score":0.9681268}'
    assert_parm(assert_b,result=2)