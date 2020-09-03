import json
import time

import pytest
import yaml
import case.common as common
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


def test_getBucketAcl(oss):
    data = common.GetData()
    bucket_list = oss.GetBucketList(data)

    loads = json.loads(bucket_list)

    for v in loads["data"]["data"]:
        data = common.GetData()
        data["bucket_id"] = v["id"]
        acl = oss.GetBucketAcl(data)
        assert "请求成功" in acl
        aclJson = json.loads(acl)
        access = aclJson["data"]["access"]
        assert JudgeAccess(access, v["access_type"])


# 判断访问的权限是否一致
def JudgeAccess(access, accessType):
    if accessType == 1:
        return access == "private"
    if accessType == 2:
        return access == "public-read"
    if accessType == 3:
        return access == "public-read-write"
    return False
