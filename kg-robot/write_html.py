def main(input_html_file,out_html_file):
    fin = open(input_html_file, 'r',encoding="utf-8")
    fout = open(out_html_file, 'w',encoding="utf-8")
    # 读取日志写入htlm
    list_kg=[]
    with open('./test.log', 'r',encoding="utf-8") as f:
        for num, line in enumerate(f):
            list_kg.append(line)
        # print(list_kg)        
            
    for line in fin:
        # print(line)
        if line.strip() == 'var nodes = {};': # 在html中的<head>上一行添加如下内容
                fout.write('var links = ['+"".join(list_kg)+'];\n') # 将所有列表元素合并在一个字符串
        fout.write(line)

input_html_file='index.html' # 可视化模板
out_html_file='test.html'   # 输出结果
main(input_html_file,out_html_file)








