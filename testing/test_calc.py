#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time  :2020/10/8:16:53
# @Author:啊哩哩
# @File  :test_calc.py
import pytest
import yaml

from pythoncode.calc import Calculator


# 对计算器加法、除法功能进行测试
class TestCalc:
    # 对输入数据和预期结果参数化
    with open("datas/calc.yml", encoding="utf8") as f:
        # 获取字典数据
        datas = yaml.safe_load(f)["datas"]
        # 获取加法输入数据和预期结果
        adddata = datas["adds"]
        # 命名加法输入数据和预期结果
        addid = datas["addid"]
        # 获取除法输入数据和预期结果
        divdata = datas["divs"]
        # 命名除法输入数据和预期结果
        divid = datas["divid"]

    def setup_class(self):
        # 实例化计算器
        self.calc = Calculator()

    def setup(self):
        # 调用测试方法前打印计算
        print("开始计算")

    def teardown(self):
        # 调用测试方法前打印计算
        print("计算结束")

    # pytest参数化
    @pytest.mark.parametrize("a,b,expect", adddata, ids=addid)
    def test_addcalc(self, a, b, expect):
        # 判断是否为数值
        if isinstance(a, str) or isinstance(b, str):
            raise Exception("不支持字符串")
            return
        else:
            # 调用相加add()方法
            result = self.calc.add(a, b)
            # 避免浮点运算误差
            if isinstance(result, float):
                result = round(result, 2)
            # 断言参数化
        assert expect == result

    # 除法参数化
    @pytest.mark.parametrize("a,b,expected", divdata, ids=divid)
    def test_divcalc(self, a, b, expected):
        # 判断是否为数值
        if isinstance(a, str) or isinstance(b, str):
            raise Exception("不支持字符串")
            return
        else:
            if b == 0:
                # 除数为0时抛出异常
                raise Exception("除数不能为0")
            else:
                # 调用相除div()方法
                result = self.calc.div(a, b)
                # 避免浮点运算误差
                if isinstance(result, float):
                    result = round(result, 2)
                    # 断言参数化
                    assert expected == result