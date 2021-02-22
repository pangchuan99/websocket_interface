#项目说明
 websocket 接口自动化
#环境准备

	windows
	python3.6
	pytest4.5.6
	依赖包安装
	使用pip安装依赖包

	pip install -r requirements.txt

	运行用例
	运行用例，生成报告在./report

	pytest --alluredir ./report

#生成allure报告

   启动allure服务查看报告

   allure serve

#common
   是公共文件夹里面包含了所有的公共方法


#filename
  是读取文件的

#report
  是执行自动化用例后，查看测试报告，测试报告是allure

#TeseCaes
  是调用TestDase文件夹相对应文件，进行调用测试用例

#TeseDase
  是执行初步测试用例
