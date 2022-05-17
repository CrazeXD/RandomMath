def doppler(speed, sos, frequency, direction, observer) -> int:
    if direction == True:
        if observer == True:
            top = sos+speed
            inparenth = top/sos
            freq = inparenth*frequency
            return freq
        elif observer == False:
            bottom = sos=speed
            inparenth = sos/bottom
            freq = inparenth*frequency
            return freq
    elif direction == False:
        if observer == True:
            top = sos-speed
            inparenth = top/sos
            freq = inparenth*freq
            return freq
        elif observer == False:
            bottom = sos+speed
            inparenth = sos/bottom
            freq = inparenth*frequency
            return freq
