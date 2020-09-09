import json
import time

import pytest
import yaml
import case.common as common
from service.OssService import OSSService



def test_putBucketPolicy(oss):
    authorized_resources_type_case = ["", "1", 1, "2", "0", "-1"]
    authorized_resources_type_case_result = ["该授权资源不可用，请重新选择", "设置成功", "设置成功",
                                             "该授权资源不可用，请重新选择", "该授权资源不可用，请重新选择",
                                             "该授权资源不可用，请重新选择"]

    account_id_case = ["", "asdsad", "123456789", "1264549575379359"]
    account_id_case_result = ["找不到授权用户", "找不到授权用户", "找不到授权用户", "设置成功"]

    authorized_operation_type_case = ["1", "2", "3", "4", "0", "asb"]
    authorized_operation_type_case_result = ["设置成功", "设置成功", "设置成功", "该授权操作不可用，请重新选择",
                                             "该授权操作不可用，请重新选择", "该授权操作不可用，请重新选择"]
    data = common.GetData()
    bucket_list = oss.GetBucketList(data)
    listJson = json.loads(bucket_list)

    data = common.GetData()
    data["id"] = listJson["data"]["data"][0]["id"]
    index = 0
    for value1 in authorized_resources_type_case:
        data["authorized_resources_type"] = value1
        data["account_id"] = "1264549575379359"
        data["authorized_operation_type"] = "1"
        result = oss.PutBucketPolicy(data)
        assert authorized_resources_type_case_result[index] in result
        index += 1

    index = 0
    for value2 in account_id_case:
        data["authorized_resources_type"] = "1"
        data["account_id"] = value2
        data["authorized_operation_type"] = "1"
        result = oss.PutBucketPolicy(data)
        assert account_id_case_result[index] in result
        index += 1

    index = 0
    for value3 in authorized_operation_type_case:
        data["authorized_resources_type"] = "1"
        data["account_id"] = "1264549575379359"
        data["authorized_operation_type"] = value3
        result = oss.PutBucketPolicy(data)
        assert authorized_operation_type_case_result[index] in result
        index += 1

    # data["resource_path"]
    # data["condition_type"]
    # data["condition_ip"]
    data = common.GetData()
    data["id"] = ""
    data["authorized_resources_type"] = "1"
    data["account_id"] = "1264549575379359"
    data["authorized_operation_type"] = "1"
    result = oss.PutBucketPolicy(data)
    assert "参数有误" in result
