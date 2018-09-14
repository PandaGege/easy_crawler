打包
python setup.py sdist build

安装
python setup.py install

服务启动，请查看help
ecserver --help


客户端:
from easy_crawler import Client
cli = Client('zk_server=localhost:2181')            #其它参数见help(Client)
res = cli.request(**kws)                  #参数和返回结果见help(Client.request)

print res.status, res.body, res.code, res.headers...

selector = res.selector         #如果body为html,也可以res.html_selector
name = selector.xpath('//div[@id="name"]/text()')[0]
selector = res.xml_selector     #如果body为xml
json = res.json                 # 如果body为json格式字符串



备忘：
python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. crawler.proto
