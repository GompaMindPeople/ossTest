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


def test_getWebsite(oss):
    bucket = common.GetBucketOne(oss, 0)
    data = common.GetData()
    data["id"] = bucket['id']
    wensite = oss.GetBucketWebsite(data)
    assert "获取成功" in wensite
