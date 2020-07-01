import os
import subprocess

folderName = 'BasicFeatureVisualizations'
fileTitle='basic-feature-visualizations'
comment = '"Changes to basic visualizations Notebook"'
noOfCommits=7

def read_dates():
    f = open("Dates.txt", "r")
    for x in f:
        dateList.append(x.rstrip())
    f.close()


dateList = list()
read_dates()


os.chdir(r"E:\Personal\Repositories\KaggleNotebooks")
# subprocess.check_call(['git'] + ['status'])

for i in range(0, noOfCommits):
    if i == 0:
        add = '';
    else:
        add = ' (' + str(i) + ')'

    filename = fileTitle + add + '.ipynb'

    cmd = 'copy "E:\Personal\Repositories\PythonTools\GitCommiter\\res\\' + filename + '" ' + \
          '"E:\Personal\Repositories\KaggleNotebooks\\' + folderName + '\\' + fileTitle + '.ipynb"'
    print(cmd)
    os.system(cmd)
    subprocess.check_call(['git'] + ['add', '*'])
    subprocess.check_call(['git'] + ['commit', '-m', comment])
    dateComplete = '--date="' + dateList[i] + '"'
    subprocess.check_call(['git'] + ['commit', '--amend', '--no-edit', dateComplete])