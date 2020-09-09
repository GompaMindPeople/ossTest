import pytest
import common.yaml_utils as yamlUtils
import case.common
from service.OssService import OSSService


@pytest.fixture(name="oss", scope="module")
def init():
    load = yamlUtils.ReadYaml("../config/config.yaml")
    url = load["url"]
    secretkey = load["secretkey"]
    kk_oss = OSSService(url, secretkey)
    return kk_oss


"""
    定义通用的场景设计
"""


@pytest.fixture(scope="module")
def Scene(oss):
    print("before")
    yield
    print("after")


@pytest.fixture(scope="module")
def TempBucketScene(oss):
    bucketName = "tempbucket"
    one = case.common.AddBucketOne(oss, bucketName)
    assert "添加成功" in one["msg"]
    oss.TempBucket = one
    yield
    bucket = case.common.DeleteBucket(oss, one["data"]["bucket_id"])
    assert "删除成功" in bucket["msg"]
