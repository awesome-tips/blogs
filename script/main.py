# from biplist import *

import csv

items = list()

class Item(object):
    nickname = ''
    desc = ''
    blog = ''
    weibo = ''
    github = ''
    header = ''


def readCSV():

    # items = list()

    with open('iOS.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            item = Item()
            item.nickname = row['nickname']
            item.desc = row['desc']
            item.blog = row['blog']
            item.weibo = row['weibo']
            item.github = row['github']
            item.header = row['header']

            items.append(item)
            print(item.nickname + "," + item.desc)

    # sorted(items)

tableTemplate = """
<table>
{rows}
</table>
"""

rowTemplate = """
<tr>
{row}
</tr>
"""

cellTemplate = """
<td id='{nickname}' style='width:180px'>
<p align='center'><a href='{blog}'><img src='{header}' height='150' width='150'/></a></p>
<h4 align='center'><a href='{blog}'>{nickname}</a></h4>
<h6 align='center'>{desc}</h6>
<p align='center'>
<a href='{weibo}'><img src='https://github.com/awesome-tips/blogs/blob/master/assets/weibo.png?raw=true' /></a>
<a href='{github}'><img src='https://github.com/awesome-tips/blogs/blob/master/assets/github.png?raw=true' /></a>
</p>
"""

def fillCell(item):
    if item is None:
        return ""

    return cellTemplate.format(nickname=item.nickname,
                             header=item.header,
                             blog=item.blog,
                             desc=item.desc,
                             weibo=item.weibo,
                             github=item.github)

def writeRow(items):

    row = ""
    for item in items:
        row += fillCell(item)

    return rowTemplate.format(row=row)

def writeTable():
    result = ""

    count = len(items)
    print('count: ' + str(count))
    if count == 0:
        return result

    row_count = int(count / 5)
    mod = count % 5
    if mod > 0:
        row_count += 1

    print("row count: " + str(row_count))
    for row in range(0, row_count):
        start = row * 5
        end = min((row + 1) * 5 - 1, count - 1)
        rowItems = items[start:end+1]
        result += writeRow(rowItems)

    return tableTemplate.format(rows=result)

def writeToFile(str):
    file = open("blog.md", "w+")
    file.write(str)
    file.close()

if __name__ == "__main__":
    readCSV()
    table = writeTable()
    print(table)
    writeToFile(table)