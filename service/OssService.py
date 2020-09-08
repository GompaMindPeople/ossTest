from model.KKOSS import KKOss


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
        new_args.insert(index, lines[0].KKOss)
        f = func(*tuple(new_args), **kargs)
        return f

    return wrapper


class OSSService:

    def __init__(self, host, secretkey):
        self.KKOss = KKOss(host, secretkey)

    @InjectionHttpClient
    def GetRegion(self, data, client):
        data["action"] = "get_regions"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def DeleteBucket(self, data, client):
        data["action"] = "delete"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def AddBucket(self, data, client):
        data["action"] = "add"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketList(self, data, client):
        data["action"] = "get_lists"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketInfo(self, data, client):
        data["action"] = "get_info"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketAcl(self, data, client):
        data["action"] = "get_acl"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketPolicy(self, data, client):
        data["action"] = "get_policy"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def PutBucketPolicy(self, data, client):
        data["action"] = "put_policy"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def DeleteBucketPolicy(self, data, client):
        data["action"] = "delete_policy"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketLifecycle(self, data, client):
        data["action"] = "get_lifecycle"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def AddBucketLifecycle(self, data, client):
        data["action"] = "add_lifecycle"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def DeleteBucketLifecycle(self, data, client):
        data["action"] = "delete_lifecycle"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def PutBucketMulVersion(self, data, client):
        data["action"] = "put_version"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketMulVersion(self, data, client):
        data["action"] = "get_version"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketLogging(self, data, client):
        data["action"] = "get_logging"
        result = client.SendOssOpsByBucket(data)
        return result

    """
        获取可选的日志存储桶
    """
    @InjectionHttpClient
    def GetBucketLoggingBuckets(self, data, client):
        data["action"] = "get_logging_buckets"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def PutBucketLogging(self, data, client):
        data["action"] = "put_logging"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def PutBucketWebsite(self, data, client):
        data["action"] = "put_website"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketWebsite(self, data, client):
        data["action"] = "get_website"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def PutBucketReferer(self, data, client):
        data["action"] = "put_referer"
        result = client.SendOssOpsByBucket(data)
        return result

    @InjectionHttpClient
    def GetBucketReferer(self, data, client):
        data["action"] = "get_referer"
        result = client.SendOssOpsByBucket(data)
        return result
