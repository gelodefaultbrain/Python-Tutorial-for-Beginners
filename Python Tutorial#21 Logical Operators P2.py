'''
Facebook Page: https://www.facebook.com/gelsdefaultskin
or just search for @gelsdefaultskin


I do live streaming gaming & coding streams :)
'''




cond = not 1==1 and 6 > 10 or 2 < 10
'''
          F     and  6 > 10 or 2 < 10
          F     and    F     or 2 < 10
                 F           or 2 < 10
                 F           or  T
                            T
'''




cond2 = not 1==1 and (6 > 10 or 2 < 10)
'''
        not 1==1  and   (F or T)
        not 1==1  and      T
        F   and      T
             F
'''


print("Value of cond is: ",cond)
print("Value of cond2 is: ",cond2)
