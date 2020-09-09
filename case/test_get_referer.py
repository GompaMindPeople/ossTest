import json
import time

import pytest
import yaml

import case.common as common


# import common.yaml_utils as yamlUtils


@pytest.fixture()
def Scene(oss):
    print("before")
    yield
    print("after")


def test_getReferer(oss):
    bucket = common.GetBucketOne(oss, 0)
    data = common.GetData()
    data["id"] = bucket['id']
    wensite = oss.GetBucketReferer(data)
    # '{"status":true,"errCode":0,"msg":"获取防盗链成功","data":{"referer_list":"www.baidu.com","refer_status":true}}'
    assert "获取防盗链成功" in wensite
