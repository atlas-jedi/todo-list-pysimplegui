import PySimpleGUI as sg

sg.theme('Default1')

value_list = []
tasks = []

layout = [
  [sg.Text('Tarefa: '), sg.InputText(key='task_input'), sg.Button('Adicionar')],
  [sg.Listbox(value_list, size=(40, 10), key='task_list')],
  [sg.Button('Marcar como Concluída'), sg.Button('Sair')]
]

window = sg.Window('ToDo List', layout)

while True:
  event, values = window.read()

  if event == sg.WIN_CLOSED or event == 'Sair':
    break
  elif event == 'Adicionar':
    task = values['task_input']
    tasks.append(task)
    window['task_list'].update(tasks)
    window['task_input'].update('')

window.close()