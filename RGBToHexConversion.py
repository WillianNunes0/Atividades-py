# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"


def rgb(r, g, b):
    rgb = [r, g, b]
    rgb_formatted = ''
    for i in rgb:
        # Primeiro dígito
        if i // 16 < 0:
            i1 = '0'
        elif i // 16 < 10:
            i1 = str(i // 16)
        else:
            if i // 16 == 10:
                i1 = 'A'
            elif i // 16 == 11:
                i1 = 'B'
            elif i // 16 == 12:
                i1 = 'C'
            elif i // 16 == 13:
                i1 = 'D'
            elif i // 16 == 14:
                i1 = 'E'
            elif i // 16 == 15:
                i1 = 'F'
        # Segundo dígito
        if i % 16 < 0:
            i2 = '0'
        elif i % 16 < 10:
            i2 = str(i % 16)
        else:
            if i % 16 == 10:
                i2 = 'A'
            elif i % 16 == 11:
                i2 = 'B'
            elif i % 16 == 12:
                i2 = 'C'
            elif i % 16 == 13:
                i2 = 'D'
            elif i % 16 == 14:
                i2 = 'E'
            elif i % 16 == 15:
                i2 = 'F'
        # Obter hexadecimal RGB
        rgb_formatted += f'{i1}{i2}'
    return rgb_formatted
        