import tkinter as tk
from tkinter import ttk
import datetime
import pickle
from tkinter import font

root = tk.Tk()
root.geometry("600x1000+0+0")

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Yu Gothic", size=10)
root.option_add("*Font", default_font)
root.configure(bg='#D2F3D4')
root.title("授業報告作成")


# テキストボックスの各項目のタイトルを格納
topics = ["受講目的",
          "志望校/受験科目",
          "今月の目標",
          "授業の内容",
          "進路相談",
          "生活や心身についての相談",
          "勉強全体の進捗状況",
          "遅刻・欠席の有無",
          "他の講師への申し送り事項",
          "休退塾懸念事項と対応状況"]

textboxes = []

def load_template_dict():  # 保存されたテンプレを読み込む関数
    try:
        with open('templateDict.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {
    "テンプレート1": {
        'texts': [
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容",
            "ここにテンプレート1の内容"
        ],
        'date': ["1", "1", "月"],
        'time': ["1", "1", "1", "1"],
        "name": ["生徒", "教師"]
    }
}
def add_date_and_time():
    month = date_month_textbox.get()
    date = date_date_textbox.get()
    day = date_day_textbox.get()
    starthour = time_starthour_textbox.get()
    startminute = time_startminute_textbox.get()
    finishhour = time_finishhour_textbox.get()
    finishminute = time_finishminute_textbox.get()
    text = "日時：" + month + "月　" + date + "日　" + day + "曜日" + starthour + "時" + startminute + "分～" + finishhour + "時" + finishminute + "分\n"
    return text
    #texts +=

def add_name():
    student_name = name_student_textbox.get()
    teacher_name = name_teacher_textbox.get()

    text = "生徒：" + student_name + "教師：" + teacher_name + "\n"
    return text

def combine_text(texts, topics):  # テキストボックスに入力された内容を結合して１つのテキストにする
    text = ""
    for i in range(len(topics)):
        text += "【" + topics[i] + "】\n" + texts[i] + "\n"
    return text

def load_template():
    selected_template = template_name.get()  # 選択されたテンプレート名を取得
    template = template_dict[selected_template]  # テンプレート名に対応するテンプレートを取得
    for i in range(len(textboxes)):
        textboxes[i].delete('1.0', tk.END)  # 既存のテキストを削除
        textboxes[i].insert(tk.END, template['texts'][i])  # テンプレートを挿入

    # Load date and time entries
    date_month_textbox.delete(0, tk.END)
    date_month_textbox.insert(tk.END, template['date'][0])
    date_date_textbox.delete(0, tk.END)
    date_date_textbox.insert(tk.END, template['date'][1])
    date_day_textbox.delete(0, tk.END)
    date_day_textbox.insert(tk.END, template['date'][2])

    time_starthour_textbox.delete(0, tk.END)
    time_starthour_textbox.insert(tk.END, template['time'][0])
    time_startminute_textbox.delete(0, tk.END)
    time_startminute_textbox.insert(tk.END, template['time'][1])
    time_finishhour_textbox.delete(0, tk.END)
    time_finishhour_textbox.insert(tk.END, template['time'][2])
    time_finishminute_textbox.delete(0, tk.END)
    time_finishminute_textbox.insert(tk.END, template['time'][3])

    name_student_textbox.delete(0, tk.END)
    name_student_textbox.insert(tk.END, template["name"][0])
    name_teacher_textbox.delete(0, tk.END)
    name_teacher_textbox.insert(tk.END, template["name"][1])




def save_template():
    new_template_name = new_template_entry.get()  # 新しいテンプレート名を取得
    new_template = {
        'texts': [textbox.get("1.0", tk.END) for textbox in textboxes],  # 新しいテンプレートを取得
        'date': [
            date_month_textbox.get(),
            date_date_textbox.get(),
            date_day_textbox.get(),
        ],
        'time': [
            time_starthour_textbox.get(),
            time_startminute_textbox.get(),
            time_finishhour_textbox.get(),
            time_finishminute_textbox.get(),
        ],
        'name': [
            name_student_textbox.get(),
            name_teacher_textbox.get(),

        ]
    }
    template_dict[new_template_name] = new_template  # 辞書に新しいテンプレートを追加
    template_name['values'] = list(template_dict.keys())  # Comboboxの選択肢を更新
    with open("templateDict.pkl", "wb") as f:
        pickle.dump(template_dict, f)

