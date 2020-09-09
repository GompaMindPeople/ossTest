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


def test_getLoggingBucket(oss):
    data = common.GetData()
    logging = oss.GetBucketLoggingBuckets(data)
    assert "请求成功" in logging
