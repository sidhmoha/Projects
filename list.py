if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        cmd=str(input())
        cmd =cmd.split()
        if ('insert' in cmd[0]):
            arr.insert(int(cmd[1]),int(cmd[2]))
        elif ('print' in cmd[0]):
            print (arr)
        elif ('remove' in cmd[0]):
            arr.remove(int(cmd[1]))
        elif ('append' in cmd[0]):
            arr.append(int(cmd[1]))
        elif ('sort' in cmd[0]):
            arr.sort()
        elif ('pop' in cmd[0]):
            arr.pop()
        elif ('reverse' in cmd[0]):
            arr.reverse()
        else:
            print (arr)