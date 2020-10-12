#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time  :2020/10/8:16:53
# @Author:啊哩哩
# @File  :test_calc.py
# 1、补全计算器（加减乘除）的测试用例
# 2、使用数据的数据驱动，完成加减乘除用例的自动生成
# 3、修改测试用例的收集规则，执行所有以 check_开头和test_ 开头的测试用例
# 4、创建 Fixture 方法实现执行测试用例前打印【开始计算】，
# 执行测试用例之后打印【计算结束】
# 5、将 Fixture 方法存放在conftest.py ，设置scope=module


class TestCalc:

    # 加法测试用例
    def test_addcalc(self, get_adddatas, get_calc):
        # 判断是否为数值
        if isinstance(get_adddatas[0], str) or isinstance(get_adddatas[1], str):
            raise Exception("不支持字符串")
            return
        else:
            # 调用相加add()方法
            result = get_calc.add(get_adddatas[0], get_adddatas[1])
            # 避免浮点运算误差
            if isinstance(result, float):
                result = round(result, 2)
            # 断言参数化
        assert get_adddatas[2] == result

    # 减法测试用例
    def check_subcalc(self, get_subdatas, get_calc):
        # 判断是否为数值
        if isinstance(get_subdatas[0], str) or isinstance(get_subdatas[1], str):
            raise Exception("不支持字符串")
            return
        else:
            # 调用相减sub()方法
            result = get_calc.sub(get_subdatas[0], get_subdatas[1])
            # 避免浮点运算误差
            if isinstance(result, float):
                result = round(result, 2)
            # 断言参数化
        assert get_subdatas[2] == result

    # 乘法测试用例
    def check_mulcalc(self, get_muldatas, get_calc):
        # 判断是否为数值
        if isinstance(get_muldatas[0], str) or isinstance(get_muldatas[1], str):
            raise Exception("不支持字符串")
            return
        else:
            # 调用相乘mul()方法
            result = get_calc.mul(get_muldatas[0], get_muldatas[1])
            # 避免浮点运算误差
            if isinstance(result, float):
                result = round(result, 2)
            # 断言参数化
        assert get_muldatas[2] == result

    # 除法测试用例
    def check_divcalc(self, get_divdatas, get_calc):
        # 判断是否为数值
        if isinstance(get_divdatas[0], str) or isinstance(get_divdatas[1], str):
            raise Exception("不支持字符串")
            return
        else:
            if get_divdatas[1] == 0:
                # 除数为0时抛出异常
                raise Exception("除数不能为0")
                return
            else:
                # 调用相除div()方法
                result = get_calc.div(get_divdatas[0], get_divdatas[1])
                # 避免浮点运算误差
                if isinstance(result, float):
                    result = round(result, 2)
                    # 断言参数化
                    assert get_divdatas[2] == result
