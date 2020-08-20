import sys
import subprocess
from pdf2image import convert_from_path

# Для Windows

def png_to_txt(file_name,path):
    out_put = path+'\\file_txt'
    lang = '-l rus+eng'
    command = 'tesseract.exe {0} {1} {2}'.format(file_name, out_put, lang)
    print('COMMAND: ', command)
    subprocess.call(command)


def ocr(filename, path):
    images = convert_from_path(filename)
    i = 0
    for target_list in images:
        i = +1
        f_name = path+'\\'+'file_{0}.png'.format(i)
        target_list.save(f_name)
        png_to_txt(f_name,path)


# main
file_in 	= r'C:\Users\dvi\Desktop\Договор ФА000134 от 08.05.2020.pdf'
out_path 	= r'C:\Users\dvi\AppData\Local\Temp\out'

ocr(file_in, out_path)