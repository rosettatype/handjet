import drawBot as db


def draw_text(txt, fontname, fontsize, txt_color, fea={}, vary={},
              shift=(0, 0)):
    with db.savedState():
        fs = db.FormattedString(txt, font=fontname, fontSize=fontsize,
                                fill=txt_color,
                                openTypeFeatures=fea, fontVariations=vary)
        txt_w, txt_h = db.textSize(fs)
        db.translate((page_w - txt_w)/2, (page_h - txt_h)/2)
        db.text(fs, shift)


page_w, page_h = 1080, 1080
sets = [
    ("Handjet!", (11, 70), 500, 200, 5),
    ("Get it!", (11, 120), 900, 100, 9),
    ("Use it!", (11, 70), 700, 200, 5),
    ("Play it!", (11, 120), 1100, 100, 9),
    ("Break it!", (11, 120), 400, 100, 9),
    ("Fix it!", (11, 70), 200, 200, 5),
    ("Love it!", (11, 70), 1000, 100,  5),
    ]
fontname = "Handjet-Regular_"
fontsize = 300
bg_color = (33/255, 33/255, 33/255)
txt_color = (230/255, 250/255, 40/255)
label_txt = "1+198 new & free fonts from Rosetta"
label_size = 60
label_vary = {"wght": 40, "wdth": 500, "opsz": 100}

db.newDrawing()
for txt, (wght_min, wght_max), wdth, opsz, step in sets:
    for wght in range(wght_min, wght_max, step):
        vary = {"wght": wght, "wdth": wdth, "opsz": opsz}
        db.newPage(page_w, page_h)
        db.fill(*bg_color)
        db.rect(0, 0, page_w, page_h)
        draw_text(txt, fontname, fontsize, txt_color,
                  vary=vary, shift=(0, 140))
        draw_text(label_txt, fontname, label_size, txt_color,
                  vary=label_vary, shift=(0, -270))
    for wght in range(wght_max, wght_min, -step):
        vary = {"wght": wght, "wdth": wdth, "opsz": opsz}
        db.newPage(page_w, page_h)
        db.fill(*bg_color)
        db.rect(0, 0, page_w, page_h)
        draw_text(txt, fontname, fontsize, txt_color,
                  vary=vary, shift=(0, 140))
        draw_text(label_txt, fontname, label_size, txt_color,
                  vary=label_vary, shift=(0, -270))
db.saveImage("handjet_basic.mp4")
