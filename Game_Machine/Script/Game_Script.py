# -*- coding: utf-8 -*-
'''
Created on 2019年9月19日

@author: likecan
'''
from Game_Machine.Base.Hero_Move import hero_move
from Game_Machine.Base.Heroic_Skill import heroic_skill


class game_scipt():
    
    
    def __init__(self,depth):
        self.depth = depth
        
    
    def simpale_play(self):
        heroic_skill.skill_plus_one(100, 100, self.depth)
        hero_move.upper_right(100, 100)
        for i in range(10):
            heroic_skill.flat_a()
        heroic_skill.skill_one(100, 100, self.depth)
        for i in range(5):
            heroic_skill.flat_a()
        heroic_skill.skill_one(100, 100, self.depth)
