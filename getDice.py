import json
import re
import os



with open("cards.json", "r") as read_file:
    data = json.load(read_file)

    for items in data:
        if items["has_die"] == True:
            tempList = []
            tempList = items["sides"]



            fname = (items["code"])
            #print (fname)


            #create create text file for dice - named after car number.
            f = open("%s.txt" % fname, "x")

            #remote first 2 chars
            first = fname[0]
            second = fname[1]
            strip_die_num = fname
            strip_die_num.replace(first,'')
            strip_die_num.replace(second,'')

            with open("beg_die.txt") as f:
                stl = (items["code"])
                with open("%s.txt" % stl, "a") as f1:
                    for line in f:
                        f1.write(line)

                    f1.write (f'DIE_NUMBER = "{strip_die_num}";\n')
                    f1.write ('FACES = [\n')

            die_side = 1

            for i in tempList:#i = 1 card with a dice - traverses all 6 die combos
                #num = int(re.search(r'\d+',i).group())
                f = open("%s.txt"%fname, "a")

                die_str = i

                


                if "-" in i:
                    f.write(f'         ["blank"]')
                    

                if "Sp" == i:
                    f.write(f'         ["special"]')


                # resource cost for die face
                if any (char.isdigit() for char in i):
                    if len(i) > 3 and i[0].isdigit():
                        first_num = i[0]
                        last_num = i[3]
                        die_str = ''.join([i for i in die_str if not i.isdigit()])

                        if "R" == die_str:#resource card
                            f.write (f'         ["resource", "{first_num}", "resource", "{last_num}"]')
                        elif "RD" == die_str:#range damage
                            f.write (f'         ["ranged", "{first_num}", "resource", "{last_num}"]')
                        elif "F" == die_str:#Focus
                            f.write (f'         ["focus", "{first_num}", "resource", "{last_num}"]')
                        elif "Dc" == die_str:#discard
                            f.write (f'         ["discard", "{first_num}", "resource", "{last_num}"]')
                        elif "MD" == die_str:#Melee
                            f.write (f'         ["melee", "{first_num}", "resource", "{last_num}"]')
                        elif "Sh" == die_str:# shield
                            f.write (f'         ["shield", "{first_num}", "resource", "{last_num}"]')
                        elif "ID" == die_str:# indirect damage
                            f.write (f'         ["indirect", "{first_num}", "resource", "{last_num}"]')
                        elif "Dr" == die_str:
                            f.write (f'         ["disrupt", "{first_num}", "resource", {last_num}"]')


                        #dies that have a +
                if i[0] == "+":
                    plus = i[0]
                    num = int(re.search(r'\d+',i).group())
                    die_str = ''.join([i for i in die_str if not i.isdigit()])
                    die_str.replace(plus,'')

                    if "R" == die_str:#resource card
                        f.write (f'         ["{plus}resource", "{num}"]')
                    elif "RD" == die_str:#range damage
                        f.write (f'         ["{plus}ranged", "{num}"]')
                    elif "F" == die_str:#Focus
                        f.write (f'         ["{plus}focus", "{num}"]')
                    elif "Dc" == die_str:#discard
                        f.write (f'         ["{plus}discard", "{num}"]')
                    elif "MD" == die_str:#Melee
                        f.write (f'         ["{plus}melee", "{num}"]')
                    elif "Sh" == die_str:# shield
                        f.write (f'         ["{plus}shield", "{num}"]')
                    elif "ID" == die_str:# indirect damage
                        f.write (f'         ["{plus}indirect", "{num}"]')
                    elif "Dr" == die_str:
                         f.write (f'         ["{plus}disrupt", "{num}"]')
                         die_count = True


        #everything else - no special results on die
                die_num = die_str[0]
                die_str = die_str.replace(i[0],'')

                if "R" == die_str:#resource card
                    f.write (f'         ["resource", "{die_num}"]')
                elif "RD" == die_str:#range damage
                    f.write (f'         ["ranged", "{die_num}"]')
                elif "F" == die_str:#Focus
                    f.write (f'         ["focus", "{die_num}"]')
                elif "Dc" == die_str:#discard
                    f.write (f'         ["discard", "{die_num}"]')
                elif "MD" == die_str:#Melee
                    f.write (f'         ["melee", "{die_num}"]')
                elif "Sh" == die_str:# shield
                    f.write (f'         ["shield", "{die_num}"]')
                elif "ID" == die_str:# indirect damage
                    f.write (f'         ["indirect", "{die_num}"]')
                elif "Dr" == die_str:
                    f.write (f'         ["disrupt", "{die_num}"]')

                #finished all possible combinations for dice side

                if die_side < 6:
                    f.write(',\n')
                else:
                    f.write("\n")
                    f.write("         ];\n")

                die_side += 1  




            with open("end_die.txt") as f:
                end_stl = items["code"]
                with open("%s.txt" % end_stl, "a") as f1:


                    for line in f:
                        f1.write(line)

                f1.close()


            f.close()

            os.rename('%s.txt' % fname,'%s.scad' % fname)













            
                    
