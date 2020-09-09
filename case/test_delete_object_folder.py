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
def test_deleteFolder(oss):
    data = common.GetData()
    data["bucket_id"] = 43
    data["key"] = "new_chrome_proxy.exe"
    data["is_version"] = 0
    result = oss.DeleteObjectFolder(data)
    assert "操作成功" in result
