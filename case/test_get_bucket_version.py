import json
import time

import pytest
import yaml
import case.common as common
from service.ossService import OSSService


@pytest.fixture(name="oss")
def init():
    f = open("../config/config.yaml", 'r', encoding="utf-8")
    cfg = f.read()
    load = yaml.load(cfg, Loader=yaml.BaseLoader)
    url = load["url"]
    kk_oss = OSSService(url)
    return kk_oss


def test_getBucketMulVersion(oss):
    one = common.AddBucketOne(oss, "get-bucket-mul-version")
    bucketId = one["data"]["bucket_id"]

    mul_version = oss.GetBucketMulVersion(oss, bucketId)
    assert "请求成功" in mul_version

    version = common.PutMulVersion(oss, bucketId, "0")

    assert "设置成功" in version["msg"]
    assert 0 in version["data"]["is_open"]

    version = common.PutMulVersion(oss, bucketId, "0")

    assert "设置成功" in version["msg"]
    assert 0 in version["data"]["is_open"]

    version = common.PutMulVersion(oss, bucketId, "1")
    assert "设置成功" in version["msg"]
    assert 1 in version["data"]["is_open"]

    # Todo: 喵喵喵....之后在写吧
