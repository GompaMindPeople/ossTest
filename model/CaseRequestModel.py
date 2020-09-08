"""

    需要对变量的生命周期做控制.
    比如 当  yaml用例文件中 具体的request  没有给定参数时,
    应该先从一个 全局的 默认池 中寻找数据, 如果全局的默认值都没有 则 置空

"""


class CaseRequestModel:
    requestId = 0
    route = ""
    Method = ""
    Header = {}
    Body = {}
    Params = ""
