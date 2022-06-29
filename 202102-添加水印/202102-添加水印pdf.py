from PyPDF2 import PdfFileWriter, PdfFileReader
import os
water_page_path = input("水印pdf地址：")
water_page = PdfFileReader(water_page_path).getPage(0)
rootdist = input("文件目录：")
fail_files = input("失败文件地址(txt)：")
list = []

from pathlib import Path
rootdist = Path(rootdist)
for p in rootdist.rglob('*.pdf'):
        list.append(str(p))


length = len(list)
for i in range(length):
    path = list[i]
    try:
        reader = PdfFileReader(path, strict=False)
        number = reader.getNumPages()
    except :
        print(' '+path)
        with open(fail_files,'a') as f:
            f.write(path+'\n')
            f.close()
        continue

    writer = PdfFileWriter()
    for x in range(number):
        page = reader.getPage(x)
        page.mergePage(water_page)
        writer.addPage(page)
    print('\r'+str(i+1)+'/'+str(length),end = '')
    os.remove(path)
    writer.write(open(path,'wb'))

input("press any key to exit")