from dataclasses import dataclass, field

from core.cmd import Cmd


@dataclass
class Shell:
    cmd: Cmd = field(default=Cmd(), init=False)

    def execute(self, commands: list[str]) -> None | str:
        command = commands[0]
        output = None
        match command:
            case 'ls' | 'dir':
                output = self.cmd.ls()
            case 'cd':
                if len(commands) > 1:
                    self.cmd.cd(commands[1])
                else:
                    self.cmd.cd()
            case 'touch' | 'create':
                self.cmd.touch(commands[1])
            case 'rm' | 'remove':
                self.cmd.rm(commands[1])
            case 'mv' | 'rename':
                self.cmd.mv(commands[1], commands[2])
            case 'rd' | 'read':
                output = self.cmd.rd(commands[1])
            case 'help':
                ...
            case _:
                return f'{command} is not recognized as an internal or external command operable program or batch file.'
        return output

    @property
    def get_current_directory(self) -> str:
        return self.cmd.get_cdir
