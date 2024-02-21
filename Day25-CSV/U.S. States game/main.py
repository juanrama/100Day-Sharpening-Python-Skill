import turtle as t
import pandas as pd

pen = t.Turtle()
scr = t.Screen()
scr.setup(725, 491)
scr.addshape('us_blank.gif')
scr.bgpic('us_blank.gif')
pen.penup()
pen.hideturtle()

data = pd.read_csv('50_states.csv')

state_coor = {}

for i in range(len(data)):
    state_coor[data['state'][i].lower()] = [data['x'][i], data['y'][i]]

true_answer = []
score = 0

while len(true_answer) < len(data):
    prov = scr.textinput(f'{score}/50 Jawaban Benar', 'Apa provinsi selanjutnya?').lower()
    if prov in state_coor:
        if prov in true_answer:
            pass
        else:
            pen.goto(state_coor[prov])
            pen.write(prov)
            true_answer.append(prov)
            score += 1

t.mainloop()



