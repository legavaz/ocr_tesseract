import sys
import subprocess
from pdf2image import convert_from_path, convert_from_bytes

# Для Windows
def png_to_txt(file_name):    
    out_put     =   'out\\file_txt'
    lang        =   '-l rus+eng'   
    command     =   'tesseract.exe {0} {1} {2}'.format(file_name,out_put,lang)
    print('COMMAND: ',command)
    subprocess.call(command)

def ocr(filename,path):
    images = convert_from_path(filename)
    i = 0    
    for target_list in images:
        i = +1
        f_name  =   path+'\\'+'file_{0}.png'.format(i)
        target_list.save(f_name) 
        png_to_txt(f_name)


file_in     =   r'D:\Py\ocr\sch.pdf'
out_path    =   r'D:\Py\ocr\out'

ocr(file_in,out_path)


# if __name__=='__main__':
#     if len(sys.argv)==3:
#         print('конвертация:{0} -> {1}'.format(sys.argv[1],sys.argv[2]))
#         array   =   convert_save(sys.argv[1],sys.argv[2])
#     else:
#         print('arg1 - in pdf,arg2 - out path')