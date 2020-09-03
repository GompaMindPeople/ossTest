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


def test_getBucketInfoIsNone(oss):
    data = common.GetData()
    data["bucket_id"] = "999999999999"
    info = oss.GetBucketInfo(data)
    assert "找不到该桶的相关信息" in info

    bucket_list = oss.GetBucketList(data)

    listJson = json.loads(bucket_list)
    list1 = listJson["data"]["data"]
    for k in list1:
        id1 = k["id"]
        data["bucket_id"] = id1
        bucket_info = oss.GetBucketInfo(data)
        assert "请求成功" in bucket_info
        print("桶id:" + id1 + "--->" + bucket_info)
