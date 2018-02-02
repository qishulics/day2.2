import pytest
import allure

class Test_abc():
    @allure.step(title="第一个测试")
    def test_asd(self):
        assert 1


# if __name__ == '__main__':
#     pytest.main("-s --alluredir report test_001.py")