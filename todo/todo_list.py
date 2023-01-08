

class Todo:    
    id = 0
    completed = False
    title = ""
    description = ""
    def __init__(self, id,title, description):
        self.id = id
        self.title = title
        self.description = description

class todo_list:
    todo_list = []

    def insert_todo(self):
        title = input("Introduce el titulo del todo")
        descripcion = input("Introduce la descripcion del todo")
        todo = Todo(len(self.todo_list),title, descripcion)
        self.todo_list.append(todo)

    def show_todos(self):
        for todo in self.todo_list:
            print(f"""
                    Id: {todo.id}
                    Title: {todo.title}
                    Descripcion: {todo.description}
                """)
    
    def show_todo(self):
        id = int(input("Introduce el id del todo que desee visualizar: "))
        for todo in self.todo_list:
            if todo.id == id:
                print(f"""
                    Title: {todo.title}
                    Descripcion: {todo.description}
                """)
                break

    def delete_todos(self):
        id = int(input("Introduce el id del todo que desee eliminar: "))
        for todo in self.todo_list:
            if todo.id == id:
                self.todo_list.remove(todo)
                break


    def list_length(self):
        return len(self.todo_list)


class Runtime:
    condition = False

    def __init__(self,list):
        self.list = list
        

    def change_condition(self):
        self.condition = True


def main():

    lista = todo_list()
    rnt = Runtime(list=lista)

    while rnt.condition == False :
        print("""
            1.Introducir una todo
            2.Ver todas los todos.
            3.Ver un todo.
            4.Borrar un todo
            5.Salir""")
        accion = input()

        if accion == "1":
            rnt.list.insert_todo()
        elif accion == "2": 
            rnt.list.show_todos()
        elif accion == "3":
            rnt.list.show_todo()
        elif accion == "4":
            rnt.list.delete_todo()   
        elif accion == "5":
            rnt.change_condition()
        



if __name__ == "__main__":
    main()
