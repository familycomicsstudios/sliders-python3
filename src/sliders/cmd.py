import os, sys
class CmdParser:
    def __init__(self, settings):
        self.conf = settings
    def parse(self, cmd, args):
        if args[0] == "help":
            self.help()
        elif args[0] == "info":
            self.info()
        elif args[0] == "exit":
            pass
        elif args[0] == "cd":
            os.chdir(args[1])
        elif args[0] == "settings":
            self.conf.settings[args[1]] = ' '.join(args[2:])
        elif args[0] == "run":
            try:
                os.system(self.conf.settings["run."+args[1]])
            except IndexError:
                os.system(self.conf.settings["run"])
        else:
            os.system(cmd)
        
        # Returns
        
        return self.conf
    
    def help(self):
        print("""
Help, eventually
""")
    def info(self):
        print("""
Info, eventually
""")
    
