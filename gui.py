import functions
import PySimpleGUI as sg
import time

# Set the theme
sg.theme("Black")

# Define the layout of the window
layout = [
    [sg.Text('', key='clock')],
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("Add", size=10)],
    [sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])],
    [sg.Button("Edit"), sg.Button("Complete"), sg.Button("Exit")]
]

# Create the window
window = sg.Window('My To-Do App', layout, font=('Helvetica', 20))

# Event loop
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))

    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))

    elif event == "Exit" or event == sg.WIN_CLOSED:
        break

    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

# Close the window
window.close()
