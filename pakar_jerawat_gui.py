import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog

prolog = Prolog()
prolog.consult("pakar_jerawat_gui.pl")  

gejala_list = []
index_gejala = 0

def ambil_gejala_dari_prolog():
    global gejala_list
    gejala_list = []
    for result in prolog.query("pertanyaan(G, _)"):
        gejala_list.append(result["G"])

def ambil_pertanyaan(gejala):
    for result in prolog.query(f"pertanyaan({gejala}, Teks)") :
        return result["Teks"]
    return ""

def tampilkan_pertanyaan():
    global index_gejala
    if index_gejala < len(gejala_list):
        gejala = gejala_list[index_gejala]
        teks = ambil_pertanyaan(gejala)
        kotak_pertanyaan.configure(state=tk.NORMAL)
        kotak_pertanyaan.delete("1.0", tk.END)
        kotak_pertanyaan.insert(tk.END, teks)
        kotak_pertanyaan.configure(state=tk.DISABLED)
    else:
        tampilkan_diagnosa()

def jawab(ya):
    global index_gejala
    gejala = gejala_list[index_gejala]
    if ya:
        prolog.assertz(f"gejala_pos({gejala})")
    else:
        prolog.assertz(f"gejala_neg({gejala})")
    index_gejala += 1
    tampilkan_pertanyaan()

def tampilkan_diagnosa():
    hasil = None
    for result in prolog.query("penyakit(P), findall(G, (gejala(G, P), gejala_pos(G)), L), length(L, N), N > 1"):
        hasil = result["P"]
        break

    if hasil:
        messagebox.showinfo("Hasil Diagnosa", f"Anda terdeteksi mengalami '{hasil}'.")
    else:
        messagebox.showinfo("Hasil Diagnosa", "Gejala tidak cukup untuk menentukan jenis jerawat.")

def mulai_diagnosa():
    global index_gejala
    prolog.retractall("gejala_pos(_)")  # Hapus fakta lama
    prolog.retractall("gejala_neg(_)")
    index_gejala = 0
    ambil_gejala_dari_prolog()
    tampilkan_pertanyaan()

# GUI setup
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Jerawat")
root.geometry("700x500")  # Menyesuaikan ukuran jendela

# Menambahkan warna latar belakang dan font
root.config(bg="#f1f1f1")

# Judul dengan warna dan font yang menarik
label_judul = tk.Label(root, text="Aplikasi Diagnosa Jenis Jerawat", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white", pady=10)
label_judul.pack(fill=tk.X, padx=20)

# Kotak pertanyaan dengan desain lebih bersih
kotak_pertanyaan = tk.Text(root, height=5, width=60, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 14), bd=0, bg="#e0f2f1", fg="#004d40")
kotak_pertanyaan.pack(pady=20)

# Frame untuk tombol
frame_tombol = tk.Frame(root, bg="#f1f1f1")
frame_tombol.pack(pady=10)

# Tombol "Tidak" dengan desain modern
btn_tidak = tk.Button(frame_tombol, text="Tidak", width=15, command=lambda: jawab(False), font=("Arial", 12), bg="#FF6347", fg="white", relief=tk.RAISED, bd=3)
btn_tidak.grid(row=0, column=0, padx=20)

# Tombol "Ya" dengan desain modern
btn_ya = tk.Button(frame_tombol, text="Ya", width=15, command=lambda: jawab(True), font=("Arial", 12), bg="#32CD32", fg="white", relief=tk.RAISED, bd=3)
btn_ya.grid(row=0, column=1, padx=20)

# Tombol Mulai Diagnosa dengan desain lebih besar
btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=mulai_diagnosa, font=("Arial", 14, "bold"), bg="#1E90FF", fg="white", relief=tk.RAISED, bd=5, width=20)
btn_mulai.pack(pady=30)

root.mainloop()
