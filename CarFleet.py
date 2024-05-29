class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = sorted(list(zip(position, speed)))[::-1] #ascending order
        res = []

        for pos,speed in pair: 
            res.append((target - pos)/speed) #time of arival 
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        return len(res)
    