'''
读取2.xlsx中的内容列表输出
[1.0, 2.0, 'q', 'w', '@', 'asd', 'asd']
['asd', 'a', 'zxc', 123.0, 123.0, '1ew', 'QWW']
'''
import xlrd
def readExcel():
    data = xlrd.open_workbook('P:\\Users\\jared\\Documents\\2.xlsx')
    table = data.sheets()[0]  # 打开第一张表 sheet1
    nrows = table.nrows  # 获取表的行数
    for i in range(nrows):  # 循环逐行打印
        print(table.row_values(i))  # 通过row_values来获取每行的值
readExcel()
