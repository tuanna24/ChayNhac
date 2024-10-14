import tkinter as tk
from tkinter import messagebox
import time
import pygame  # Thêm thư viện pygame

def run_text(widget, lyrics, delays):
    for line, delay in zip(lyrics, delays):
        for char in line:
            widget.insert(tk.END, char)
            widget.update()
            time.sleep(delay) 
        widget.insert(tk.END, '\n') 
    messagebox.showinfo("Thông Báo!", "Cho Anh Tựa Vào Vai Em Có Được Không ?")
    pygame.mixer.music.stop()  # Dừng nhạc khi hoàn tất

# Khởi động pygame
pygame.mixer.init()

# Thay đổi đường dẫn đến file nhạc của bạn
music_file = r"D:\Python_AI\nhac.mp3"  # Thay "your_music_file.mp3" bằng tên file của bạn

pygame.mixer.music.load(music_file)  # Tải file nhạc
pygame.mixer.music.play()  # Phát nhạc

root = tk.Tk()
root.title("Chạy Văn Bản Từng Chữ")

text_widget = tk.Text(root, wrap=tk.WORD, height=20, width=60)
text_widget.pack(pady=20, padx=20)

lyrics = [
    "Cho anh tựa vào vai em có được không?",
    "Cho anh tựa vào vai em có được không?",
    "Để cho anh được cảm thấy anh không một mình lạc lõng",
    "Để anh vơi đi những nỗi lo bận lòng?",
    "",
    "Cho anh tựa vào vai em có được không?",
    "Cho anh tựa vào vai em có được không?",
    "Để anh yên những giây phút muốn con tim mình trống không",
    "Giữa thế giới vô tình vẫn yên bình!"
]

delays = [0.14, 0.15, 0.12, 0.17, 0.15, 0.15, 0.13, 0.15] 

# Tính toán kích thước của cửa sổ và vị trí trung tâm
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.after(100, lambda: run_text(text_widget, lyrics, delays))

root.mainloop()
