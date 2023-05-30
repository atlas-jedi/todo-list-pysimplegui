import PySimpleGUI as sg

sg.theme('Default1')

initial_list = ['Adicione uma nova task para aparecer aqui']
tasks = []

layout = [
  [sg.Text('Tarefa: '), sg.InputText(key='task_input'), sg.Button('Adicionar')],
  [sg.Listbox(initial_list, size=(40, 10), enable_events=True, key='task_list')],
  [sg.Button('Remover task selecionada', disabled=True, key='remove_task'), sg.Button('Sair')]
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
  elif event == 'task_list':
    if len(tasks) == 0:
      window['remove_task'].update(disabled=True)
    else:
      window['remove_task'].update(disabled=False)
  elif event == 'remove_task':
    selected_task = values['task_list'][0]
    if not tasks:
      continue
    else:
      tasks.remove(selected_task)
      window['task_list'].update(tasks)
    window['remove_task'].update(disabled=True)

window.close()