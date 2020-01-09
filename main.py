#coding = UTF-8

import hashlib
import os
import shutil

class DuplicateFiles:

    def rename_file(self, file_0, file_1):
        num = 0
        split_name = file_0.split('.')
        try:
            num += 1
            duplicate_file = f'{split_name[0]}-duplicate.{split_name[1]}'
        except:
            duplicate_file = f'{split_name[0]}-duplicate{num}.{split_name[1]}'
        os.renames(file_1, duplicate_file)
        return duplicate_file

    def move_file(self, file_0, file_1):
        duplicate_file = self.rename_file(file_0, file_1)
        if not os.path.exists('duplicate files'):
            os.makedirs('duplicate files')
        shutil.move(duplicate_file, 'duplicate files' + '/' + duplicate_file)


    def read_hash(self, file_0, file_1):

        hash_0 = hashlib.new('ripemd160')
        hash_0.update(open(file_0, 'rb').read())

        hash_1 = hashlib.new('ripemd160')
        hash_1.update(open(file_1, 'rb').read())

        if hash_0.digest() == hash_1.digest(): #run function for rename or delete file
            self.move_file(file_0, file_1)
            return True
        else:
            return False

    def run(self):
        files_0 = []
        files_1 = []
        for name_file in os.listdir('.'):
            if os.path.isfile(name_file):
                files_0.append(name_file)
                files_1.append(name_file)

        for file_0 in files_0:
            for file_1 in files_1:
                if file_0 != file_1:
                    confirmation = self.read_hash(file_0, file_1) #This variable confirmation is for check if this file is duplicate or not.
                    if confirmation == True:
                        files_0.remove(file_1)
                        files_1.remove(file_1)



Run = DuplicateFiles()
Run.run()
