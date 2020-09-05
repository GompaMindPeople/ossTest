import pytest  # 导入包


# if __name__ == "__main__":
#
#     test_list = ['demo.py']
#
# # 用pytest模块的main()方法，参数为上面定义好的列表或者元组。
#
#     pytest.main(test_list)
# pytest.main(['-s','demo.py'])  # 也可以这样写，这样写和上面那样写会运行结果会有所不同，可以自己试试看。
class TestLogin:

    def setup(self):
        print("setup1")

    def teardown(self):
        print("teardown1")

    def test_sucess(self):
        print("test sucess2333")

    def test_fail(self):
        print("test fail2333333333")
