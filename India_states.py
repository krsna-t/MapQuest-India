import pandas
import turtle

screen=turtle.Screen()
image="map_resized.gif"
screen.title("India's state game")
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("state.csv")
state_ut=data.state.to_list()
guessed_s_ut=[]



t=turtle.Turtle()
t.hideturtle()
t.penup()


while len(guessed_s_ut) < 37:
    answer_state=screen.textinput(title=f"State & UT Guessed:len{guessed_s_ut}/37",prompt="Name Indian States & UT").title()
    if answer_state=="Exit":
        missing_s_ut=[]
        for state in state_ut:
            if state not in guessed_s_ut:
                missing_s_ut.append(state)
            print(missing_s_ut)    
        break

    if answer_state in state_ut:
        guessed_s_ut.append(answer_state)
        Coord_data=data[data.state == answer_state]
        x = float(Coord_data['x'].item())
        y = float(Coord_data['y'].item())
        t.goto(x,y)
        t.write(answer_state)




# def get_click_coordinates(x, y):
#     '''# ##### this part of code was written to get the coordinates of states after clicking on them in map first  #####
# '''
#     print(f"Clicked at coordinates: ({x}, {y})")

# screen.onscreenclick(get_click_coordinates)

turtle.mainloop()

