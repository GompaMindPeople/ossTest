import json
import time

import pytest
import yaml

import case.common as common

import common.yaml_utils as yamlUtils


# def test_sucess():
#     print("test sucess")
#
# def test_fail():
#     print("test fail")
@pytest.mark.usefixtures("Scene")
def test_deleteBucketTag(oss):
    bucket = common.GetBucketOne(oss, 0)
    data = common.GetData()
    data["id"] = bucket['id']
    tag = oss.GetBucketTag(data)
    data["bucket_id"] = bucket['id']
    loads = json.loads(tag)
    for v in loads["data"]:
        data["id"] = v["id"]
        wensite = oss.DeleteBucketTag(data)
        assert "删除成功" in wensite
        return

#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_add_bucket_case'])
