def show_result(plaintext, n):

    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(n, plaintext)



    print 'Plaintext: %s' % plaintext
    print 'Encrytped: %s' % encrypted


show_result("abc", 1)

