
import pandas as pd
import numpy as np





def display_periodic_table(element):
    print()
    print()
    print("                     --------- MODERN PERIODIC TABLE -----------             \n\n")
    print("┌────┐                                                                               ┌────┐")
    print("│ {0}  │                                                                               │ {1} │".format(element[1],element[2]))
    print("├────┼────┐                                                 ┌────┬────┬────┬────┬────┼────┤")
    print("│ {0} │ {1} │                                                 │ {2}  │ {3}  │ {4}  │ {5}  │ {6}  │ {7} │".format(element[3],element[4],element[5],element[6],element[7],element[8],element[9],element[10]))
    print("├────┼────┤                                                 ├────┼────┤────┼────┤────┼────┤")
    print("│ {0} │ {1} │                                                 │ {2} │ {3} │ {4}  │ {5}  │ {6} │ {7} │".format(element[11],element[12],element[13],element[14],element[15],element[16],element[17],element[18]))
    print("├────┼────┼────┬────┬────┬────┬────┬────┬────┬────┬────┬────┼────┼────┼────┼────┼────┼────┤")
    print("│ {0}  │ {1} │ {2} │ {3} │ {4}  │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │ {15} │ {16} │ {17} │".format(element[19],element[20],element[21],element[22],element[23],element[24],element[25],element[26],element[27],element[28],element[29],element[30],element[31],element[32],element[33],element[34],element[35],element[36]))
    print("├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤")
    print("│ {0} │ {1} │ {2}  │ {3} │ {4} │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │ {15} │ {16}  │ {17} │".format(element[37],element[38],element[39],element[40],element[41],element[42],element[43],element[44],element[45],element[46],element[47],element[48],element[49],element[50],element[51],element[52],element[53],element[54]))
    print("├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤")
    print("│ {0} │ {1} │{2}│ {3} │ {4} │ {5}  │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │ {15} │ {16} │ {17} │".format(element[55],element[56],"LaLu",element[72],element[73],element[74],element[75],element[76],element[77],element[78],element[79],element[80],element[81],element[82],element[83],element[84],element[85],element[86]))
    print("├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤")
    print("│ {0} │ {1} │{2}│ {3} │ {4} │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12}│ {13}│ {14}│ {15}│ {16}│ {17}│".format(element[87],element[88],"AcLr",element[104],element[105],element[106],element[107],element[108],element[109],element[110],element[111],element[112],element[113],element[114],element[115],element[116],element[117],element[118]))
    print("└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘")
    print()
    print("       ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐")
    print("       │ {0} │ {1} │ {2} │ {3} │ {4} │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │".format(element[57],element[58],element[59],element[60],element[61],element[62],element[63],element[64],element[65],element[66],element[67],element[68],element[69],element[70],element[71]))
    print("       ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤")
    print("       │ {0} │ {1} │ {2} │ {3}  │ {4} │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │".format(element[89],element[90],element[91],element[92],element[93],element[94],element[95],element[96],element[97],element[98],element[99],element[100],element[101],element[102],element[103]))
    print("       └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘")
    print()
    print()





data = pd.read_csv("atomic_data.csv")





data.head()





data.shape





l = data['element_symbol'].to_list()
l.insert(0, "")





display_periodic_table(l)

atom = input("Enter the Atomic Symbol : ")

indx = data.index[data['element_symbol']== atom].tolist()[0]

print("----------------------------"),
print("\tDescription")
print("----------------------------")
print("Atomic Number : ",data['atomic_number'][indx])
print("Atomic Symbol : ",data['element_symbol'][indx])
print("Element Name  : ",data['element_name'][indx])
print("Property      : ",data['property'][indx])
