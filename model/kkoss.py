from server.httpClient import HttpClient
import re


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
    return {}


class KKOss:
    host = ""
    httpClient = None

    def __init__(self, host):
        self.httpClient = HttpClient()
        self.httpClient.MakeSession(host)

    @InjectionHttpClient
    def SendOssOps(self, params, module, httpClient):
        header = MakeDefaultHeader()
        if "module" not in params:
            params["module"] = module
        if "version" not in params:
            params["version"] = "v1"
        if "timestamp" not in params:
            params["timestamp"] = "1"

        response = httpClient.SendRequest("/oss", "POST", header, params)
        return response.text

    """
        发送对桶的 操作 
    """

    def SendOssOpsByBucket(self, params):
        return self.SendOssOps(params, "buckets")
