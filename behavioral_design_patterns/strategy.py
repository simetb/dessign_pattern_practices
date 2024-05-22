"""
    Strategy 
    Strategy pattern allows you to switch the algorithm or strategy based upon the situation.
"""
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data): pass
    
class BubbleSort(SortStrategy):
    def sort(self, data):
        print("sorting using bubble sort")
        return data

class QuickSort(SortStrategy):
    def sort(self, data):
        print("sorting using quick sort")
        return data
    
# Then wue have our client 
class Sorter:
    def __init__(self, sorter_small : SortStrategy, sorter_big : SortStrategy) -> None:
        self.sorter_small = sorter_small
        self.sorter_big = sorter_big
    
    def sort(self, data):
        return self.sorter_small.sort(data)  if len(data) <= 5 else self.sorter_big.sort(data)

if __name__ == "__main__":
    smalldataset = [1, 3, 4, 2]
    bigdataset = [1, 4, 3, 2, 8, 10, 5, 6, 9, 7]
    
    sorter = Sorter(BubbleSort(), QuickSort())
    
    sorter.sort(smalldataset)
    sorter.sort(bigdataset)

    