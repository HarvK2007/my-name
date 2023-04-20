basic.show_string("Harvey ")
basic.show_string("King")
def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)