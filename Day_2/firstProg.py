# Program 1
# A Water Jug Problem: You are given two jugs, a 4-gallon one and a 3-gallon one, a pump which has 
# unlimited water which you can use to fill the jug, and the ground on which water may be poured. Neither 
# jug has any measuring markings on it. How can you get exactly 2 gallons of water in the 4-gallon jug?
# Implement using a python program
# Program 2
# Implementation of Tic-Tac-Toe game using a python Program.

def water_jug_prog():
    jug4=0
    jug3=3
    print(f"Fill 3-gallon jug:jug4={jug4},jug3={jug3}-->({jug4},{jug3})")
    
    jug4+=jug3
    jug3=0
    print(f"Fill 4-gallon jug:jug4={jug4},jug3={jug3}-->({jug4},{jug3})")
    
    jug3=3
    print(f"Fill 3-gallon jug:jug4={jug4},jug3={jug3}-->({jug4},{jug3})")
    
    size_jug4=4-jug4
    if jug3<=size_jug4:
        jug4+=jug3
        jug3=0
    else :
        jug3-=size_jug4
        jug4=4
    print(f"Fill 4-gallon jug & Pour 3-gallon jug:jug4={jug4},jug3={jug3}-->({jug4},{jug3})")
    jug4=0
    print(f"Pour 4-gallon jug:jug4={jug4},jug3={jug3}-->({jug4},{jug3})")
    
    jug4=jug3
    jug3=0
    print(f"Fill 4-gallon jug:jug4={jug4},jug3={jug3}-->({jug4},{jug3})")
    
water_jug_prog()