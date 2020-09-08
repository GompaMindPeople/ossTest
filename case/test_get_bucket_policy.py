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


def test_getBucketPolicy(oss):
    data = common.GetData()
    bucket_list = oss.GetBucketList(data)
    listJson = json.loads(bucket_list)
    data = common.GetData()
    for v in listJson["data"]["data"]:
        data["id"] = v["id"]
        policy = oss.GetBucketPolicy(data)
        assert "获取成功" in policy
