from tkinter import *             # asi jen v Linuxu
import tkinter
import time
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
CANVAS_PADY = 10
CIRCLE_WIDTH = 100                # průměr kružníce
MOVE_STEP = 10                    # po kolika pixlech se bude krokovat (animace)
SLEEP_TIME = .05                  # 50 ms - čas mezi kroky (animace)
LINES = [550, 600, 650, 700, 750] # 5 linek
LINE_COUNT = 5                    # kvůli náhodnému číslu - nejde udělat dynamicky náhodný rozsah pomocí LINES.count
TITLE = "Moving ..."
SPACE = 100

root = Tk()                       # asi jen v Linuxu
root.title(TITLE)

canvas = Canvas(root, bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

for pos in LINES:
  canvas.create_line(SPACE, pos, CANVAS_WIDTH - SPACE, pos)

circleX0 = (CANVAS_WIDTH - CIRCLE_WIDTH) / 2
circleY0 = SPACE
circleX1 = circleX0 + CIRCLE_WIDTH
circleY1 = circleY0 + CIRCLE_WIDTH
circleObj = canvas.create_oval(circleX0, circleY0, circleX1, circleY1, fill='yellow')

def CirceMove():
  # startButton["state"] = DISABLED # nefunguje :-(

  x0, y0, x1, y1 = canvas.coords(circleObj)
  canvas.move(circleObj, 0, circleY0 + (y0 * -1))

  rndLine = random.randint(1, LINE_COUNT) # nejde LINES.count
  root.title(TITLE + " random line: #" + str(rndLine))

  for pos in range(circleY1, LINES[rndLine - 1], MOVE_STEP):
    time.sleep(SLEEP_TIME)
    canvas.move(circleObj, 0, MOVE_STEP)
    #root.update_idletasks()
    root.update()
  #else:
    # startButton["state"] = NORMAL # nefunguje :-(

startButton = Button(root, text='Run', command = CirceMove).pack(pady=CANVAS_PADY)

root.mainloop()         # asi jen v Linuxu
