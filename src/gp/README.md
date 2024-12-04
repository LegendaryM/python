操作步骤
1. 打开anaconda:  conda activate github_python
2. 拉取图片: cd src && python -m gp.main
3. 启动web页面： cd gp\web && node server.js，如果没有安装依赖包，先执行npm install 


url说明：
1. 行业板块资金流排行： `https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=500&po=1&np=1&fields=f12%2Cf13%2Cf14%2Cf62&fid=f62&fs=m%3A90%2Bt%3A2`
```shell script
"f12": "BK0737",
"f13": 90,
"f14": "软件开发",
"f62": 5930019584
```
2. 行业具体股份资金流排行： `https://push2.eastmoney.com/api/qt/clist/get?fid=f62&po=1&pz=100&pn=1&np=1&fltt=2&invt=2&fs=b%3ABK0737&fields=f12%2Cf14%2Cf62%2Cf66%2Cf72%2Cf3`
```shell script
fid: 按照哪个字段排序, 默认是f3

"f12": "002230",
"f14": "科大讯飞",
"f13": 0,           # 查询tag
"f62": 1092966480,  # 主力净流入
"f66": 1026171632   # 超大单净流入
"f72": 66794848     # 大单净流入
"f3": 1.1           # 当天涨幅 1.1%
```

