import sys
import os
def buck_rename(args):
    files=os.listdir(args)
    print('input:'+args)
    for file in files:
        a = 'm-' + file
        print(file+'-->'+a)
        os.rename(args+file,args+a)

if __name__ == '__main__':
    buck_rename(sys.argv[1])
