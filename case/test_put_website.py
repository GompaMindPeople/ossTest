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


def test_putWebsite(oss):
    bucket = common.GetBucketOne(oss, 0)
    data = common.GetData()

    data["id"] = bucket['id']
    data["default_page"] = "aaa.html"
    data["default_four_page"] = "404.html"
    wensite = oss.PutBucketWebsite(data)
    assert "设置成功" in wensite
