class dynamic_queue:
    def __init__(self, cap):
        self.queue=[]
        self.length=0
        self.capacity=cap

    def queue_push(self, val):
        if self.length == self.capacity:
            print('Max Capacity reached...')
            return None
        self.queue.insert(0, val)
        self.length+=1
        print('Element queued...')

    def queue_pop(self):
        if self.length == 0:
            print('Empty queue')
            return None
        self.queue.pop()
        self.length-=1

    def length_of_queue(self):
        print('Current length of queue' + str(self.length))

    def get_val_by_index(self, index):
        if self.length == 0:
            print('Empty queue')
            return None
        print('Element at index ' + str(index) + ': ' + str(self.queue[index-1]))








