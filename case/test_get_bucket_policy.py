import json
import time

import pytest
import yaml
import case.common as common
from service.OssService import OSSService




def test_getBucketPolicy(oss):
    data = common.GetData()
    bucket_list = oss.GetBucketList(data)
    listJson = json.loads(bucket_list)
    data = common.GetData()
    for v in listJson["data"]["data"]:
        data["id"] = v["id"]
        policy = oss.GetBucketPolicy(data)
        assert "获取成功" in policy
