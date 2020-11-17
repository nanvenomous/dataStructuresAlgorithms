def page_break():
    print('___________________________________________________________________________')

def _kot(args):
    if len(args) > 1:
        raise TypeError('too many input arguments')
    if len(args) == 0:
        raise TypeError('not enough input arguments')
    kotlinFile = args[0]
    mkdir -p build
    jarFile = os.path.join('./build/', os.path.basename(kotlinFile).split('.')[0] + '.jar')
    print(f'building {kotlinFile} to {jarFile}')
    kotlinc @(kotlinFile) -include-runtime -d @(jarFile)
    if _.rtn == 0:
        page_break()
        java -jar @(jarFile)
aliases['kot'] = _kot
