import yaml

"""
    从文件中读取yaml配置,并转换成一个对象
"""


def ReadYaml(filePath, mode="r"):
    f = open(filePath, mode, encoding="utf-8")
    cfg = f.read()
    load = yaml.load(cfg, Loader=yaml.BaseLoader)
    return load
