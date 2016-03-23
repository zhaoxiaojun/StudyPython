#coding=utf8
#查找

def sequential_search(a_list, item):
    '''
    顺序查找
    '''
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found



def Binary_Search(L, key):
    '''
    二分查找
    '''
    low = 0
    hight = len(L)-1
    while low<=hight:
        mid = (low+hight)/2
        if L[mid]>key:
            hight = mid-1
        elif L[mid]<key:
            low = mid+1
        else:
            return mid
    return -1



class HashTable:
    '''
    哈希查找
    '''
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    #put data in slot
    def put_data_in_slot(self,key,data,slot):
        if self.slots[slot] == None: # '==None' ? or  'is None' ?
            self.slots[slot] = key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key: # not None
                self.data[slot] = data #replace
                return True
            else:
                return False

    def put(self, key, data):
        slot = self.hash_function(key, self.size);
        result = self.put_data_in_slot(key,data,slot);
        while not result:
            slot = self.rehash(slot, self.size);
            result = self.put_data_in_slot(key,data,slot);

    #reminder method
    def hash_function(self, key, size):
        '''
        哈希函数
        '''
        return key % size

    #plus 1
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)





if __name__ == '__main__':
    L = [23,34,57,3,2,3,86,45,6,9]
    L.sort()
    key = 86
    print L
    print sequential_search(L, key)

    table=HashTable();
    table[54]='cat';
    table[26]='dog';
    table[93]='lion';
    table[17]="tiger";
    table[77]="bird";
    table[44]="goat";
    table[55]="pig";
    table[20]="chicken";
    print table.slots;
    print table.data;
