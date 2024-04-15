# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.


def make_readable(seconds):
   
    # HH = horas , MM = minutos , SS = segundos
    HH = 0
    MM = 0
    SS = 0 
    
    # Contador para o while
    Counter = seconds

    while Counter > 0:
        # Segundos
        if SS < 59:
            SS += 1
        else:
            SS = 0
            MM += 1 
        # Minutos
        if  MM > 59:
            MM = 0
            HH += 1 

        Counter -= 1 
    
    # Formatando para 2 casas
    HF = str(HH)
    HF = HF.zfill(2)
    
    MF = str(MM)
    MF = MF.zfill(2)

    SF = str(SS)
    SF = SF.zfill(2)
    
    hours_formated = f'{HF}:{MF}:{SF}'
    return hours_formated
