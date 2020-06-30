def read_dates():
    f = open("Dates.txt", "r")
    for x in f:
        dateList.append(x.rstrip())
    f.close()


dateList = list()
read_dates()


os.chdir(r"E:\Personal\Repositories\KaggleNotebooks")
# subprocess.check_call(['git'] + ['status'])

for i in range(0, 21):
    if i == 0:
        add = '';
    else:
        add = ' (' + str(i) + ')'

    filename = 'beginners-basic-workflow-introduction' + add + '.ipynb'

    cmd = 'copy "E:\Personal\Repositories\PythonTools\GitCommiter\\res\\' + filename + '" ' + \
          '"E:\Personal\Repositories\KaggleNotebooks\BasicWorkflowIntroduction' \
          '\\beginners-basic-workflow-introduction.ipynb"'
    print(cmd)
    os.system(cmd)
    subprocess.check_call(['git'] + ['add', '*'])
    subprocess.check_call(['git'] + ['commit', '-m', r'"Changes to Basic WorkFlow Notebook"'])
    dateComplete = '--date="' + dateList[i] +'"'
    subprocess.check_call(['git'] + ['commit', '--amend', '--no-edit', dateComplete])