from collections import deque
import sys

def initial_state():
    return (8, 0, 0)

def is_goal(s):
      if(s[0]!=4 or s[1]!=4):
      return True
  return False

def print_pour(oldconfig, newconfig):
    N = str(oldconfig[0]) + str(oldconfig[1]) + str(oldconfig[2])
    M = str(newconfig[0]) + str(newconfig[1]) + str(newconfig[2])
    # print(N,M)

def print_jugs(jugs):
    M = str(jugs[0]) + str(jugs[1]) + str(jugs[2])
    x = '(' + str(jugs[0]) +', '+ str(jugs[1]) +', '+ str(jugs[2]) + ')'
    print(x)

queue = deque()

already = dict()

start = (8,0,0)
total = start[0] + start[1] + start[2]

def successors(s):
   queue.append(start)
    while True:
        try: item = queue.popleft()
        except IndexError:
            break
        N = item[0]*100 + item[1]*10 + item[2]
        if N in already:
            continue
        print_jugs(item)
        already[N] = True
        jar8 = item[0]
        jar5 = item[1]
        jar3 = item[2]
        current_total = jar8 + jar5 + jar3


        if current_total != total:
            print("Problem: jars sum to "+str(current_total)+" should sum to", total)
            sys.exit(1)
        if jar8 > 0:
            if jar5 < 5:
                v5 = 5 - jar5
                if v5 >= jar8:
                    newconfig = (0,jar5+jar8,jar3)
                else:
                    newconfig = (jar8-v5,5,jar3)
                queue.append(newconfig);
                print_pour(item, newconfig)
            if jar3 < 3:
                v3 = 3 - jar3
                if v3 >= jar8:
                    newconfig = (0,jar5,jar3+jar8)
                else:
                    newconfig = (jar8-v3,jar5,3)
                queue.append(newconfig);
                print_pour(item, newconfig)

        if jar5 > 0:
            if jar8 < 8:
                v8 = 8 - jar8
                if v8 >= jar5:
                    newconfig = (jar8+jar5,0,jar3)
                else:
                    newconfig = (8,jar5-v8,jar3)
                queue.append(newconfig);
                print_pour(item, newconfig)
            if jar3 < 3:
                v3 = 3 - jar3
                if v3 >= jar5:
                    newconfig = (jar8,0,jar3+jar5)
                else:
                    newconfig = (jar8,jar5-v3,3)
                queue.append(newconfig);
                print_pour(item, newconfig)

        if jar3 > 0:
            if jar8 < 8:
                v8 = 8 - jar8
                if v8 >= jar3:
                    newconfig = (jar8+jar3,jar5,0)
                else:
                    newconfig = (8,jar5,jar3-v8)
                queue.append(newconfig);
                print_pour(item, newconfig)
            if jar5 < 5:
                v5 = 5 - jar5
                if v5 >= jar3:
                    newconfig = (jar8,jar5+jar3,0)
                else:
                    newconfig = (jar8,5,jar3-v5)
                queue.append(newconfig);
                print_pour(item, newconfig)
