from dataclasses import dataclass, field

from core.modules import FileInfo, DirInfo
from core.shell import Shell


@dataclass
class View:
    terminal: Shell = field(default=Shell(), init=False)

    def run(self) -> None:
        while True:
            print(self.terminal.get_current_directory, end='>')
            commands = input().split()

            output = self.terminal.execute(commands)

            if output is not None:
                self._show_content(output)

    @staticmethod
    def _show_content(content) -> None:
        if isinstance(content, list):
            for info in content:
                if isinstance(info, FileInfo):
                    print(f'{info.get_m_date} \t\t{info.get_size[0:8]} {info.name}')
                elif isinstance(info, DirInfo):
                    print(f'{info.get_m_date} \t\t<DIR>\t\t {info.name}')
                else:
                    print(info)

        elif isinstance(content, str):
            print(content)
