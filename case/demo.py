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
def test_GetRegion(oss):
    data = common.GetData()
    result = oss.GetRegion(data)
    assert "请求成功" in result
