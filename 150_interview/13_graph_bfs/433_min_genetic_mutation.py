from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]):
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        possible_muts = ["A", "C", "G", "T"]
        checked_paths = {startGene}
        que = deque()
        que.append((startGene, 0))  # gen + liczba mutacji

        while que:
            gene, mutations = que.popleft()
            if gene == endGene:
                return mutations

            for possible_mutation in possible_muts:
                for i in range(len(gene)):
                    if possible_mutation == gene[i]:
                        continue
                    temp = gene[:i] + possible_mutation + gene[i + 1 :]
                    if temp not in checked_paths and temp in bank_set:
                        checked_paths.add(temp)
                        que.append((temp, mutations + 1))
        return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

print(Solution().minMutation(startGene, endGene, bank))
assert Solution().minMutation(startGene, endGene, bank) == 2
