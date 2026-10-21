class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        '''

        1. turn position and speed into tuples in cars arr
        2. sort input based on position smallest to largest
        iterate through arr in reverse order
            add car to stack
            if time to finish of car at end of stack is X, all cars that can get to finish in time < X are apart of that car fleet
            delete car that was added to stack, as its now apart of the car fleet
        
        stack initially empty
        
        return length of stack # number of car fleets

        how to calculate time to finish line: math.ceil(target/speed)




        '''


        stack = []
        cars = []

        for p, s in zip(position, speed):

            arrivalTime = (target-p)/s
            cars.append((p,arrivalTime))
        
        cars.sort() #python automatically sorts tuples by their first integer (int1, int2)


        for car in cars[::-1]:
        

            if stack and car[1] <= stack[-1][1]:
                continue
            else:
                stack.append(car)

        return len(stack)





        