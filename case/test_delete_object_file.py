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
def test_deleteFile(oss):
    data = common.GetData()
    data["bucket_id"] = 43
    data["key"] = "new_chrome_proxy.exe"
    result = oss.DeleteObjectFile(data)
    assert "删除成功" in result
