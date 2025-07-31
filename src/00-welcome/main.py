import turtle


def init_screen_turtle(width, height, bg_color, pen_color):
    """
    Initialize a screen & a turtle object for drawing

    :param width: screen width
    :param height: screen height
    :param bg_color: screen background color
    :param pen_color: turtle pen color
    :return: screen and turtle objects
    """
    sc = turtle.Screen()
    sc.setup(width, height)
    sc.bgcolor(bg_color)

    tur = turtle.Turtle()
    tur.pencolor(pen_color)

    return sc, tur


def draw_benzene(tur):
    """
    Draw a benzene shape on the screen

    :param tur: turtle object to use for drawing
    :return: nothing
    """
    colors = ["violet", "indigo", "blue", "green", "yellow", "orange"]

    curr_pencolor = tur.pencolor()

    tur.pendown()
    for x in range(200):
        tur.pencolor(colors[x % 6])
        tur.width(x // 100 + 1)
        tur.forward(x)
        tur.left(59)
    tur.penup()

    tur.pencolor(curr_pencolor)


def write_msg(tur, x, y, msg, font_size, font_color):
    """
    Write a message on the screen
    :param tur: the turtle object to use for writing
    :param x: x position for the message
    :param y: y position for the message
    :param msg: the message to write
    :param font_size: font size of the message
    :param font_color: font color of the message
    :return: nothing
    """
    tur.penup()
    tur.goto(x, y)

    curr_speed = tur.speed()
    tur.speed(1)

    curr_pencolor = tur.pencolor()
    tur.pencolor(font_color)

    tur.write(msg,
              True,
              "center",
              ('Arial', font_size, 'bold'))

    tur.speed(curr_speed)
    tur.pencolor(curr_pencolor)


def write_header(sc, tur):
    """
    Write a header on the screen
    :param sc: screen object to write on
    :param tur: turtle object to use for writing
    :return: nothing
    """
    font_size = 20
    msg = "Welcome to COMP123"
    write_msg(tur,
              0,
              sc.window_height()/2 - 2*font_size,
              msg,
              font_size,
              "white")


def write_footer(sc, tur):
    """
    Write a footer on the screen
    :param sc: screen object to write on
    :param tur: turtle object to use for writing
    :return: nothing
    """
    font_size = 10
    msg = "click anywhere to quit"
    write_msg(tur,
              0,
              -1 * (sc.window_height() / 2 - 2 * font_size),
              msg,
              font_size,
              "orange")


if __name__ == "__main__":
    scn, turt = init_screen_turtle(500, 500, "black", "white")

    write_header(scn, turt)

    turt.home()
    turt.speed(0)
    draw_benzene(turt)

    write_footer(scn, turt)

    turt.home()

    scn.exitonclick()
