from statistics import mean
from matplotlib.pyplot import scatter,show,title,plot


def is_number(s):
    '''
    Judge whether the entered information is a number
    '''

    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass


def get_dict(dict):
    '''
    To get a dictionary by users,including some amount of dimensions
    '''

    i = 1

    while True:

        k = input(f'Enter x{i}:\nIf you have finished your entering,enter \'end\' to end\n')
        if k == 'end':
            break
        k1 = input(f'Enter y{i}:\nIf you have finished your entering,enter \'end\' to end\n')
        if k1 == 'end':
            break

        i += 1

        if is_number(k) and is_number(k1):
            dict[float(k)] = float(k1)
            print(dict,'\n')
            print('Tip:wrong number entered,continue first;you can correct it later')

        else:
            print('\aError!Enter a number.\n')
            i -= 1


def correct_enter(dict):
    '''
    If the user wrongly entered some numbers,it will correct them
    '''

    while True:
        h1 = input('Which one?(value)\n')

        if is_number(h1):
            del dict[float(h1)]
            break
        else:
            print('\aError!Enter a number.\n')

    while True:
        h2 = input('Enter the right value(xi,yi);\nxi=\n')
        h3 = input('Enter the right value(xi,yi);\nyi=\n')

        if is_number(h2) and is_number(h3):
            dict[float(h2)] = float(h3)
            break
        else:
            print('\aError!Enter a number.\n')


def least_squares(dict):
    '''
    Caculate the least squares,and return a dimension,including two numbers(a,b) in function 'y = bx + a'
    '''

    xi,yi = [],[]
    for k,v in dict.items():
        xi.append(k)
        yi.append(v)

    xi_2,yi_2 = [i**2 for i in xi],[i**2 for i in yi]
    xy = [i*j for i,j in zip(xi,yi)]

    r = (sum(xy) - mean(xi)*mean(yi)*len(xi))/((sum(xi_2) - mean(xi)**2*len(xi))**0.5*(sum(yi_2) - mean(yi)**2*len(xi))**0.5)

    if r == 0:
        print('Linearly independent.')
    else:
        b = (sum(xy) -  len(xi)*mean(xi)*mean(yi))/(sum(xi_2) - len(xi)*mean(xi)**2)
        a = mean(yi) - b*mean(xi)
        print(f'y = {b}x + {a}\n')

    return (b,a)


def draw_graph(a,k):
    '''
    Draw the scatter and the line in the same graph
    '''
    h,i = k[0],k[1]

    scatter(a[0],a[1])
    plot(a[2],a[3])
    title(f'y = {h}x + {i}')
    show()


def generate_list(dict,t):
    '''
    Generate necessary ists for the graph to draw,and return a dimension
    '''

    x,y,m = [],[],[]

    for k,v in dict.items():
        x.append(k)
        y.append(v)

    limit = int(max(x)) + 5
    for i in range(0,limit,2):
        p = t[0]*i + t[1]
        m.append(p)

    return (x,y,range(0,limit,2),m)

def save(dict,m):
    '''
    Save the results
    '''
    filename = 'Leastsquares.txt'
    with open(filename, 'a') as k:
        for p,v in dict.items():
            k.write(f'({p},{v}) ')
        b,a = m[0],m[1]
        k.write(f'y = {b}x + {a}\r\n')

def read_history():
    filename = 'Leastsquares.txt'
    try:
        with open(filename) as r:
            for line in r:
                print(line)
    except FileNotFoundError:
        print('No history.')