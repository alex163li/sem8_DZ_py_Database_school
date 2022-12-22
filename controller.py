import view
import model

def category(f, param=0):
    li=[]
    for i in f:
        if param == '1':
            li.append(i.split()[0])
        elif param == '2':
            li.append(i.split()[1])
        elif param == '3':
            li.append(i.split()[2])
    return '\n'.join(li)


def sort(n, f, param=0):
    li=[]
    if param == '6' and len(n) == 1:
        for i in f:
            split_str = i.split()
            g = list(filter(lambda x: x in n.upper(), split_str[0]))
            if len(g):
                li.append(i)
    elif param == '6' and len(n) > 1:
        for i in f:
            e = i.split(" ")
            f = n[0:1].upper() + n[1:]
            if f in e[0]:
                li.append(i)
    else:
        for i in f:
            if n.lower() in i.lower():
                li.append(i)
    return '\n'.join(li)

def init(d, run = True):
    while run:
        if d == '1':
            print('\n' + category(model.read(), d), sep='\n')
            init(view.menu())    
        elif d == '2':
            print('\n' + category(model.read(), d), sep='\n')
            init(view.menu())        
        elif d == '3':
            print('\n' + category(model.read(), d), sep='\n')
            init(view.menu())   
        elif d == '4':
            print('\n' + sort(input('Введите № класса: '), model.read()), sep='')
            init(view.menu())   
        elif d == '5':
            print('\n' + ''.join(model.read()), sep='')
            init(view.menu())
        elif d == '6':
            print('\n' + sort(input('Введите фамилию ученика: '), model.read(), d), sep='')
            init(view.menu())    
        elif d == '7':
            print('\n')
            model.write(view.get_user_data())
            print('\nУченик добавлен!\n')
            init(view.menu())
        elif d == '8':
            print('\nДо свидания!\n')
            run = False
        break