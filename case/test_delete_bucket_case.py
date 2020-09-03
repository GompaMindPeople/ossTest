import json
import time

import pytest
import yaml
from service.ossService import OSSService
import case.common as common


@pytest.fixture(name="oss")
def init():
    f = open("../config/config.yaml", 'r', encoding="utf-8")
    cfg = f.read()
    load = yaml.load(cfg, Loader=yaml.BaseLoader)
    url = load["url"]
    kk_oss = OSSService(url)
    return kk_oss


def GetRegion(oss):
    data = common.GetData()
    result = oss.GetRegion(data)
    assert "请求成功" in result


def CreateBucket(oss):
    data = common.GetData()
    data["storage_type"] = "1"
    data["version_control"] = "1"
    data["access_type"] = "1"
    data["name"] = "delete-name-test"
    data["region"] = "1"
    bucket = oss.AddBucket(data)
    return bucket


def test_DeleteBucket(oss):
    bucket = CreateBucket(oss)
    assert "添加成功" in bucket
    time.sleep(10)

    data = common.GetData()
    bucketJson = json.loads(bucket)
    bucket_ID = bucketJson["data"]["bucket_id"]
    data["bucket_id"] = bucket_ID
    result = oss.DeleteBucket(data)
    assert "删除成功" in result


def test_DeleteBucketByNull(oss):
    data = common.GetData()
    data["bucket_id"] = "99999999999999999"
    result = oss.DeleteBucket(data)
    assert "找不到需要配置的桶信息" in result


def test_DeleteBucketByNotEmpty(oss):
    data = common.GetData()
    # 暂时写死
    data["bucket_id"] = "89"
    result = oss.DeleteBucket(data)
    assert "Can\'t delete object storage bucket OSBucket(id=155, name=delete-bucket-not-empty) with data" in result
