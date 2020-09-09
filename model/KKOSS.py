from server.HttpClient import HttpClient
import re
import time
from server.Signature import Signature
import json
import common.yaml_utils as yamlUtils

# 定义装饰器
def InjectionHttpClient(func):
    def wrapper(*args, **kargs):
        lines = list(args)[:]
        new_args = list()
        index = 0
        for _, line in enumerate(lines):
            new_args.insert(index, line)
            index = index + 1
        # 在最后的参数中注入 一个 httpClient.
        new_args.insert(index, lines[0].httpClient)
        f = func(*tuple(new_args), **kargs)
        return f

    return wrapper


def MakeDefaultHeader():
    return {"Content-Type": "application/json"}


class KKOss:
    secretKey = ""
    accessKet = ""
    httpClient = None

    def __init__(self, host, secretKey):
        self.httpClient = HttpClient()
        self.httpClient.MakeSession(host)
        self.secretKey = secretKey
        yaml = yamlUtils.ReadYaml("../config/config.yaml")
        self.accessKet = yaml["accessKet"]

    @InjectionHttpClient
    def SendOssOps(self, params, module, httpClient):
        header = MakeDefaultHeader()
        if "module" not in params:
            params["module"] = module
        if "version" not in params:
            params["version"] = "v1"
        params["timestamp"] = str(int(time.time()))
        params["access_key"] = self.accessKet
        sign = Signature().makeSign(params=params, secret_key=self.secretKey)
        params["sign"] = sign
        encode = json.dumps(params).encode('utf-8')
        response = httpClient.SendRequest("/oss", "POST", header, encode)
        return response.text

    """
        发送对桶的 操作 
    """

    def SendOssOpsByBucket(self, params):
        return self.SendOssOps(params, "buckets")

    def SendOssOpsByObject(self, params):
        return self.SendOssOps(params, "Objects")