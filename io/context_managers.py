#with opens a new context. After running that code block connection destroys. So no need to close the file
with open("sample.txt", 'a') as file:
    x = [str(i) for i in range(0, 100)]
    msg = ', '.join(x)
    file = open('sample.txt', 'a')
    file.write(msg)

    file = open('sample.txt')
    line = file.readline()
    print(line)


