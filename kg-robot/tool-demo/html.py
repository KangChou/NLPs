def main():
    fin = open('index.html', 'r',encoding="utf-8")
    fout = open('test.html', 'w',encoding="utf-8")

    for line in fin:
        print(line)
        if line.strip() == '<head>': # 在html中的<head>上一行添加如下内容
            fout.write('\t\t<link rel="stylesheet" type="text/css" href="css/style.css">\n')
        fout.write(line)

if __name__ == '__main__':
    main()