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
name = ""


@pytest.mark.usefixtures("TempBucketScene")
def test_AddBucketTag(oss):
    bucket = common.GetBucketOne(oss, 0)
    data = common.GetData()
    data["id"] = bucket['id']
    data["key"] = "key1"
    data["value"] = "value1"
    wensite = oss.AddBucketTag(data)
    assert "添加成功" in wensite

#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_add_bucket_case'])
