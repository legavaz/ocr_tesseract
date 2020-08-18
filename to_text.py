import subprocess
 
# Для Windows
file_name   =   'D:\\Py\\ocr\\out\\file_1.png'   
out_put     =   'out\\txt'
lang        =   '-l rus+eng'   
command     =   'tesseract.exe {0} {1} {2}'.format(file_name,out_put,lang)

print('COMMAND: ',command)
subprocess.call(command)



