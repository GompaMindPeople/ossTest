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
def test_GetFileVersionList(oss):
    data = common.GetData()
    bucketId = oss.TempBucket["data"]["bucket_id"]
    data["id"] = 43
    result = oss.GetObjectFileVersionList(data)
    assert "获取成功" in result
