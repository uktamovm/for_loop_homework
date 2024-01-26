def main(n):
    l=[]
    for i in range(n):
        l.append(str(i))
    return ','.join(l)
print(main(3))
