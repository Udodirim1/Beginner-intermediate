import PySimpleGUI as sg

layout = [
    [sg.Text('text', enable_events = True, key = "-Text-"),sg.Spin(['item 1, item 2'])],
    [sg.Button('Button', key='-BUTTON1-')],
    [sg.Input(key='-INPUT-')],
    [sg.Text('Test'), sg.Button('Button', key='-BUTTON2-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'BUTTON1':
        window['-TEXT-'].update(visible=False)

    if event == 'BUTTON2':
        print('something else')

    if event == '-TEXT-':
        print('text was pressed')

window.close()





# A print statement
# layout = [
#     [sg.Text("Hello from the otherside")],
#     [sg.Button("OK")]
# ]
#
# # create the window
# window = sg.Window("Demo", layout)
#
# # create an event loop
# while True:
#     event, values = window.read()
#
#     # end program if user closes window or presses the ok button
#
#     if event == "OK" or event == sg.WINDOW_CLOSED:
#         break
#
# window.close()
