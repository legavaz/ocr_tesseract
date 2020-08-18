import sys
from pdf2image import convert_from_path, convert_from_bytes


def convert_save(filename,path):
    images = convert_from_path(filename)
    i = 0
    array_file_png  =   []
    for target_list in images:
        i = +1
        f_name  =   path+'\\'+'file_{0}.png'.format(i)
        target_list.save(f_name) 
        array_file_png.append(f_name)
    return array_file_png


if __name__=='__main__':
    if len(sys.argv)==3:
        print('конвертация:{0} -> {1}'.format(sys.argv[1],sys.argv[2]))
        convert_save(sys.argv[1],sys.argv[2])
    else:
        print('arg1 - in pdf,arg2 - out path')



