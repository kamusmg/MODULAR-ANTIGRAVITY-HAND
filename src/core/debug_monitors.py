import mss

def debug_monitors():
    with mss.mss() as sct:
        for i, m in enumerate(sct.monitors):
            print(f"Monitor {i}: {m}")

if __name__ == "__main__":
    debug_monitors()
