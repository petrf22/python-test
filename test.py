import tkinter
import time
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
CANVAS_PADY = 10
CIRCLE_DIAMETER = 130             # průměr kružníce
CIRCLE_COLOR = 'yellow'           # barva kružníce
MOVE_STEP = 10                    # po kolika pixlech se bude krokovat (animace)
SLEEP_TIME = .025                 # 25 ms - čas mezi kroky (animace)
LINES = [550, 600, 650, 700, 750] # 5 linek
TITLE = "Moving ..."
SPACE = 100
# Inicializační souřadnice kružnice
CIRCLE_X0 = (CANVAS_WIDTH - CIRCLE_DIAMETER) / 2
CIRCLE_Y0 = SPACE
CIRCLE_X1 = CIRCLE_X0 + CIRCLE_DIAMETER
CIRCLE_Y1 = CIRCLE_Y0 + CIRCLE_DIAMETER

root = tkinter.Tk()
root.title(TITLE)

canvas = tkinter.Canvas(root, bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

for idx, pos in enumerate(LINES):
  canvas.create_line(SPACE, pos, CANVAS_WIDTH - SPACE, pos)
  canvas.create_text(SPACE - 10 , pos, text=str(idx + 1))

circleObj = canvas.create_oval(CIRCLE_X0, CIRCLE_Y0, CIRCLE_X1, CIRCLE_Y1, fill=CIRCLE_COLOR)

def CirceMove():
  # startButton["state"] = DISABLED # nefunguje :-(

  x0, y0, x1, y1 = canvas.coords(circleObj)
  canvas.move(circleObj, 0, CIRCLE_Y0 + (y0 * -1))
  root.update()

  rndLine = random.randint(1, len(LINES))
  root.title(TITLE + " random line: #" + str(rndLine))

  for pos in range(CIRCLE_Y1, LINES[rndLine - 1], MOVE_STEP):
    time.sleep(SLEEP_TIME)
    canvas.move(circleObj, 0, MOVE_STEP)
    #root.update_idletasks()
    root.update()
  #else:
    # startButton["state"] = NORMAL # nefunguje :-(

startButton = tkinter.Button(root, text='Run', command = CirceMove).pack(pady=CANVAS_PADY)

root.mainloop()
