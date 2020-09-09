import json
import time

import pytest
import yaml

import case.common as common

import common.yaml_utils as yamlUtils


# def test_sucess():
#     print("test sucess")
#
# def test_fail():
#     print("test fail")
@pytest.mark.usefixtures("TempBucketScene")
def test_GetFileInfo(oss):
    data = common.GetData()
    bucketId = oss.TempBucket["data"]["bucket_id"]
    data["id"] = 43
    data["key"] = "new_chrome_proxy.exe"
    result = oss.GetObjecFileInfo(data)
    assert "获取成功" in result
