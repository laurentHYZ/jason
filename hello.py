gems = 0
gems += 1 ement gems by 1 
gems -= 1 #we decrement gems by 1 
print(gems)
for step in range(10):
    gems += 1
print(gems)

# let's imagine that you and me start with a wallet that
# in my wallet I have 100 rmb
# in your wallet , there is nothing
# we want to create a verb/function, that will reward you
# When I want to reward you, it will take some money out of my wdtAccountCollection
# and it will add that same amount, to your wallet
coach_wallet = 100 # we introduce the variable xxxx and we set it to xxxx 
jason_wallet = 0

def reward_jason():
    '''sdfgsdfg''' 
    coach_wallet -= 1
    jason_wallet += 1

reward_jason()
print(jason_wallet) # ---> it will print 1, correcty
for step in range(10):
    reward_jason()

# sometimes, the tasks that our hero Jason must accomplish are easy
# sometimes they are difficult
# we want to reward him, accordingly 
# so we want our reward_jason() function to take an argument/parameter
# e.g. reward_jason(10)

def reward_jason(a):
    coach_wallet -= a
    jason_wallet += a
reward_jason(10)
reward_jason(20)

# next time, we will build  a list of product, each product has a price, 
# you will use your wallet to buy those items 







# jason.write()
You Jason, write!
# Walk fast !
walk(fast)
# Come ! 
come()
# Write()
write()
# write(“hello”)
Write “hello”!!
# Say “Hi !
say(“Hi”)
# Say “thank you Dad!” !
say(“thank you Dad!”)
# say(“pleased to meet you.”)
Say "pleased to meet you"!
# Mike’s bike
mike.bike
# The bike of Mike
# Mike.bike
# The dad of Mike 
mike.dad
# Mike’s dad
# jason.mother
Jason's mother
# The age of Mike
# Mike.age
# The age of mike is 11
mike.age = 11
# Mike.age = 11
# The age of jason 
# jason.mother.age
# jason.mother.age = 30
Jason's mother's age is 30.
