"""
main directory : 'c:\\' +

commands 'ls' or 'dir' to show existing directory in current directory +

command 'cd' to move in directories when directory exists, otherwise throw an exception +

command deleting, creating, renaming files +

make command to view files with formats .txt .md and others +

create interface and logic such cmd +

*creating new functionality:
help command,
admin and user,
tree command,
finding deep directory file,
searching file by name

"""
import os

from dataclasses import dataclass, field

from core.modules import FileInfo, DirInfo


@dataclass
class Cmd:
    cur_directory: str = field(default='C:\\')
    prev_directory: str = field(default='C:\\')

    def ls(self) -> list[DirInfo | FileInfo]:
        dir_list = os.listdir(self.cur_directory)
        result: list[DirInfo | FileInfo] = []

        for n_dir in dir_list:
            temp_directory = os.path.join(self.cur_directory, n_dir)

            if os.path.isdir(temp_directory):
                result.append(DirInfo(created_at=os.path.getctime(temp_directory),
                                      modified_at=os.path.getmtime(temp_directory),
                                      name=n_dir))
            elif os.path.isfile(temp_directory):
                result.append(FileInfo(created_at=os.path.getctime(temp_directory),
                                       modified_at=os.path.getmtime(temp_directory),
                                       file_size=os.path.getsize(temp_directory),
                                       name=n_dir))

        return result

    def cd(self, new_dir:str = "\\") -> None:
        if new_dir == '-':
            self.cur_directory = self.prev_directory
            self.prev_directory = self.cur_directory[:]
            return

        self.prev_directory = self.cur_directory[:]

        if new_dir == '..':
            if self.cur_directory.rfind('\\') != -1 and self.cur_directory.count('\\') != 1:
                self.cur_directory = self.cur_directory[:self.cur_directory.rfind('\\')]
            else:
                self.cur_directory = 'C:\\'
        elif new_dir == '/':
            self.cur_directory = 'C:\\'
        elif new_dir.startswith('C:') and os.path.exists(new_dir):
            self.cur_directory = new_dir
        elif os.path.exists(os.path.join(self.cur_directory, new_dir)):
            self.cur_directory = os.path.join(self.cur_directory, new_dir)
        else:
            raise Exception(NotADirectoryError)

    def touch(self, file: str) -> None:
        with open(os.path.join(self.cur_directory, file), 'w'):
            pass

    def rm(self, file: str) -> None:
        if os.path.exists(os.path.join(self.cur_directory, file)):
            os.remove(os.path.join(self.cur_directory, file))

    def mv(self, old_name: str, new_name: str) -> None:
        if os.path.exists(os.path.join(self.cur_directory, old_name)):
            os.rename(os.path.join(self.cur_directory, old_name), os.path.join(self.cur_directory, new_name))

    def rd(self, file: str) -> list[str] | None:
        output: list[str] | None = None

        if os.path.exists(os.path.join(self.cur_directory, file)):
            f = open(os.path.join(self.cur_directory, file), 'r')
            output = f.readlines()

        return output

    @property
    def get_cdir(self) -> str:
        return self.cur_directory
