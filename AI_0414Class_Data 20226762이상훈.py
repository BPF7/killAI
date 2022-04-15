# dictionary & for 반복문 활용하기

avenger_dic = { "Type": "Hero Movie","Cast": "Ironman","Power": 50000 }


print(avenger_dic["Cast"],avenger_dic["Power"])
for avenger in avenger_dic:
    print(avenger,":",avenger_dic[avenger])


movie_dic = {
    "Title": ["Avengers End Game"],
    "Type": ["Hero Movie"],
    "Director": ["Ansony Luso","Joe Luso"],
    "Cast": ["Ironman","Hulk","Doctor_strange","Thor"],
    "Theater": ["CGV","Lotte_cinema"],
    "Time": [ 9,12,13,18,22 ]
    }

for contents in movie_dic:
    print("="*9+"=\n",contents,"\n="+"="*9)
    for factor in movie_dic[contents]:
        print(factor)

print()



# 리스트 안의 사전, 반복문 활용

aven_list = [ { "cast": "Ironman", "power": 50000 },\
              { "cast": "Thor", "power": 80000 },\
              { "cast": "Spiderman", "power": 30000 },\
              { "cast": "Antman", "power": 45000 },\
              { "cast": "Hulk", "power": 60000 } ]


print(aven_list[1]["cast"],aven_list[1]["power"])
for avenger in aven_list:
    print(avenger["cast"],":",avenger["power"])
print()   


# 사전 안의 리스트, 반복문 활용

avengers = { "Casts": [ "Ironman","Thor","Spiderman","Antman","Hulk" ],\
             "Powers": [ 50000,80000,30000,45000,60000 ] }

print(avengers["Casts"][2],avengers["Powers"][2])


for avenger in range(len(avengers["Casts"])):
    print(avengers["Casts"][avenger],":",avengers["Powers"][avenger])

# 반복문 활용하여 키와 값을 조합한 사전 만들기

hero_list = [ "Ironman","Thor","Spiderman","Antman","Hulk" ]
power_list = [ 50000,80000,30000,45000,60000 ]



hero_dic = { }

hero_dic[hero_list[4]]=power_list[4]
print(hero_dic)


for hero in range(len(hero_list)):
    hero_dic[hero_list[hero]]=power_list[hero]
print(hero_dic)