def save_text():
    whole_text = ""
    filename = "test"
    whole_text += add_date_and_time()
    whole_text += add_name()
    texts = [textbox.get("1.0", tk.END) for textbox in textboxes]
    main_text = combine_text(texts, topics)
    whole_text += main_text
    print(whole_text)
    with open(f"{filename}.txt", "w") as file:
        file.write(whole_text)
template_dict = load_template_dict()


top_frame = tk.Frame(root, bg='#D2F3D4')
top_frame.pack(side=tk.TOP, fill=tk.X)
canvas = tk.Canvas(root, bg='#D2F3D4')
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas, takefocus=False, bg='#D2F3D4')

scrollbar.pack(side=tk.LEFT, fill="y")
canvas.pack(side=tk.LEFT, fill="both", expand=True)

canvas.create_window((0,0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

template_name = ttk.Combobox(top_frame, values=list(template_dict.keys()))
template_name.grid(row=0, column=0)

load_button = tk.Button(top_frame, text="テンプレートを読み込む", command=load_template)
load_button.grid(row=1, column=0)

new_template_entry = tk.Entry(top_frame)
new_template_entry.grid(row=0, column=1)


add_button = tk.Button(top_frame, text="現在のテキストをテンプレートに追加", command=save_template)
add_button.grid(row=1, column=1)

save_button = tk.Button(top_frame, text="保存",  command=save_text)
save_button.grid(row =1, column = 2, padx = (100, 0), sticky = tk.E)

date_frame = tk.Frame(frame, bg='#D2F3D4')
date_frame.pack()

date_label = tk.Label(date_frame, text="日付:",  anchor=tk.W, justify=tk.LEFT, bg='#D2F3A1')
date_label.pack(side=tk.LEFT)
date_month_textbox = tk.Entry(date_frame, width = 4)
date_month_textbox.pack(side = tk.LEFT)
date_month_label = tk.Label(date_frame, text = "月" )
date_month_label.pack(side = tk.LEFT)
date_date_textbox = tk.Entry(date_frame, width = 4)
date_date_textbox.pack(side=tk.LEFT)
date_date_label = tk.Label(date_frame, text = "日")
date_date_label.pack(side= tk.LEFT)
date_day_textbox = tk.Entry(date_frame, width = 2)
date_day_textbox.pack(side = tk.LEFT)
date_day_label = tk.Label(date_frame, text = "曜日")
date_day_label.pack(side=tk.LEFT)


time_frame = tk.Frame(frame, bg='#D2F3D4')
time_frame.pack()

time_label = tk.Label(time_frame, text="時間:",  anchor=tk.W, justify=tk.LEFT, bg='#D2F3A1')
time_label.pack(side=tk.LEFT)
time_starthour_textbox = tk.Entry(time_frame, width =2)
time_starthour_textbox.pack(side=tk.LEFT)
time_starthour_label = tk.Label(time_frame, text=":")
time_starthour_label.pack(side=tk.LEFT)
time_startminute_textbox = tk.Entry(time_frame, width=2)
time_startminute_textbox.pack(side=tk.LEFT)
time_startminute_label = tk.Label(time_frame, text= "～")
time_startminute_label.pack(side=tk.LEFT)

time_finishhour_textbox = tk.Entry(time_frame, width=2)
time_finishhour_textbox.pack(side=tk.LEFT)
time_finishhour_label = tk.Label(time_frame, text=":")
time_finishhour_label.pack(side=tk.LEFT)
time_finishminute_textbox = tk.Entry(time_frame, width=2)
time_finishminute_textbox.pack(side=tk.LEFT)


name_frame = tk.Frame(frame, bg = "#D2F3D4")
name_frame.pack()

name_student_label = tk.Label(name_frame, text = "生徒名", bg='#D2F3A1')
name_student_label.pack(side = tk.LEFT)
name_student_textbox = tk.Entry(name_frame, width = 15)
name_student_textbox.pack(side= tk.LEFT)
name_teacher_label =tk.Label(name_frame, text = "教師名", bg='#D2F3A1')
name_teacher_label.pack(side=tk.LEFT)
name_teacher_textbox = tk.Entry(name_frame, width = 15)
name_teacher_textbox.pack()


for topic in topics:
    label = tk.Label(frame,  anchor=tk.W, text=topic, justify=tk.LEFT, bg='#D2F3A1')
    label.pack(anchor=tk.W)
    textbox = tk.Text(frame, height=3, width=80)
    textbox.pack()
    pad = tk.Label(frame, height=1, bg='#D2F3D4')
    pad.pack()
    textboxes.append(textbox)



root.mainloop()
