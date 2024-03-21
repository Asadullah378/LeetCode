class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.requests = []

    def ping(self, t: int) -> int:
        
        self.requests.append(t)

        end = (t-3000)

        while self.requests[0]<end:
            self.requests.pop(0)

        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
