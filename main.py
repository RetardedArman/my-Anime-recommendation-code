import random
import time
import csv


def find_anime( mood , nerve_stat ) :
    matchs = []
    for i in range (len(anime_list)) :
        if mood == 2 :
            if int(anime_list[i][3]) == nerve_stat :
                matchs.append(anime_list[i][0])
        elif int(anime_list[i][2]) == mood :
            if int(anime_list[i][3]) == nerve_stat :
                matchs.append(anime_list[i][0])
            else : 
                continue
        else :
            continue
    random_num = random.randint(0,len(matchs))
    for i in range (len(anime_list)) :
        if anime_list[i][0] == matchs[random_num] :
            return i
        else :
            continue

with open('anime_list.csv',newline='') as data :
    reader = csv.reader(data)
    anime_list = list(reader)
# anime_list = [['anime_1_name','anime_1_length','anime_1_mood','anime_1_nerve_racking_level','anime_1_link'],['anime_2_name','anime_2_length','anime_2_mood','anime_2_nerve','anime_2_link']]
while(1) :
    mood =  int(input('What\'s the mood that you are looking for right now ? \n1] happy\n2] Idk\n3] sad\nplease type the number only, I\'m poorly programmed and I can\'t understand anything else. :"( \n' ))
    if mood in range(1,4,1) :
        nerve_stat = int(input('which one of these describes what you want more ?\n1) something without any stress, something relaxing to watch, something that doesn\'t have an engaging story so that if I flop it, I wouldn\'t feel bad.\n2) something with a intersting plot but yet without any tension and stress.\n3) something with a good plot and a little engaging story.\n4) something that can give me goose bumps but I wouldn\'t think about it a lot.\n5) give me something to distract my mind from my life and make it to focus on it, something that can make me cry or laugh. something that I would never forget.\nplease don\'t forget that I\'m the same poorly program as before!\n'))
        if nerve_stat in range(1,6) :
            anime_code = find_anime(mood,nerve_stat)
            print('Here you go, i found this for you, I hope that You would like this and enjoy it!')
            print('Name: ' , anime_list[anime_code][0])
            print('Episode count: ' , anime_list[anime_code][1])
            #print('Link to download: ' , anime_list[anime_code][4])
            print('Thanks for using me! <3')
        else :
            print("OK I totally get it, your brain is filled with other stuff. All you need is something relaxing, something that doesn\'t add anything to your troubles!")
            nerve_stat = 1
            anime_code = find_anime(mood,nerve_stat)
            print('Here you go, i found this for you, I hope that You would like this and enjoy it!')
            print('Name: ' , anime_list[anime_code][0])
            print('Episode count: ' , anime_list[anime_code][1])
            #print('Link to download: ' , anime_list[anime_code][4])
            print('Thanks for using me! <3')
        time.sleep(10)
    else :  print("I told you that I\'m poorly programmed, so please say something that even I understand!")    ;   time.sleep(2)   ;   pass

