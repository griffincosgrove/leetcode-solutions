class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        '''
        smash the two largest stones together and based on their arithmatic relationship determine outcome
        
        
        inputs
            arg1: stones: integer list
        
        outputs
            integer - output 0 if 0 stones remain, or return the last stone left
        
        Process
            smash stones and determine outcome
            
        Approach 1:
            continually sort the stones array to find the min element and perform arthimatic
            continued selection sort will lead to an inneficient run time
        
        Approach 2:
            continued min/max operations lead me to believe a heap would be the best data structure to use.
            pop two stones and subtract them and push the result back
            
            psuedo code
            heapify stones - O(n) time *negate the stones to create a max queue
            while min_heap > 1 
                pop two stones and subtract them
                if stone1 != stone2
                    push (result)
                else
                    pass - we do not need to do anything if the stones equal eachother
            if min_heap is empty return 0
            else return pop(min_heap)
            
            *be very aware of keeping the sign negative to keep max queue
        '''
        
        import heapq as h
        
        if len(stones) == 1:
            return stones[0]
        
        if stones[0] is None:
            return 0
        
        stones = [-x for x in stones] # turns everything negative so result is max queue
        
        h.heapify(stones)
        
        while (len(stones) > 1):
            stone1 = (h.heappop(stones) * -1)
            stone2 = (h.heappop(stones) * -1)
            if stone1 != stone2:
                h.heappush(stones, ((stone1 - stone2) * -1)) 
        if not stones:
            return 0
        else:
            return (stones[0] * -1)

