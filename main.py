import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
import fitz

def pdf_listele():
    klasor_adi = "makale"
    dosyalar = os.listdir(klasor_adi)

    pdf_listesi = []
    for dosya in dosyalar:
        if dosya.endswith(".pdf"):
            pdf_listesi.append(dosya)

    return pdf_listesi

def pdf_ilk_sayfa_basligi_al(pdf_adi):
    klasor_adi = "makale"
    pdf_dosya = fitz.open(os.path.join(klasor_adi, pdf_adi))
    sayfa = pdf_dosya.load_page(0)

    metin = sayfa.get_text()
    basliklar = [satir.strip() for satir in metin.split('\n') if satir.strip()]

    if basliklar:
        ilk_baslik = basliklar[0]
        return f"{pdf_adi} ilk sayfadaki başlık: {ilk_baslik}"
    else:
        return f"{pdf_adi} ilk sayfada başlık bulunamadı."

def pdf_isimlerini_goster():
    pdf_listesi = pdf_listele()
    show_custom_message("PDF İsimleri", "\n".join(f"• {pdf}" for pdf in pdf_listesi), "lightblue")

def pdf_basliklari_goster():
    pdf_listesi = pdf_listele()
    basliklar = []

    for pdf_adi in pdf_listesi:
        sonuc = pdf_ilk_sayfa_basligi_al(pdf_adi)
        basliklar.append(f"• {sonuc}")

    show_custom_message("Başlıklar", "\n".join(basliklar), "lightblue")

def show_custom_message(title, message, bg_color):
    custom_window = tk.Toplevel(root)
    custom_window.title(title)

    text_widget = scrolledtext.ScrolledText(custom_window, wrap=tk.WORD, width=40, height=20, font=("Times New Roman", 12))
    text_widget.insert(tk.INSERT, message)
    text_widget.configure(state='disabled')
    text_widget.pack(padx=20, pady=20)

root = tk.Tk()
root.title("PDF İşlemleri")
root.geometry("500x400")
root.configure(bg="pink")

label = tk.Label(root, text="PDF OKUMA SİSTEMİNE HOŞGELDİNİZ!", font=("Times New Roman", 15, "bold"), bg="pink", fg="black")
label.pack(pady=10)

button_pdf_listele = tk.Button(root, text="PDF İsimlerini Göster", command=pdf_isimlerini_goster, bg="blue", fg="white", width=20, height=2, font=("Times New Roman", 12))
button_pdf_listele.pack(pady=10)

button_pdf_basliklari = tk.Button(root, text="PDF Başlıklarını Yaz", command=pdf_basliklari_goster, bg="blue", fg="white", width=20, height=2, font=("Times New Roman", 12))
button_pdf_basliklari.pack(pady=10)

button_cikis = tk.Button(root, text="Çıkış", command=root.destroy, bg="blue", fg="white", width=20, height=2, font=("Times New Roman", 12))
button_cikis.pack(pady=10)

root.mainloop()
