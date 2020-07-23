import least_squares_functions as kv
from statistics import StatisticsError

while True:
    
    #Get statistics
    d = {}
    kv.get_dict(d)

    #Correct wrong input
    while True:
        h = input('Wrong number entered? Y/N\n')
        if h == 'Y':
            kv.correct_enter(d)
        elif h == 'N':
            break

    #Solve
    try:
        mn = kv.least_squares(d)
        break
    except StatisticsError:
        print('\aYou have entered nothing')
        pass

#Ask whether to save the results
ask = input('Save?Y/N\n')
while True:
    if ask == 'Y':
        kv.save(d,mn)
        break
    elif ask == 'N':
        break

#Draw graph
p = kv.generate_list(d,mn)
kv.draw_graph(p,mn)

#Ask for history
question = input('Do you want to see the history? Y/N\n')
while True:
    if question == 'Y':
        kv.read_history()
        break
    elif question == 'N':
        break