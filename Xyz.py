__author__ = 'anshu'

import  sys

wishes = {1:'hello', 2:'Hi', 3:"Namshkar", 4:"ola", 5:"Buna", 6:"Bonjour"}
string1 = str(wishes)
print string1


with open('resources/default.css','r') as a_file_to_read_obj:
    lines = a_file_to_read_obj.readlines()

with open('resources/copy_default.css','w') as a_file_to_write_obj:

    a_file_to_read_obj.close()

    for i in lines:
    #print i
        try:
            a_file_to_write_obj.write(i)
        except ValueError as ve:
            print 'ValueError Caught' + ve.message + str(sys.exc_info()[0])
            break
        except:
            print "Valu" +sys.exc_info()[1]


a_file_to_read_obj.close()
a_file_to_write_obj.close()
a_file_to_read_obj.close()
a_file_to_write_obj.close()