def on_button_pressed_a():
    global message
    message = "" + message + "0"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string(message)
    radio.send_string(message)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global message
    message = "" + message + "1"
input.on_button_pressed(Button.B, on_button_pressed_b)

message = ""
message = ""
radio.set_group(245)

def on_forever():
    pass
basic.forever(on_forever)
