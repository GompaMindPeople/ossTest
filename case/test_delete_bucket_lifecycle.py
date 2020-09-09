import json
import time

import pytest
import yaml
import case.common as common
from service.OssService import OSSService



def test_deleteBucketLifecycle(oss):
    bucketName = "lifecycle1"
    one = common.AddBucketOne(oss, bucketName)
    assert "" in one["msg"]
    bucketId = one["data"]["bucket_id"]
    time.sleep(10)
    try:
        lifecycleName = "li123"
        lifecycle = common.AddBucketLifecycle(oss, bucketId, lifecycleName)
        assert "操作成功" in lifecycle["msg"]
        time.sleep(20)
        data = common.GetData()
        data["name"] = lifecycleName
        data["bucket_id"] = bucketId
        bucket_lifecycle = oss.DeleteBucketLifecycle(data)
        assert "删除成功" in bucket_lifecycle
        time.sleep(20)
    except Exception as e:
        print(e)
    finally:
        data = common.GetData()
        data["bucket_id"] = bucketId
        bucket = oss.DeleteBucket(data)
        assert "删除成功" in bucket

