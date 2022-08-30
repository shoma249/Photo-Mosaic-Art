

import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def colorGet(photo):
    # 対象範囲の切り出し
    boxFromX = 20 #対象範囲開始位置 X座標
    boxFromY = 40 #対象範囲開始位置 Y座標
    boxToX = 80   #対象範囲終了位置 X座標
    boxToY = 60   #対象範囲終了位置 Y座標
    # y:y+h, x:x+w の順で設定
    imgBox = photo[boxFromY: boxToY, boxFromX: boxToX]

    # RGB平均値を出力
    # falttenで一次元化しmeanで平均を取得
    b = imgBox.T[0].flatten().mean()
    g = imgBox.T[1].flatten().mean()
    r = imgBox.T[2].flatten().mean()

    # RGB平均値を取得
    print("B: %.2f" % (b))
    print("G: %.2f" % (g))
    print("R: %.2f" % (r))

def photo():
    filename = filedialog.askopenfilename(
        title="画像ファイルを開く",
        filetypes=[("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"),
                   ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif")],  # ファイルフィルタ
        initialdir='C:\\pg'  # 開くディレクトリ
    )

    img = cv2.imread(filename)
    img2 = cv2.imread(filename, cv2.IMREAD_COLOR)
    colorGet(img2)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)

    canvas = tk.Canvas(root, width=img.shape[0], height=img.shape[1])
    canvas.pack()
    canvas.create_image(0, 0, image=img_tk, anchor='nw')

    root.mainloop()


# rootメインウィンドウの設定
root = tk.Tk()
root.title("application")
# root.geometry("200x100")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

# 各種ウィジットの作成
button = ttk.Button(frame, text="photo", command=photo)
button.grid(row=0, column=1)

root.mainloop()
