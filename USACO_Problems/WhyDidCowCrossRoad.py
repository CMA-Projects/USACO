"""
Farmer John, in his old age, has unfortunately become increasingly grumpy and paranoid. 
Forgetting the extent to which bovine diversity helped his farm truly flourish over the years, 
he has recently decided to build a huge fence around the farm, discouraging cows from neighboring 
farms from visiting, and completely prohibiting entry from a handful of neighboring farms. The cows 
are quite upset by this state of affairs, not only since they can no longer visit with their friends, 
but since it has caused them to cancel participation in the International Milking Olympiad, an 
event to which they look forward all year.
Neighboring cows that still have the ability to enter Farmer John's property find the process has 
become more arduous, as they can enter only through a single gate where each cow is subject to intense 
questioning, often causing the cows to queue up in a long line.

For each of the N cows visiting the farm, you are told the time 
she arrives at the gate and the duration of time required for her to answer 
her entry questions. Only one cow can be undergoing questioning at any given time, so if 
many cows arrive near the same time, they will likely need to wait in line to be processed one 
by one. For example, if a cow arrives at time 5 and answers questions for 7 units of time, another 
cow arriving at time 8 would need to wait until time 12 to start answering questions herself.

Please determine the earliest possible time by which all cows are able to enter the farm.

INPUT FORMAT (file cowqueue.in):
The first line of input contains N, a positive integer at most 100. Each of the next N 
lines describes one cow, giving the time it arrives and the time it requires for questioning; each 
of these numbers are positive integers at most 1,000,000.

OUTPUT FORMAT (file cowqueue.out):
Please determine the minimum possible time at which all the cows could have completed processing.

SAMPLE INPUT:
3
2 1
8 3
5 7

SAMPLE OUTPUT:
15

Here, first cow arrives at time 2 and is quickly processed. 
The gate remains briefly idle until the third cow arrives at time 5, 
and begins processing. The second cow then arrives at time 8 and waits 
until time 5+7=12 to start answering questions, finishing at time 12+3 = 15.
"""

import sys
sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

n = int(input())
current_time = 0
cows = []

for i in range(n):
    cows.append(list(map(int,input().split())))

cows.sort()

for cow in cows:
    if current_time > cow[0]:
        current_time += cow[1]
    else:
        current_time = cow[0] + cow[1]

print(current_time)