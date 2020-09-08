import json
import time


def GetData():
    return {"access_key": "7qCOXq7GfZVpTPAyuAHI"}


def AddBucketOne(oss, bucketName):
    data = GetData()
    data["region"] = "1"
    data["storage_type"] = "1"
    data["version_control"] = "1"
    data["access_type"] = "1"
    data["name"] = bucketName
    data["action"] = "add"
    bucket = oss.AddBucket(data)
    time.sleep(10)
    return json.loads(bucket)


def AddBucketLifecycle(oss, bucketId, name):
    data = GetData()
    data["bucket_id"] = bucketId
    data["days"] = 1
    data["name"] = name
    data["status"] = 0
    lifecycle = oss.AddBucketLifecycle(data)
    return json.loads(lifecycle)


def GetBucketList(oss):
    data = GetData()
    bucket_list = oss.GetBucketList(data)
    loads = json.loads(bucket_list)
    return loads["data"]["data"]


def GetBucketOne(oss, index):
    return GetBucketList(oss)[index]


def DeleteBucketLifecycleOne(oss, bucketId, lifecycleName):
    data = GetData()
    data["bucket_id"] = bucketId
    data["name"] = lifecycleName
    lifecycle = oss.DeleteBucketLifecycle(data)
    loads = json.loads(lifecycle)
    return loads


def DeleteBucket(oss, bucketId):
    data = GetData()
    data["bucket_id"] = bucketId
    bucket = oss.DeleteBucket(data)
    return json.loads(bucket)


def PutMulVersion(oss, bucketId, isOpen):
    data = GetData()
    data["bucket_id"] = bucketId
    data["is_open"] = isOpen
    version = oss.PutBucketMulVersion(data)
    time.sleep(10)
    return json.loads(version)
