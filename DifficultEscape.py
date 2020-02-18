import tkinter
import random


def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])
    if canvas.coords(obj)[2] <= 0:
        canvas.move(obj, step * N_X, 0)
    if canvas.coords(obj)[3] <= 0:
        canvas.move(obj, 0, step * N_Y)
    if canvas.coords(obj)[0] >= step * N_X:
        canvas.move(obj, - step * N_X, 0)
    if canvas.coords(obj)[1] >= step * N_Y:
        canvas.move(obj, 0, - step * N_Y)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    if event.keysym == 'Down':
        move_wrap(player, (0, step))
    if event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    if event.keysym == 'Right':
        move_wrap(player, (step, 0))
    for enemy in enemies:
        if enemy[0] in exiles:
            continue
        global enemy_global
        enemy_global = enemy
        direction = enemy[1]()  # вызвать функцию перемещения у "врага"
        move_wrap(enemy[0], direction) # произвести  перемещение
    check_move()


def check_move():
    global aim
    if canvas.coords(player) == canvas.coords(exit) and len(exiles) != N_X * N_Y // 25 * selected_difficulty:
        label.config(text="Сначала уничтожьте врагов!")
    if canvas.coords(player) == canvas.coords(exit) and len(exiles) == N_X * N_Y // 25 * selected_difficulty:
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Пол - это лава, а вы проиграли!")
            master.bind("<KeyPress>", do_nothing)
    for e in enemies:
        if canvas.coords(player) == canvas.coords(e[0]):
            label.config(text="Вас съел летающий монстр!")
            master.bind("<KeyPress>", do_nothing)
        
    if canvas.coords(player) == canvas.coords(grenade):
        grenade_pos = (random.randint(0, N_X - 1) * step,
                     random.randint(0, N_Y - 1) * step)
        fire_flag = False
        for j in fires:
                if (canvas.coords(j)[0], canvas.coords(j)[1]) == grenade_pos:
                    fire_flag = True
                    break
        enemy_flag = False
        for j in enemies:
                if not j[0] in exiles and (canvas.coords(j[0])[0], canvas.coords(j[0])[1]) == grenade_pos:
                    enemy_flag = True
                    break        
        while grenade_pos == (canvas.coords(player)[0], canvas.coords(player)[1]) or grenade_pos == (canvas.coords(exit)[0], canvas.coords(exit)[1]) or fire_flag:
            grenade_pos = (random.randint(0, N_X - 1) * step,
                         random.randint(0, N_Y - 1) * step)
            fire_flag = False
            for j in fires:
                if (canvas.coords(j)[0], canvas.coords(j)[1]) == grenade_pos:
                    fire_flag = True
                    break
            enemy_flag = False
            for j in enemies:
                    if not j[0] in exiles and (canvas.coords(j[0])[0], canvas.coords(j[0])[1]) == grenade_pos:
                        enemy_flag = True
                        break                 
        canvas.move(grenade, grenade_pos[0] - canvas.coords(grenade)[0], grenade_pos[1] - canvas.coords(grenade)[1])
        aim = canvas.create_rectangle(canvas.coords(player), fill='white')
        label.config(text="Вы подобрали гранату - прицельтесь!")
        master.bind("<KeyPress>", grenade_throwing)

        
