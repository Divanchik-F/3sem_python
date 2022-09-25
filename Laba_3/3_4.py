import csv

groups = ("101", "102")

def add_student(st):
    try:
        ent = check_ent(input("Введите ФИО, курс и группу").strip())
        st.append(ent)
    except Exception as q:
        print(q.args[0])


def list_gr(st, args):
    try:
        gr = args[1]

        for ent in st:
            if ent[-1].lower() == gr:
                print(" ".join(ent))
    except IndexError:
        print("Укажите группу")


def find_student(st, args):
    try:
        surname, name = args[2], args[3]

        for ent in st:
            if surname == ent[0].lower() and name == ent[1].lower():
                print(" ".join(ent))
    except IndexError:
        print("Укажите ФИО студента")


def remove_student(st):
    name = tuple(input("Введите ФИО студента: ").strip().split())
    try:
        st.pop(st.index(next(q for q in st if q[:3] == name)))
    except StopIteration:
        print("Студент не найден")


def check_ent(ent):
    ent = ent.split()

    try:
        year, gr = ent[3], ent[4]
        if gr.lower() not in groups:
            raise ValueError("Неверная группа")
        if not ( float(year).is_integer() and 1 <= int(year) <= 6 ):
            raise ValueError("Неверный номер курса")
    except IndexError:
        raise ValueError("Неверный формат записи")

    return tuple(ent)


def saving(fifi, st):
    fifi.seek(0)
    fifi.truncate()
    writer = csv.writer(fifi)
    writer.writerows(st)
    fifi.close()
    return open(fifi.name, "r+", encoding="utf8")



def end(fifi, st):
    print("\nСохранение изменений")
    fifi = saving(fifi, st)
    fifi.close()
    print("Выход")
    exit()


def read_data(fifi):
    st = []
    success = True
    
    for i, row in enumerate(csv.reader(fifi)):
        try:
            st.append(check_ent(" ".join(row)))
        except Exception as q:
            print(f"При чтении файла на строке {i+1} возникла ошибка")
            print(q.args[0])
            success = False
            break

    return st if success else None


def first_loop(fifi, st):
    while True:
        try:
            cmd = input("Введите команду").strip().lower()
            if cmd == "Сохранить изменения":
                fifi = saving(fifi, st)
            elif cmd == "Добавить студента":
                add_student(st)
            elif cmd == "Удалить студента":
                remove_student(st)
            elif cmd.startswith("Группа"):
                list_gr(st, cmd.split())
            elif cmd.startswith("Найти студента"):
                find_student(st, cmd.split())
            elif cmd in ("Выход"):
                end(fifi, st)
            else:
                print("Неизвестная команда")
        except KeyboardInterrupt:
            end(fifi, st)


def start_first_loop(fifi):
    st = read_data(fifi)
    if st is not None:
        first_loop(fifi, st)
    exit() 


def open_file():
    path = input("Укажите путь к файлу базы данных")
    success = False
    fifi = None
    try:
        fifi = open(path, "r+", encoding="utf8")
        success = True
    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Доступ к файлу базы данных запрещён")
    except:
        print("Неизвестная ошибка при открытии файла базы данных")
    else:
        start_first_loop(fifi)
    finally:
        if not success:
            open_dialogue(path)


def create_file(path):
    try:
        fifi = open(path, "x", encoding="utf8")
    except FileExistsError:
        print("Такой файл уже существует")
    except PermissionError:
        print("Недостаточно прав для создания такого файла")
    except:
        print("Неизвестная ошибка при создании файла")
    else:
        print(f"Файл {path} создан.")
        fifi = open(fifi.name, "r+", encoding="utf8")
        start_first_loop(fifi)


def open_dialogue(path):
    print("""Выберите:
    1) Ввести другой путь
    2) Создать по указанному пути пустой файл базы данных""")
    try:
        ans = int(input())

        if ans == 1:
            open_file()
        elif ans == 2:
            create_file(path)
        else:
            raise ValueError
    except ValueError:
        print("Введите число")


open_file()
