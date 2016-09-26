#!/usr/bin/env python

import argparse
import os
import re
import shutil

TEMPLATE_DIR = 'project_template'
PACKAGE_NAME_PLACEHOLDER  = 'PACKAGE_NAME'
PACKAGE_NAME_REGEX = re.compile(r'^\w+$')


def getAllFilesInDir(directory):
    files = []
    dirs = []
    for root, directories, filenames in os.walk(directory):
        for f in filenames:
            files.append(os.path.join(root, f))
        for d in directories:
            dirs.append(os.path.join(root, d))
    return (files, dirs)


def createProjectFiles(templateDir, destinationDir, projectName):
    os.mkdir(destinationDir)

    files, dirs = getAllFilesInDir(templateDir)
    for srcDir in dirs:
        destDir = srcDir.replace(TEMPLATE_DIR, destinationDir)
        destDir = destDir.replace(PACKAGE_NAME_PLACEHOLDER, projectName)
        os.mkdir(destDir)
    for srcFile in files:
        destFile = srcFile.replace(TEMPLATE_DIR, destinationDir)
        destFile = destFile.replace(PACKAGE_NAME_PLACEHOLDER, projectName)
        shutil.copyfile(srcFile, destFile)
        shutil.copymode(srcFile, destFile) # ensures executable bits are copied


def replaceTextInFile(filename, textToReplace, newText):
    with open(filename) as f:
        modifiedContents = f.read().replace(textToReplace, newText)
    with open(filename, 'w') as f:
        f.write(modifiedContents)


def replaceTextRecursively(rootDir, textToReplace, newText):
    files, dirs = getAllFilesInDir(rootDir)
    for fname in files:
        replaceTextInFile(fname, textToReplace, newText)


def createProjectBoilerplate(templateDir, projectName, projectDir=None):
    if not projectDir:
        projectDir = projectName
    if os.path.isdir(projectDir):
        raise ValueError('Directory "{:s}" already exists'.format(projectDir))
    if not PACKAGE_NAME_REGEX.match(projectName):
        raise ValueError('"{:s}" is not a valid package name'.format(projectName))

    createProjectFiles(templateDir, projectDir, projectName)
    replaceTextRecursively(projectDir, PACKAGE_NAME_PLACEHOLDER, projectName)


if __name__ == '__main__':
    # Parse command lime arguments
    parser = argparse.ArgumentParser(
        description='Generate Python package/script boilerplate')
    parser.add_argument('package_name', type=str,
                        help='name of top-level package of project')
    parser.add_argument('-o', '--outputDir', dest='output_dir', type=str,
                        help='directory to store generated project files')
    args = parser.parse_args()

    # Generate package
    createProjectBoilerplate(TEMPLATE_DIR, args.package_name, args.output_dir)
