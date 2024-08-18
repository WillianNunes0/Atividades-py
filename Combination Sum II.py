"""
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

    Each number in candidates may only be used once in the combination.

    Note: The solution set must not contain duplicate combinations.
    """

def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            # Adiciona a combinação encontrada à lista de possibilidades
            possibilidades.append(path)
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            # Pula elementos duplicados para evitar combinações duplicadas
            if i > start and candidates[i] == candidates[i-1]:
                continue
            # Faz a chamada recursiva para o próximo nível de combinação
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])
    
    possibilidades = []
    candidates.sort()  # Ordena a lista de candidatos
    backtrack(0, target, [])
    return possibilidades

print(combinationSum2([10,1,2,7,6,1,5], 8))


