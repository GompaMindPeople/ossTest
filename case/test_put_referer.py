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


def test_putReferer(oss):
    bucket = common.GetBucketOne(oss, 0)
    data = common.GetData()

    data["id"] = bucket['id']
    data["referer_list"] = "www.baidu.com"
    data["refer_status"] = "on"
    logging = oss.PutBucketReferer(data)
    #  '{"status":true,"errCode":0,"msg":"配置防盗链成功","data":{"id":43}}'
    assert "配置防盗链成功" in logging
