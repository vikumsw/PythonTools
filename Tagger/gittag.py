import sys

args = sys.argv[1:]

if len(args)!= 4:
    print('Invalid Usage!!')
    print('Correct Usage -> gitta.py <homeBranch> <targetBranch> <tagName> <tagMessage>')
    print('Stopping')
    quit()


print('Number of arguments:', len(args), 'arguments.')
print('Argument List:', str(args))


#git stash
#git checkout targetBranch
#git pull
#git tag -a tagName -m tagMessage
#git push origin tagName
#git checkout homeBranch
#git stash apply