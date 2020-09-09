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


def test_putLoggingBucket(oss):
    bucket = common.GetBucketOne(oss, 0)
    data = common.GetData()

    data["bucket_id"] = bucket['id']
    data["prefix"] = "aaa"
    data["is_open"] = 1
    logging = oss.GetBucketLoggingBuckets(data)

    loads = json.loads(logging)
    for v in loads["data"]["lists"]:
        data["to_bucket_id"] = v
        logging = oss.PutBucketLogging(data)
        assert "设置成功" in logging
        return
