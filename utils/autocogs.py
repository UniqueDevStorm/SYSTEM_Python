import os


def AutoCogs(self):
    cogs = [i.replace(".py", "") for i in os.listdir("./cogs") if i.endswith(".py")]
    for i in cogs:
        self.load_extension(f"cogs.{i}")
        print(f"{i}.py On Ready.")
    self.load_extension('jishaku')
    print('jishaku On Ready.')

def AutoCogsReload(self):
    cogs = [i.replace(".py", "") for i in os.listdir("./cogs") if i.endswith(".py")]
    for i in cogs:
        self.reload_extension(f"cogs.{i}")
        print(f"{i}.py On Ready.")
    self.reload_extension('jishaku')
    print('jishaku On Ready.')