import sys
import os 
import re
import shutil
from transliterate import translit

def normalize(str):
    txt = translit(str, 'ru', reversed=True)
    txt = re.sub(r'[^a-zA-Z0-9]', '_', txt)
    return txt

def path(el):
    return el[1]


def all_files(path):
    return os.listdir(path)

def find_indx(txt):
    return txt.rfind('.')

def create_folder(path):
    try:
        os.mkdir(path + '\\sorted')
        os.mkdir(path + '\\sorted\\images')
        os.mkdir(path + '\\sorted\\video')
        os.mkdir(path + '\\sorted\\documents')
        os.mkdir(path + '\\sorted\\audio')
        os.mkdir(path + '\\sorted\\archives')
    except Exception:
        pass

def sort(path,c):
    
    for i in all_files(path):
            if i in {'sorted', 'images', 'video', 'documents', 'audio', 'archives'}:
                continue
            rtxt = normalize(i[:find_indx(i)])
            if i[find_indx(i):] in {'.jpeg', '.png', '.jpg', '.svg'}:
                os.rename(f'{path}\\{i}', f'{path}\\{rtxt}{i[find_indx(i):]}')
                shutil.move(f'{path}\\{rtxt}{i[find_indx(i):]}',f'{c}\\sorted\\images')

            if i[find_indx(i):] in {'.avi', '.mp4', '.mov', '.mkv'}:
                os.rename(f'{path}\\{i}', f'{path}\\{rtxt}{i[find_indx(i):]}')
                shutil.move(f'{path}\\{rtxt}{i[find_indx(i):]}',f'{c}\\sorted\\video')

            if i[find_indx(i):] in {'.doc','.docx', '.txt', '.pdf','.xlsx', '.pptx'}:
                os.rename(f'{path}\\{i}', f'{path}\\{rtxt}{i[find_indx(i):]}')
                shutil.move(f'{path}\\{rtxt}{i[find_indx(i):]}', f'{c}\\sorted\\documents')

            if i[find_indx(i):] in {'.mp3','.ogg', '.wav', '.amr'}:
                os.rename(f'{path}\\{i}', f'{path}\\{rtxt}{i[find_indx(i):]}')
                shutil.move(f'{path}\\{rtxt}{i[find_indx(i):]}', f'{c}\\sorted\\audio')

            if i[find_indx(i):] in {'.zip', '.gz', '.tar'}:
                os.rename(f'{path}\\{i}', f'{path}\\{rtxt}{i[find_indx(i):]}')
                arc1 = f'{rtxt}{i[find_indx(i):]}'
                arc1 = arc1[:find_indx(arc1)]
                os.mkdir(f'{c}\\sorted\\archives\\{arc1}')
                shutil.unpack_archive(f'{path}\\{rtxt}{i[find_indx(i):]}', f'{c}\\sorted\\archives\\{arc1}',f'{i[find_indx(i)+1:]}')
                for j in all_files(f'{c}\\sorted\\archives\\{arc1}'):
                    ntxt = normalize(j[:find_indx(j)])+j[find_indx(j):]
                    os.rename(f'{c}\\sorted\\archives\\{arc1}\\{j}',f'{c}\\sorted\\archives\\{arc1}\\{ntxt}')
                    
            if os.path.isdir(path+'\\'+i):
                os.rename(f'{path}\\{i}', f'{path}\\{rtxt}{i[find_indx(i):]}')
                sort(f'{path}\\{rtxt}{i[find_indx(i):]}', c)
        
                if len(os.listdir(f'{path}\\{rtxt}{i[find_indx(i):]}')) == 0:
                    shutil.rmtree(f'{path}\\{rtxt}{i[find_indx(i):]}')

def main():
    create_folder(path(sys.argv))
    sort(path(sys.argv),path(sys.argv))

if __name__ == '__main__':
    main()