def prepare_and_start():
    global grenade, player, exit, fires, enemies
    canvas.delete("all")
    exiles.clear()
    player_pos = (random.randint(0, N_X - 1) * step,
                  random.randint(0, N_Y - 1) * step)
    player = canvas.create_oval(player_pos, (player_pos[0] + step,
                                             player_pos[1] + step), fill='green')
    exit_pos = (random.randint(0, N_X - 1) * step,
                random.randint(0, N_Y - 1) * step)
    while exit_pos == player_pos:
        exit_pos = (random.randint(0, N_X - 1) * step, \
                    random.randint(0, N_Y - 1) * step)
    exit = canvas.create_rectangle(exit_pos, (exit_pos[0] + step, \
                                              exit_pos[1] + step), fill='yellow')
    N_FIRES = N_X * N_Y // 25 * selected_difficulty  # Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(0, N_X - 1) * step,
                    random.randint(0, N_Y - 1) * step)
        fire_flag = False
        for j in fires:
                if (canvas.coords(j)[0], canvas.coords(j)[1]) == fire_pos:
                    fire_flag = True
                    break
        while fire_pos == player_pos or fire_pos == exit_pos or fire_flag:
            fire_pos = (random.randint(0, N_X - 1) * step,
                        random.randint(0, N_Y - 1) * step)
            fire_flag = False
            for j in fires:
                    if (canvas.coords(j)[0], canvas.coords(j)[1]) == fire_pos:
                        fire_flag = True
                        break            
        fire = canvas.create_rectangle(fire_pos, (fire_pos[0] + step, \
                                                  fire_pos[1] + step), fill='red')
        fires.append(fire)
    N_ENEMIES = N_X * N_Y // 25 * selected_difficulty  # Число врагов
    enemies = []
    for i in range(N_ENEMIES):
        enemy_pos = (random.randint(0, N_X - 1) * step,
                     random.randint(0, N_Y - 1) * step)
        fire_flag = False
        for j in fires:
                if (canvas.coords(j)[0], canvas.coords(j)[1]) == enemy_pos:
                    fire_flag = True
                    break
        enemy_flag = False
        for j in enemies:
                if (canvas.coords(j[0])[0], canvas.coords(j[0])[1]) == enemy_pos:
                    enemy_flag = True
                    break        
        while enemy_pos == player_pos or enemy_pos == exit_pos or fire_flag or enemy_flag:
            enemy_pos = (random.randint(0, N_X - 1) * step,
                         random.randint(0, N_Y - 1) * step)
            fire_flag = False
            for j in fires:
                if (canvas.coords(j)[0], canvas.coords(j)[1]) == enemy_pos:
                    fire_flag = True
                    break
            enemy_flag = False
            for j in enemies:
                    if (canvas.coords(j[0])[0], canvas.coords(j[0])[1]) == enemy_pos:
                        enemy_flag = True
                        break                 
        enemy = canvas.create_oval(enemy_pos, (enemy_pos[0] + step, \
                                               enemy_pos[1] + step), fill='HotPink4')
        enemies.append((enemy, chase_move))
    grenade_pos = (random.randint(0, N_X - 1) * step, random.randint(0, N_Y - 1) * step)
    fire_flag = False
    for j in fires:
        if (canvas.coords(j)[0], canvas.coords(j)[1]) == grenade_pos:
            fire_flag = True
            break
    enemy_flag = False
    for j in enemies:
        if (canvas.coords(j[0])[0], canvas.coords(j[0])[1]) == grenade_pos:
            enemy_flag = True
            break
    while grenade_pos == player_pos or grenade_pos == exit_pos or fire_flag or enemy_flag:
        grenade_pos = (random.randint(0, N_X - 1) * step, random.randint(0, N_Y - 1) * step)
        fire_flag = False
        for j in fires:
            if (canvas.coords(j)[0], canvas.coords(j)[1]) == grenade_pos:
                fire_flag = True
                break
        enemy_flag = False
        for j in enemies:
            if (canvas.coords(j[0])[0], canvas.coords(j[0])[1]) == grenade_pos:
                enemy_flag = True
                break
    grenade = canvas.create_rectangle(grenade_pos, (grenade_pos[0] + step, \
                                                    grenade_pos[1] + step), fill='dark slate grey')    
    label.config(text="Спасайтесь от монстров!")
    master.bind("<KeyPress>", key_pressed)


def do_nothing(x):
    pass


def grenade_throwing(event):
    if event.keysym != 'Return':
        if event.keysym == 'Up':
            move_wrap(aim, (0, -step))
        if event.keysym == 'Down':
            move_wrap(aim, (0, step))
        if event.keysym == 'Left':
            move_wrap(aim, (-step, 0))
        if event.keysym == 'Right':
            move_wrap(aim, (step, 0))
    else:
        for e in enemies:
            if canvas.coords(aim) == canvas.coords(e[0]):
                label.config(text="Цель ранена!")
                canvas.delete(aim)
                exiles.add(e[0])
                canvas.delete(e[0])
        master.bind("<KeyPress>", key_pressed)


def chase_move():
    if canvas.coords(player)[0] - canvas.coords(enemy_global[0])[0] != 0 and \
       canvas.coords(player)[1] - canvas.coords(enemy_global[0])[1] != 0:
        return random.choice([(difference_sign(canvas.coords(player)[0], canvas.coords(enemy_global[0])[0]) * step, 0),
                              (0, difference_sign(canvas.coords(player)[1], canvas.coords(enemy_global[0])[1]) * step)])
    else:
        return (difference_sign(canvas.coords(player)[0], canvas.coords(enemy_global[0])[0]) * step,
                difference_sign(canvas.coords(player)[1], canvas.coords(enemy_global[0])[1]) * step)


def difference_sign(a, b):
    if a != b:
        return int((a - b) / abs(a - b))
    else:
        return 0


def difficulty_choice():
    global selected_difficulty
    if len(lbox_difficulty.curselection()) > 0:
        selected_difficulty = lbox_difficulty.get(lbox_difficulty.curselection())
    else:
        selected_difficulty = 2    


step = 60
N_X = 10
N_Y = 10
exiles = set()
master = tkinter.Tk()
lbox_difficulty = tkinter.Listbox(bg='peach puff')
lbox_difficulty.insert(tkinter.END, 1)
lbox_difficulty.insert(tkinter.END, 2)
lbox_difficulty.insert(tkinter.END, 3)
lbox_difficulty.pack(side='left')
selected_difficulty = 2

choice = tkinter.Button(master, text="Выбрать сложность", command=difficulty_choice)
choice.pack(side='left')

label=tkinter.Label(master, text="Найди выход")
label.pack()
canvas=tkinter.Canvas(master, bg='blue',
                        height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()
