input.onButtonPressed(Button.A, function () {
    basic.showNumber(0)
    message = "" + message + "0"
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    basic.showString(message)
    radio.sendString(message)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(1)
    message = "" + message + "1"
})
let message = ""
message = ""
radio.setGroup(245)
basic.forever(function () {
	
})
