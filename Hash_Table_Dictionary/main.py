import PySimpleGUI as sg
import hash_table_dictionary
import random, string
import os
def open_window():
    layout = [
    [sg.Text("Size of dictionary: "),sg.Text(str(htd.size()),font =('Calibri', 20, 'bold'))],
    [sg.Text("Size of Hash Table: "),sg.Text(str(htd.get_num_buckets()),font =('Calibri', 20, 'bold'))],
    [sg.Text("The longest element in the Hash Table: "),sg.Text(str(max(keys, key=lambda x: len(x.split()))),font =('Calibri', 20, 'bold')), sg.Text(' (size = '),sg.Text(str(max(len(x.split()) for x in keys)),font =('Calibri', 10,'bold')),sg.Text(')')]
    ]

    window = sg.Window("Information Hash Table", layout, modal=True, margins=(2,2))
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()

column1 = [[sg.Text('Enter the word to delete:'), sg.InputText(size=(10,1), key='input_delete')], 
    [sg.Button('Delete')],
    [sg.Text('Enter the new word to add:'),sg.InputText(size=(10,1), key='input_add_key')],
    [sg.Text('Meaning:'),sg.InputText(size=(10,1), key='input_add_value')],
    [sg.Button('Add')],
    [sg.Text('Choose the word to edit means:'),sg.InputText(size=(10,1), key='input_edit_key')],
    [sg.Text('Enter the meaning:'),sg.InputText(size=(10,1), key='input_edit_value')],
    [sg.Button('Edit')]]
layout = [
    [sg.Text("Uploads Dictionary")],
    [sg.Input(), sg.FileBrowse('FileBrowse')],
    [sg.Submit(),sg.Text('                                                               ', key='submit_successful',font =('Calibri', 20, 'bold'))],
    [sg.InputText(size=(10,1), key='input_search'),sg.Button('Search'), sg.Text('                                   ', key='search_result',font =('Calibri', 20, 'bold'))],
    [sg.Button('Show')],
    [sg.Listbox(values =[''], size = (25, 20),font = ('Calibri', 12), background_color ='White',key = '_display_'), sg.Column(column1)],
    [sg.Button('Information Hash Table'), sg.Button('Exit', button_color=('white', 'firebrick3'))]
]

window = sg.Window('Dictionary Using Hash Table', layout, margins=(2,2))
htd = hash_table_dictionary.HashTableMap()
while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    
    if event == 'Submit':
        f = open(values['FileBrowse'], "r", encoding='utf-8')
        Lines = f.readlines()
        arr_keys = []
        arr_values = []
        for line in Lines:
            str_keys = ''
        
            for i in range(len(line)):
                if (line[i] == '|'):
                    str_keys = str(str_keys)
                    arr_keys.append(str_keys)
                    #
                    str_values = ''
                    for j in range(i+1, len(line)):
                        if(line[j] == '\n'): break
                        str_values += line[j]
                    arr_values.append(str_values)
                str_keys += line[i]

        print(arr_keys)
        print(arr_values)
        for i in range(len(arr_keys)):
            htd.add(arr_keys[i].strip(), arr_values[i].strip())

        for k, v in htd.get_all():
            print (k,'|' ,v)

        window['submit_successful'].update('Uploads Successfull')
    elif event == 'Search':
        print('Search: ', values['input_search'])
        search_str = values['input_search']
        print('Result: ',htd.get(search_str.strip()))
        if htd.get(search_str.strip()) == None:
            window['search_result'].update('Not in dictionary')
        window['search_result'].update(htd.get(search_str.strip()))
    elif event == 'Add':
        key = values['input_add_key']
        value = values['input_add_value']
        print('Add key: ', key)
        print('Add value: ', value)
        htd.add(key, value)
        window['_display_'].update([])
        values = [k + " | " + v for k, v in htd.get_all()]
        window.FindElement('_display_').update(values)
    elif event == 'Edit':
        key = values['input_edit_key']
        value = values['input_edit_value']
        print('Edit key: ', key)
        print('Edit value: ', value)
        htd.insert(key, value)
        window['_display_'].update([])
        values = [k + " | " + v for k, v in htd.get_all()]
        window.FindElement('_display_').update(values)
    elif event == 'Delete':
        print('Delete: ', values['input_delete'])
        delete_str = values['input_delete']
        htd.delete(delete_str)
        # update hdt
        window['_display_'].update([])
        values = [k + " | " + v for k, v in htd.get_all()]
        window.FindElement('_display_').update(values)

    elif event == 'Show':
        values = [k + " | " + v for k, v in htd.get_all()]
        window.FindElement('_display_').update(values)

    elif event == 'Information Hash Table':
        # window['size_dictionary'].update(str(htd.size()))
        # window['size_hashtable'].update(str(htd.get_num_buckets()))
        print(str(htd.size()))
        print(str(htd.get_num_buckets()))
        keys = [k for k, v in htd.get_all()]
        print('The longest element in the Hash Table: ',max(keys, key=lambda x: len(x.split())),' (size = ', max(len(x.split()) for x in keys),')')

        open_window()
        
window.close()