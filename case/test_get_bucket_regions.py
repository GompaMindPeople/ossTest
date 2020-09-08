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


def test_get_region(oss):
    data = common.GetData()
    region = oss.GetRegion(data)
    assert "请求成功" in region
    loads = json.loads(region)
    lists = loads["data"]["lists"]
    assert len(lists) > 0
