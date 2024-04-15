# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].

def dir_reduc(arr):
    
    opostos = {
        'NORTH': 'SOUTH', 'SOUTH': 'NORTH',
        'EAST': 'WEST', 'WEST': 'EAST'
              }
    
    resultado = [] 
    for direcao in arr:

        if resultado and opostos[direcao] == resultado[-1]:
            resultado.pop()
        else:
            resultado.append(direcao)
    
    return resultado
