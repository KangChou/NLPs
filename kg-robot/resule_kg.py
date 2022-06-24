import os
import sys
import requests

def kg_view(entity):
	url = 'https://api.ownthink.com/kg/knowledge?entity=%s'%entity      # 知识图谱API
	sess = requests.get(url) # 请求
	text = sess.text # 获取返回的数据

	response = eval(text) # 转为字典类型
	knowledge = response['data']
	
	nodes = []
	for avp in knowledge['avp']:
		if avp[1] == knowledge['entity']:
			continue
		node = {'source': knowledge['entity'], 'target': avp[1], 'type': "resolved", 'rela':avp[0]}
		nodes.append(node)	
    
	for node in nodes:
		node = str(node)
		node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target')
		print(node+',')
    
if __name__=='__main__':
	kg_view('刘德华')
 	
 



# https://github.com/ownthink/KG-View/blob/master/index.html
# https://www.ownthink.com/docs/web_bot/