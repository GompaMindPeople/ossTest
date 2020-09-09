import json
import time

import pytest
import yaml
from service.OssService import OSSService
import case.common as common





def test_GetBucketList(oss):
    data = common.GetData()
    data["name"] = ""
    bucket_list = oss.GetBucketList(data)
    assert "请求成功" in bucket_list

    data = common.GetData()
    data["name"] = "dsfafassdfdsfsfsfdf"
    bucket_list = oss.GetBucketList(data)
    assert "请求成功" in bucket_list

    data = common.GetData()
    data["name"] = ""
    data["page"] = 1
    bucket_list = oss.GetBucketList(data)
    assert "请求成功" in bucket_list

    data = common.GetData()
    data["name"] = ""
    data["page"] = 0
    bucket_list = oss.GetBucketList(data)
    assert "请求成功" in bucket_list

    data = common.GetData()
    data["name"] = ""
    data["page"] = -1
    bucket_list = oss.GetBucketList(data)
    assert "请求成功" in bucket_list

    data = common.GetData()
    data["name"] = ""
    data["page"] = 9999999999
    bucket_list = oss.GetBucketList(data)
    assert "请求成功" in bucket_list

    data = common.GetData()
    data["name"] = "delete-bucket-not-empty"
    data["page"] = 1
    bucket_list = oss.GetBucketList(data)
    assert "请求成功" in bucket_list
    assert "delete-bucket-not-empty" in bucket_list
