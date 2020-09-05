import pytest
import common.yaml_utils as yamlUtils
from service.ossService import OSSService


@pytest.fixture(name="oss", scope="module")
def init():
    load = yamlUtils.ReadYaml("../config/config.yaml")
    url = load["url"]
    kk_oss = OSSService(url)
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
def Scene1(oss):
    print("before")
    yield
    print("after")
