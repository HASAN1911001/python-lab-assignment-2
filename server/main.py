from glob import glob
import shutil
import os
import zipfile
from subprocess import call

source_path = '../source/*'
destination_path = '../destination'
postfix = [1, 2, 3]

while True:
    source_object = glob(source_path)

    if len(source_object) > 0:

        object_path = source_object[0]
        object_name = object_path.split('\\')[-1].split('.')
        prefix = object_name[0]
        postfix2 = object_name[1]
        shutil.copy(object_path, '.')

        if postfix2 == 'py':
            call(["python", "{}".format('.'.join(object_name))])

        else:
            with open('.'.join(object_name), 'r') as f:
                file = f.readlines()

            newZip = zipfile.ZipFile('../destination/new.zip', 'w')
            for item in postfix:
                filename = prefix + '_' + str(item) + '.' + postfix2

                with open(filename, 'w') as f:
                    for i in range(item*10):
                        f.write(''.join(file[i]))

                newZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
                #shutil.copy(filename, f'{destination_path}/{filename}')
                os.remove(filename)

            newZip.extractall('../destination')

        os.remove(object_path)
        os.remove('.'.join(object_name))
