import tkinter
import tkinter.messagebox
import pickle

#main
root = tkinter.Tk()
root.title("To-Do List App")
root.config(bg="pink")

#Create a header label
header_label = tkinter.Label(root, text="To-Do List App", bg="pink", fg="black", font=("Arial 0 bold", 20))
header_label.pack(pady=20)

#Create a toolbar to hold buttons
toolbar = tkinter.Frame(root, bg="pink")
toolbar.pack(fill=tkinter.X, side=tkinter.TOP)

#Create a listbox to display tasks
todolist_container = tkinter.Listbox(root, width=50, bg="white", fg="black", font=("Arial 0 bold", 10))
todolist_container.pack(pady=20)

#Create a label for the task entry field
entry_label = tkinter.Label(root, text="Enter The Task:",bg="white",fg="black", font=("Arial 0 bold", 15))
entry_label.pack(pady=10)

#Create an entry field for users to type new tasks
todo_entry = tkinter.Entry(root, width=30, bg="white", fg="black", font=("Arial 0 bold", 16))
todo_entry.pack(pady=10)

#function for adding tasks
def addTask():
    task = todo_entry.get()
    if task != "":
        todolist_container.insert(tkinter.END, task)
        todo_entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

#Create a button to add tasks
add_button = tkinter.Button(toolbar, text="Add Task", command=addTask, bg="white", fg="black", font=("Arial", 12), relief="flat")
add_button.pack(side=tkinter.LEFT, padx=10)

#Define a function to delete tasks from the listbox
def deleteTask():
    try:
        task_index = todolist_container.curselection()[0]
        todolist_container.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

#Create a button to delete tasks    
delete_button = tkinter.Button(toolbar, text="Delete Task", command=deleteTask, bg="white", fg="black", font=("Arial", 12), relief="flat")
delete_button.pack(side=tkinter.LEFT, padx=10)

#Define a function to save tasks to a file
def saveTasks():
    tasks = todolist_container.get(0, todolist_container.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
    tkinter.messagebox.showinfo(title="Saved!", message="Tasks entered are now saved.")

#Create a button to save tasks
save_button = tkinter.Button(toolbar, text="Save Tasks", command=saveTasks, bg="white", fg="black", font=("Arial", 12), relief="flat")
save_button.pack(side=tkinter.LEFT, padx=10)

#Define a function to load tasks from a file
def loadTasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        todolist_container.delete(0, tkinter.END)
        for task in tasks:
            todolist_container.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="No tasks saved.") 

#Create a button to load tasks
load_button = tkinter.Button(toolbar, text="Load Tasks", command=loadTasks, bg="white", fg="black", font=("Arial", 12), relief="flat")
load_button.pack(side=tkinter.LEFT, padx=10)

#Start the main loop
root.mainloop()

