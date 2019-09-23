import PySimpleGUI as sg
import backend
import data_params
import json

# sg.ChangeLookAndFeel("Dark")

menu_def = [['Help', ['&Instructions', '&About', 'E&xit']]]

layout = [
    [sg.Menu(menu_def)],
    [sg.Text("Select number of test persons"),
     sg.Spin([i for i in range(1, 101)], initial_value=1, key="SPIN1", size=(3, 1))],
    [sg.Text("Do you want to save results in a file?"), sg.Radio('Yes', "RADIO1", key="Y", default=False),
     sg.Radio('No', "RADIO1", key="N", default=True)],
    [sg.Button("Run", bind_return_key=True), sg.Button("Exit"), sg.Button("Reset"), sg.T("" * 10),
     sg.Button("Show results")]
]

window = sg.Window(
    'Test person generator',
    layout,
    return_keyboard_events=True
)

win2_active = False
while True:
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == "Run":
        backend.generate_data(values["SPIN1"])
        data_params.personer_formatted = json.dumps(data_params.final, indent=4, ensure_ascii=False)
        sg.PopupScrolled(data_params.personer_formatted, title="Call success")
        if values["Y"]:
            try:
                folder_path = sg.PopupGetFolder(
                    "Select folder path",
                    title='Select folder',
                    default_path=data_params.path)
                data_params.path = folder_path
                backend.save_output(folder_path)
            except FileNotFoundError as file_not_found:
                sg.Popup("File not found or no file selected")
                print(file_not_found)
    if event == "Reset":
        backend.reset()
        window["N"](True)
    if event == "Show results":
        sg.PopupScrolled(data_params.personer_formatted, title="Results")
    if event == "Instructions":
        sg.popup(data_params.howto_msg, non_blocking=True)
    if event == "About":
        sg.popup(data_params.about_msg, non_blocking=True)

window.Close()

