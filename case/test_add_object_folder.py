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
def test_addFolder(oss):
    data = common.GetData()
    data["bucket_id"] = 43
    data["name"] = "new_chrome_proxy.exe"
    result = oss.AddObjectFolder(data)
    assert "创建成功" in result
