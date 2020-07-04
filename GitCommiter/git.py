import os
import subprocess
from Downloader import download
from ExtactTags import extractTags

folderName = 'HousePricesSolution_Beginner'
fileTitle='house-prices-solution-beginner'
comment = '"Changes to house-prices-solution-beginner Notebook"'
repetition = 1

# Download tags

ll = extractTags()
noOfCommits = len(ll)
#done


def read_dates():
    f = open("Dates.txt", "r")
    for x in f:
        dateList.append(x.rstrip())
    f.close()


dateList = list()
read_dates()

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
        subprocess.check_call(['git'] + ['add', '*'])
        subprocess.check_call(['git'] + ['commit', '-m', comment])
        dateComplete = '--date="' + dateList[d] + '"'
        d = d+1
        subprocess.check_call(['git'] + ['commit', '--amend', '--no-edit', dateComplete])
