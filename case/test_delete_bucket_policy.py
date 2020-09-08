import json
import time

import pytest
import yaml
import case.common as common
from service.OssService import OSSService


@pytest.fixture(name="oss")
def init():
    f = open("../config/config.yaml", 'r', encoding="utf-8")
    cfg = f.read()
    load = yaml.load(cfg, Loader=yaml.BaseLoader)
    url = load["url"]
    kk_oss = OSSService(url)
    return kk_oss


def MakeBucketPolicy(oss, bucketId):
    data = common.GetData()
    data["id"] = bucketId
    data["authorized_resources_type"] = "1"
    data["account_id"] = "1264549575379359"
    data["authorized_operation_type"] = "1"
    policy = oss.PutBucketPolicy(data)
    assert "设置成功" in policy
    return json.loads(policy)


def test_deleteBucketPolicy(oss):
    data = common.GetData()
    bucket_list = oss.GetBucketList(data)
    listJson = json.loads(bucket_list)
    # 对一个桶创建一个 策略
    data["id"] = listJson["data"]["data"][0]["id"]
    policyId = MakeBucketPolicy(oss, data["id"])

    # 删除刚刚创建的策略
    data = common.GetData()
    data["id"] = listJson["data"]["data"][0]["id"]
    data["config_id"] = policyId["data"]["config_id"]
    policy = oss.DeleteBucketPolicy(data)
    assert "删除成功" in policy
    loads = json.loads(policy)
    assert data["id"] == loads["data"]["id"]

    data = common.GetData()
    data["id"] = "999999999999999999999"
    data["config_id"] = "9999999"
    policy = oss.DeleteBucketPolicy(data)
    assert "找不到Bucket授权策略的信息" in policy

    data = common.GetData()
    data["id"] = listJson["data"]["data"][0]["id"]
    data["config_id"] = "999999999999"
    policy = oss.DeleteBucketPolicy(data)
    assert "找不到Bucket授权策略的信息" in policy

