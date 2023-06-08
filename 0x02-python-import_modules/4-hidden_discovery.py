#!/usr/bin/python3
if __name__ == "__main__":
    import py_compile
    import marshal

    py_compile.compile('hidden_4.py')
    code = open('hidden_4.pyc', 'rb').read()
    names = []
    for const in marshal.load(code)['co_consts']:
        if isinstance(const, str) and not const.startswith('__'):
            names.append(const)
    for name in sorted(names):
        print(name)
