import json
import logging
import time

import pytest
import yaml
import case.common as common
from service.OssService import OSSService






def test_putBucketVersion(oss):

    bucketName = "test-mul-version"
    one = common.AddBucketOne(oss, bucketName)
    bucketId = ""

    try:
        assert "添加成功" in one["msg"]
        bucketId = one["data"]["bucket_id"]

        TestPutMulVersionModel(oss, bucketId, "0", "设置成功")

        TestPutMulVersionModel(oss, bucketId, "1", "设置成功")

        TestPutMulVersionModel(oss, "", "1", '找不到该信息')

    except Exception as e:
        print("发生异常删除桶--->", bucketId, "--->", e)
        raise Exception(e)
    finally:
        time.sleep(10)
        bucket = common.DeleteBucket(oss, bucketId)
        print(bucket)


def TestPutMulVersionModel(oss, buckId, isOpen, result):
    mul_version = common.PutMulVersion(oss, buckId, isOpen)
    assert result in mul_version["msg"]
    return mul_version



