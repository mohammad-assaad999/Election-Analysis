# counties=list('Arapahoe','Denver','Jefferson')
# print(counties)
# counties.insert(1,"El Paso")
# print(counties)
# counties.pop(0)
# print(counties)
# counties.pop(1)
# counties.insert(2,"Denver")
# print(counties)
# counties.append("Arapahoe")
# print(counties)

# mytuple = ('Arapahoe','Denver','Jefferson')
# print(mytuple [:-1])

# mydict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
# # print(mydict)
# # print(mydict.items())
# print(mydict.keys())

# voting_data=[]
# voting_data.append({"county":"Arapahoe","voters":422829})
# voting_data.append({"County":"Denver","voters":463353})
# voting_data.append({"county":"Jefferson","Voters":432438})
# print(voting_data)
# voting_data.insert(1,{"county":"El Paso","voters":461149})
# voting_data.remove({"county":"Arapahoe","voters":422829})
# voting_data.remove({"County":"Denver","voters":463353})
# voting_data.insert(2,{"County":"Denver","voters":463353})
# voting_data.append({"county":"Arapahoe","voters":422829})
# print(voting_data)

# counties=['Arapahoe','Denver','Jefferson']
# if counties[1]=='Denver':
#     print(counties[1])

# temperature = int(input("What is the temperature outside?"))
# if temperature > 80:
#     print("Turn on the AC")
# else:
#     print("open the window")

#What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')

# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# voting_data=[]
# voting_data.append({"county":"Arapahoe","voters":422829})
# voting_data.append({"County":"Denver","voters":463353})
# voting_data.append({"county":"Jefferson","Voters":432438})
# print(voting_data)
# voting_data.insert(1,{"county":"El Paso","voters":461149})
# voting_data.remove({"county":"Arapahoe","voters":422829})
# voting_data.remove({"County":"Denver","voters":463353})
# voting_data.insert(2,{"County":"Denver","voters":463353})
# voting_data.append({"county":"Arapahoe","voters":422829})

# for county in voting_data:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# for hoho in range(5):
#     print(hoho)

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])

# numbers=[0,1,2,3,4,5]
# for num in range(len(numbers)): 
#     print(numbers[num])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for c, v in counties_dict.items():
#     # print(c,v)
#     print(f"{c} county has {v} registered votes")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for j in voting_data:
#     for i,k in j.items():
#         print(i,k)

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for i,j in counties_dict.items():
#     print(f'{i} has a registered voters of {j}')
#     print(i + " has registered voters of " + str(j))

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for i,j in counties_dict.items():
    print(f'{i} county has {j:,.0f} registered voters.')