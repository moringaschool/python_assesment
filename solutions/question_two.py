def sentence():
    print "Please enter a sentence"

    sentence = raw_input("Write it here")

    sentList=[]
    for index in sentence:
        if (index == index.upper()):
            sentList.append(index.upper())
        elif (index == index.lower()):
            sentList.append(index.upper())

    print ''.join(sentList)


sentence()
