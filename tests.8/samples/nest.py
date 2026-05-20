def outer():
    msg = 'this is inner2'

    def inner():
        return 'inner-result'

    def inner2():
        return msg

    print(inner2())
    return inner()


if __name__ == '__main__':
    print('calling outer()...')
    print('outer() returned:', outer())
    print('test nest OK')
