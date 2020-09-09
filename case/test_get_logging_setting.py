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


def test_getLoggingSetting(oss):
    bucket_list = common.GetBucketList(oss)
    data = common.GetData()
    for v in bucket_list:
        data["bucket_id"] = v['id']
        logging = oss.GetBucketLogging(data)
        assert "请求成功" in logging
