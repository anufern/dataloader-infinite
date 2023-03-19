
from torch.utils.data import DataLoader, Dataset, Sampler
import random
from itertools import cycle

class CreateDataset(Dataset):
    def __init__(self):
        self.varList = [4,5,6,7,8]
    def __len__(self):
        return len(self.varList)
    def __getitem__(self, idx) :
        return self.varList[idx]

class customSampler(Sampler) :
    def __init__(self, dataset, shuffle):
        assert len(dataset) > 0
        self.dataset = dataset
        self.shuffle = shuffle
    
    def __iter__(self):
        order = list(range((len(self.dataset))))
        idx = 0
        while True:
            yield order[idx]
            idx += 1
            if idx == len(order):
                if self.shuffle:
                    random.shuffle(order)
                idx = 0

if __name__ == "__main__":
    dset = CreateDataset()
    sampler = customSampler(dset, shuffle=True)
    loader = iter(DataLoader(dataset=dset, sampler=sampler, batch_size=15, num_workers=2))
    
    # For demonstation
    for x in range(10):
        i = next(loader)
        print(i)
    
    #For infinite loop

    #for i, data in cycle(enumerate(loader)):
    #    print(i, data)
    