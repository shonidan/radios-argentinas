import os

#Escriba el nombre de su archivo teniendo en cuenta que cada linea debe contar con los siguientes parametros {AM or FM} [nombre radio] (URL)
radios_file = "radios.txt" 

final_list = open("final_list.txt", "a")
first_word = "#EXTM3U"


def write_first_line():
    final_list.write(first_word + "\n\n")
    final_list.close()

if first_word in open('final_list.txt').read():
    print("Word '#EXTM3U' found")
else:
    write_first_line()

with open(radios_file, "r") as radio_list:
    for line in radio_list:
        modulation = line[line.find("{")+1:line.find("}")]
        radio_name = line[line.find("[")+1:line.find("]")]
        radio_url = line[line.find("(")+1:line.find(")")]
        if radio_url and radio_name in line:
            with open("final_list.txt", 'a') as file:
                file.write("#EXTINF:0 group-title=" + modulation + "," + radio_name + "\n" + radio_url + "\n\n")

old_file_name = "final_list.txt"
new_file_name = "final_list.m3u"
os.rename(old_file_name, new_file_name)
