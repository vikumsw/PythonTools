import os
import subprocess
from Downloader import download
from ExtactTags import extractTags
from DateGenerator import genDates, read_dates


def getFolderName(title):
    l = len(title)
    folderName = ""
    ConvertNextToUpper =False
    for i, c in zip(range(l),title):
        if i == 0:
            folderName = folderName + c.upper()
        elif c == '_' or c == '-':
            ConvertNextToUpper = True
        else:
            if ConvertNextToUpper:
                folderName = folderName + c.upper()
                ConvertNextToUpper = False
            else:
                folderName = folderName + c
    print(folderName)
    return folderName


def doGitStuff():
    subprocess.check_call(['git'] + ['add', '*'])
    try:
        subprocess.check_call(['git'] + ['commit', '-m', comment])
    except subprocess.CalledProcessError as error:
        print(error)
    dateComplete = '--date="' + dateList[d] + '"'
    subprocess.check_call(['git'] + ['commit', '--amend', '--no-edit', dateComplete])

fileTitle='classification-with-scikit-learn'
folderName = getFolderName(fileTitle)
comment = '"Changes to classification-with-scikit-learn Notebook"'
repetition = 1
genDates(2020, 4, 15)
# Download tags
ll = extractTags()
noOfCommits = len(ll)
#done


dateList = list()
read_dates(dateList)
download(fileTitle, ll)

os.chdir(r"E:\Personal\Repositories\KaggleNotebooks")
os.system("mkdir " + folderName)

d = 0
for k in range(0, repetition):
    for i in range(0, noOfCommits):
        add = '(' + str(i) + ')'

        filename = fileTitle + add + '.ipynb'

        cmd = 'copy "E:\Personal\Repositories\PythonTools\GitCommiter\\res\\' + filename + '" ' + \
              '"E:\Personal\Repositories\KaggleNotebooks\\' + folderName + '\\' + fileTitle + '.ipynb"'
        print(cmd)
        os.system(cmd)
        doGitStuff()
        d = d + 1