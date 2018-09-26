def merge_the_tools(string, k):
     
    a = [string[i:i+k] for i in range(0,len(string),k)]
    for i in a:
        uni = []
        for j in i:
            if j not in uni:
                uni.append(j)
        print (''.join(uni))

    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
