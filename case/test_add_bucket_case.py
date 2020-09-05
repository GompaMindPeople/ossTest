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
def test_GetRegion(oss):
    data = common.GetData()
    result = oss.GetRegion(data)
    assert "请求成功" in result


def test_addBucket(oss):
    data1 = common.GetData()
    # 先获取到 地区列表
    region = oss.GetRegion(data1)
    assert "请求成功" in region
    data = common.GetData()
    data["storage_type"] = "1"
    addBucketCase = yamlUtils.ReadYaml("./AddBucket.yaml")
    jsonDict = json.loads(region)
    for k1 in addBucketCase["case"]:
        data["version_control"] = k1["version_control"]
        data["access_type"] = k1["access_type"]
        data["name"] = k1["name"]
        data["action"] = "add"
        for k in jsonDict["data"]["lists"]:
            time.sleep(10)
            data["region"] = k
            result = oss.KKOss.SendOssOpsByBucket(data)
            assert k1["result"] in result
            if "isDeleteBucket" in k1:
                if k1["isDeleteBucket"] == "0":
                    continue
            jsonResult = json.loads(result)
            d = common.GetData()
            d["bucket_id"] = jsonResult["data"]["bucket_id"]
            time.sleep(10)
            result = oss.DeleteBucket(d)
            assert "删除成功" in result
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_add_bucket_case'])
