import tkinter as tk
from tkinter import filedialog
import vlc
import os

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("视频播放器")
        self.root.geometry("800x600")

        self.player = vlc.MediaPlayer()

        self.create_widgets()

    def create_widgets(self):
        self.btn_open = tk.Button(self.root, text="打开视频文件", command=self.open_file)
        self.btn_open.pack(pady=20)

        self.btn_play = tk.Button(self.root, text="播放", command=self.play)
        self.btn_play.pack(pady=10)

        self.btn_pause = tk.Button(self.root, text="暂停", command=self.pause)
        self.btn_pause.pack(pady=10)

        self.btn_stop = tk.Button(self.root, text="停止", command=self.stop)
        self.btn_stop.pack(pady=10)

        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack(pady=20)

    def open_file(self):
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="选择视频文件", filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))
        if file_path:
            media = vlc.Media(file_path)
            self.player.set_media(media)
            self.player.set_hwnd(self.video_frame.winfo_id())

    def play(self):
        if not self.player.is_playing():
            self.player.play()

    def pause(self):
        if self.player.is_playing():
            self.player.pause()
        else:
            self.player.play()

    def stop(self):
        self.player.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
