import json
import time

import pytest
import yaml
import case.common as common
from service.OssService import OSSService





def test_getBucketLifecycle(oss):
    bucket = common.GetBucketOne(oss, 0)

    data = common.GetData()
    data["bucket_id"] = bucket["id"]
    lifecycle = oss.GetBucketLifecycle(data)
    assert "请求成功" in lifecycle

    data = common.GetData()
    data["bucket_id"] = "999999999999999"
    lifecycle = oss.GetBucketLifecycle(data)
    assert "找不到该桶信息" in lifecycle
