import math


def count_down(count, timer):
    my_text = ""
    if count % 60 < 10 and count / 60 < 10:
        my_text = f"0{math.floor(count / 60)}:0{int(count % 60)}"
    elif count / 60 < 10:
        my_text = f"0{math.floor(count / 60)}:{int(count % 60)}"
    elif count % 60 < 10:
        my_text = f"{math.floor(count / 60)}:0{int(count % 60)}"
    else:
        my_text = f"{math.floor(count / 60)}:{int(count % 60)}"

    timer.config(text=my_text)
