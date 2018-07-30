import click
import setuptools
import shutil
import os
import fileinput

@click.command("convert")
@click.argument('oldProject')
@click.argument('outProject')
@click.argument('name')
def createProject(oldproject, outproject, name):
    shutil.copytree("templateIntellij", outproject)
    shutil.copytree(oldproject, outproject + "/src")
    os.rename(outproject + "/rename.iml", outproject + "/%s.iml" % name)
    with fileinput.FileInput(outproject + "/.idea/modules.xml", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("rename", name), end='')

if __name__ == "__main__":
    createProject()