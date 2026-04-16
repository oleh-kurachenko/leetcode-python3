from typing import List, Dict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]],
                          items2: List[List[int]]) -> List[List[int]]:
        items = dict(items1)

        for k, v in items2:
            if k not in items:
                items[k] = v
            else:
                items[k] += v

        return list(map(list, sorted(items.items())))
