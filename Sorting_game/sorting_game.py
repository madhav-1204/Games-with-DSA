import tkinter as tk
from tkinter import ttk, messagebox
import random
import threading
import time

# --- Setup window ---
root = tk.Tk()
root.title("Sorting Race Visualizer")
root.geometry("1000x650")
root.config(bg="#222")

# --- Title ---
title = tk.Label(
    root,
    text="🏁 Sorting Algorithm Race 🏁",
    font=("Helvetica", 20, "bold"),
    fg="white",
    bg="#222",
)
title.pack(pady=20)

# --- Frame for canvases ---
canvas_frame = tk.Frame(root, bg="#222")
canvas_frame.pack(fill="both", expand=True)

# --- Helper to create labeled canvas ---
def create_canvas_with_label(parent, label_text):
    frame = tk.Frame(parent, bg="#222")
    label = tk.Label(
        frame,
        text=label_text,
        font=("Helvetica", 14, "bold"),
        fg="white",
        bg="#222",
    )
    label.pack()
    canvas = tk.Canvas(frame, width=300, height=400, bg="black")
    canvas.pack(padx=10, pady=10)
    frame.pack(side="left", expand=True)
    return canvas

# --- Create canvases ---
bubble_canvas = create_canvas_with_label(canvas_frame, "Bubble Sort")
merge_canvas = create_canvas_with_label(canvas_frame, "Merge Sort")
quick_canvas = create_canvas_with_label(canvas_frame, "Quick Sort")

# --- Draw bars ---
def draw_bars(canvas, data, color="#3A86FF"):
    canvas.delete("all")
    c_height = 400
    c_width = 300
    bar_width = c_width / len(data)
    for i, value in enumerate(data):
        x0 = i * bar_width
        y0 = c_height - value
        x1 = (i + 1) * bar_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
    canvas.update()

# --- Generate data ---
def generate_data():
    return [random.randint(10, 400) for _ in range(30)]

# --- Global race tracker ---
results = {}
lock = threading.Lock()

def finish_race(name, start_time):
    global results
    end_time = time.time() - start_time
    with lock:
        results[name] = end_time
        # If all 3 finished
        if len(results) == 3:
            winner = min(results, key=results.get)
            msg = f"🏆 {winner} wins!\n\n"
            msg += f"⏱️ Times:\n"
            for k, v in results.items():
                msg += f"{k}: {v:.2f}s\n"
            # Check bet
            if bet_choice.get() == winner:
                msg += f"\n🎉 You guessed right!"
            else:
                msg += f"\n❌ You guessed {bet_choice.get()}!"
            messagebox.showinfo("Race Results", msg)

# --- Sorting algorithms ---
def bubble_sort(data, canvas, name):
    start_time = time.time()
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            draw_bars(canvas, data, color="#FF595E")  # red
            time.sleep(0.01)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        draw_bars(canvas, data)
    draw_bars(canvas, data, color="#06D6A0")
    finish_race(name, start_time)

def merge_sort(data, canvas, name):
    start_time = time.time()
    def merge_sort_recursive(arr, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort_recursive(arr, l, m)
            merge_sort_recursive(arr, m + 1, r)
            merge(arr, l, m, r)
            draw_bars(canvas, arr, color="#C77DFF")
            time.sleep(0.05)
    def merge(arr, l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    merge_sort_recursive(data, 0, len(data) - 1)
    draw_bars(canvas, data, color="#06D6A0")
    finish_race(name, start_time)

def quick_sort(data, canvas, name):
    start_time = time.time()
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            draw_bars(canvas, arr, color="#FF595E")
            time.sleep(0.01)
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)
    quick_sort_recursive(data, 0, len(data) - 1)
    draw_bars(canvas, data, color="#06D6A0")
    finish_race(name, start_time)

# --- Start Race ---
def start_race():
    global results
    results = {}  # reset
    data = generate_data()
    bubble_data, merge_data, quick_data = data[:], data[:], data[:]
    draw_bars(bubble_canvas, bubble_data)
    draw_bars(merge_canvas, merge_data)
    draw_bars(quick_canvas, quick_data)
    threading.Thread(target=bubble_sort, args=(bubble_data, bubble_canvas, "Bubble Sort")).start()
    threading.Thread(target=merge_sort, args=(merge_data, merge_canvas, "Merge Sort")).start()
    threading.Thread(target=quick_sort, args=(quick_data, quick_canvas, "Quick Sort")).start()

# --- Betting UI ---
bet_frame = tk.Frame(root, bg="#222")
bet_frame.pack(pady=10)
tk.Label(bet_frame, text="Place your bet 🎲:", font=("Helvetica", 14), fg="white", bg="#222").pack(side="left", padx=10)
bet_choice = tk.StringVar(value="Bubble Sort")
bet_menu = ttk.Combobox(bet_frame, textvariable=bet_choice, values=["Bubble Sort", "Merge Sort", "Quick Sort"], state="readonly")
bet_menu.pack(side="left", padx=5)

# --- Start Button ---
start_button = ttk.Button(root, text="Start Race", command=start_race)
start_button.pack(pady=20)

root.mainloop()
