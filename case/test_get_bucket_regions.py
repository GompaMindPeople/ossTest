import json
import time

import pytest
import yaml
import case.common as common
from service.OssService import OSSService




def test_get_region(oss):
    data = common.GetData()
    region = oss.GetRegion(data)
    assert "请求成功" in region
    loads = json.loads(region)
    lists = loads["data"]["lists"]
    assert len(lists) > 0
