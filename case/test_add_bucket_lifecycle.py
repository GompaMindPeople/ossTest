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


def test_addBucketLifecycle(oss):
    data = common.GetData()
    name = "lifecycle1"
    bucket = common.GetBucketOne(oss, 0)
    data["days"] = 1
    data["bucket_id"] = bucket["id"]
    data["name"] = name
    data["status"] = 0
    lifecycle = oss.AddBucketLifecycle(data)
    assert "操作成功" in lifecycle
    time.sleep(5)
    one = common.DeleteBucketLifecycleOne(oss, bucket["id"], name)

    assert "删除成功" in one["msg"]

    data = common.GetData()
    data["bucket_id"] = bucket["id"]
    data["days"] = 0
    data["name"] = "aaaaaa"
    data["status"] = 0
    lifecycle = oss.AddBucketLifecycle(data)
    # '{"status":false,"errCode":"100001","msg":"过期删除天数必须大于0","data":[]}'
    assert "过期删除天数必须大于0" in lifecycle

    data = common.GetData()
    data["bucket_id"] = "99999999999999999"
    data["days"] = 1
    data["name"] = "aaaaaa"
    data["status"] = 0
    lifecycle = oss.AddBucketLifecycle(data)
    # '{"status":false,"errCode":"100001","msg":"找不到需要配置的桶信息","data":[]}'
    assert "找不到需要配置的桶信息" in lifecycle

    data = common.GetData()
    data["bucket_id"] = bucket["id"]
    data["days"] = 1
    data["name"] = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999" \
                   "99999999999999999999999999999999999999999999999999999999999999999999999999999 "
    data["status"] = 0
    lifecycle = oss.AddBucketLifecycle(data)
    # '{"status":false,"errCode":"100001","msg":"lifecycle_rules.1.name: String length must be less
    # than or equal to 128","data":[]}'
    assert "String length must be less than or equal to 128" in lifecycle
    # -----------------------------------------------------------
    time.sleep(3)
    name = "aaaaaa"
    data = common.GetData()
    data["bucket_id"] = bucket["id"]
    data["days"] = 1
    data["name"] = name
    data["status"] = 1
    lifecycle = oss.AddBucketLifecycle(data)
    # '{"status":false,"errCode":"100001","msg":"找不到需要配置的桶信息","data":[]}'
    assert "操作成功" in lifecycle

    time.sleep(5)
    one = common.DeleteBucketLifecycleOne(oss, bucket["id"], name)
    assert "删除成功" in one["msg"]
    # ---------------------------------------------------------------------------
    data = common.GetData()
    time.sleep(2)
    data["bucket_id"] = bucket["id"]
    data["days"] = 1
    data["name"] = "aaaaa"
    data["status"] = 0
    lifecycle = oss.AddBucketLifecycle(data)
    # '{"status":false,"errCode":"100001","msg":"can not set
    # lifecycle when bucket in action status lifecycle_setting","data":[]}'
    assert "操作成功" in lifecycle
    time.sleep(5)
    data = common.GetData()
    data["bucket_id"] = bucket["id"]
    data["days"] = 1
    data["name"] = "aaaaa"
    data["status"] = 0
    lifecycle = oss.AddBucketLifecycle(data)
    # '{"status":false,"errCode":"100001","msg":"Duplicated rule name: aaaaa","data":[]}'
    assert "Duplicated rule name" in lifecycle
    time.sleep(5)
    one = common.DeleteBucketLifecycleOne(oss, bucket["id"], "aaaaa")
