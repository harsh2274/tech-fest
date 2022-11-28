import time
import random
import datetime

#lists of current working pod bays in Pune and Mumbai

lis_cur_mum = [datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), 
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), 
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), 
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), 
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0)]

lis_cur_pun = [datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), 
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), 
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), 
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), 
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0),
datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2022, 1, 1, 0, 0)]

#convoy defination
#Concoys from Mumbai
Convey = {'Convoy_1': [0, 1, 2, 3, 4, 5], 'Convoy_2': [6, 7, 8, 9, 10, 11], 'Convoy_3': [12, 13, 14, 15, 16, 17], 
'Convoy_4': [18, 19, 20, 21, 22, 23], 'Convoy_5': [24, 25, 26, 27, 28, 29], 'Convoy_6': [30, 31, 32, 33, 34, 35], 
'Convoy_7': [36, 37, 38, 39, 40, 41], 'Convoy_8': [42, 43, 44, 45, 46, 47], 'Convoy_9': [48, 49, 50, 51, 52, 53], 
'Convoy_10': [54, 55, 56, 57, 58, 59], 'Convoy_11': [60, 61, 62, 63, 64, 65], 'Convoy_12': [66, 67, 68, 69, 70, 71],
'Convoy_13': [72, 73, 74, 75, 76, 77], 'Convoy_14': [78, 79, 80, 81, 82, 83], 'Convoy_15': [84, 85, 86, 87, 88, 89],
'Convoy_16': [90, 91, 92, 93, 94, 95], 'Convoy_17': [96, 97, 98, 99, 100, 101], 'Convoy_18': [102, 103, 104, 105, 106, 107],
'Convoy_19': [108, 109, 110, 111, 112, 113], 'Convoy_20': [114, 115, 116, 117, 118, 119], 'Convoy_21': [120, 121, 122, 123, 124, 125],
'Convoy_22': [126, 127, 128, 129, 130, 131], 'Convoy_23': [132, 133, 134, 135, 136, 137], 'Convoy_24': [138, 139, 140, 141, 142, 143],
'Convoy_25': [144, 145, 146, 147, 148, 149], 'Convoy_26': [150, 151, 152, 153, 154, 155], 'Convoy_27': [156, 157, 158, 159, 160, 161],
'Convoy_28': [162, 163, 164, 165, 166, 167], 'Convoy_29': [168, 169, 170, 171, 172, 173], 'Convoy_30': [174, 175, 176, 177, 178, 179],
'Convoy_31': [180, 181, 182, 183, 184, 185], 'Convoy_32': [186, 187, 188, 189, 190, 191], 'Convoy_33': [192, 193, 194, 195, 196, 197], 
'Convoy_34': [198, 199, 200, 201, 202, 203], 'Convoy_35': [204, 205, 206, 207, 208, 209], 'Convoy_36': [210, 211, 212, 213, 214, 215],
'Convoy_37': [216, 217, 218, 219, 220, 221], 'Convoy_38': [222, 223, 224, 225, 226, 227], 'Convoy_39': [228, 229, 230, 231, 232, 233],
'Convoy_40': [234, 235, 236, 237, 238, 239], 'Convoy_41': [240, 241, 242, 243, 244, 245], 'Convoy_42': [246, 247, 248, 249, 250, 251],
'Convoy_43': [252, 253, 254, 255, 256, 257], 'Convoy_44': [258, 259, 260, 261, 262, 263], 'Convoy_45': [264, 265, 266, 267, 268, 269],
'Convoy_46': [270, 271, 272, 273, 274, 275], 'Convoy_47': [276, 277, 278, 279, 280, 281], 'Convoy_48': [282, 283, 284, 285, 286, 287],
'Convoy_49': [288, 289, 290, 291, 292, 293], 'Convoy_50': [294, 295, 296, 297, 298, 299], 'Convoy_51': [300, 301, 302, 303, 304, 305],
'Convoy_52': [306, 307, 308, 309, 310, 311], 'Convoy_53': [312, 313, 314, 315, 316, 317], 'Convoy_54': [318, 319, 320, 321, 322, 323],
'Convoy_55': [324, 325, 326, 327, 328, 329], 'Convoy_56': [330, 331, 332, 333, 334, 335], 'Convoy_57': [336, 337, 338, 339, 340, 341],
'Convoy_58': [342, 343, 344, 345, 346, 347], 'Convoy_59': [348, 349, 350, 351, 352, 353], 'Convoy_60': [354, 355, 356, 357, 358, 359],
'Convoy_61': [360, 361, 362, 363, 364, 365], 'Convoy_62': [366, 367, 368, 369, 370, 371], 'Convoy_63': [372, 373, 374, 375, 376, 377],
'Convoy_64': [378, 379, 380, 381, 382, 383], 'Convoy_65': [384, 385, 386, 387, 388, 389], 'Convoy_66': [390, 391, 392, 393, 394, 395],
'Convoy_67': [396, 397, 398, 399, 400, 401], 'Convoy_68': [402, 403, 404, 405, 406, 407], 'Convoy_69': [408, 409, 410, 411, 412, 413],
'Convoy_70': [414, 415, 416, 417, 418, 419], 'Convoy_71': [420, 421, 422, 423, 424, 425], 'Convoy_72': [426, 427, 428, 429, 430, 431], 
'Convoy_73': [432, 433, 434, 435, 436, 437], 'Convoy_74': [438, 439, 440, 441, 442, 443], 'Convoy_75': [444, 445, 446, 447, 448, 449], 
'Convoy_76': [450, 451, 452, 453, 454, 455], 'Convoy_77': [456, 457, 458, 459, 460, 461], 'Convoy_78': [462, 463, 464, 465, 466, 467], 
'Convoy_79': [468, 469, 470, 471, 472, 473], 'Convoy_80': [474, 475, 476, 477, 478, 479], 'Convoy_81': [480, 481, 482, 483, 484, 485],
'Convoy_82': [486, 487, 488, 489, 490, 491], 'Convoy_83': [492, 493, 494, 495, 496, 497], 'Convoy_84': [498, 499, 500, 501, 502, 503],       
'Convoy_85': [504, 505, 506, 507, 508, 509], 'Convoy_86': [510, 511, 512, 513, 514, 515], 'Convoy_87': [516, 517, 518, 519, 520, 521],
'Convoy_88': [522, 523, 524, 525, 526, 527], 'Convoy_89': [528, 529, 530, 531, 532, 533], 'Convoy_90': [534, 535, 536, 537, 538, 539],
'Convoy_91': [540, 541, 542, 543, 544, 545], 'Convoy_92': [546, 547, 548, 549, 550, 551], 'Convoy_93': [552, 553, 554, 555, 556, 557],
'Convoy_94': [558, 559, 560, 561, 562, 563], 'Convoy_95': [564, 565, 566, 567, 568, 569], 'Convoy_96': [570, 571, 572, 573, 574, 575],
'Convoy_97': [576, 577, 578, 579, 580, 581], 'Convoy_98': [582, 583, 584, 585, 586, 587], 'Convoy_99': [588, 589, 590, 591, 592, 593],
'Convoy_100': [594, 595, 596, 597, 598, 599], 'Convoy_101': [600, 601, 602, 603, 604, 605], 'Convoy_102': [606, 607, 608, 609, 610, 611],
'Convoy_103': [612, 613, 614, 615, 616, 617], 'Convoy_104': [618, 619, 620, 621, 622, 623], 'Convoy_105': [624, 625, 626, 627, 628, 629],
'Convoy_106': [630, 631, 632, 633, 634, 635], 'Convoy_107': [636, 637, 638, 639, 640, 641], 'Convoy_108': [642, 643, 644, 645, 646, 647],
'Convoy_109': [648, 649, 650, 651, 652, 653], 'Convoy_110': [654, 655, 656, 657, 658, 659], 'Convoy_111': [660, 661, 662, 663, 664, 665],
'Convoy_112': [666, 667, 668, 669, 670, 671], 'Convoy_113': [672, 673, 674, 675, 676, 677], 'Convoy_114': [678, 679, 680, 681, 682, 683],
'Convoy_115': [684, 685, 686, 687, 688, 689], 'Convoy_116': [690, 691, 692, 693, 694, 695], 'Convoy_117': [696, 697, 698, 699, 700, 701],
'Convoy_118': [702, 703, 704, 705, 706, 707], 'Convoy_119': [708, 709, 710, 711, 712, 713], 'Convoy_120': [714, 715, 716, 717, 718, 719],
'Convoy_121': [720, 721, 722, 723, 724, 725], 'Convoy_122': [726, 727, 728, 729, 730, 731], 'Convoy_123': [732, 733, 734, 735, 736, 737],
'Convoy_124': [738, 739, 740, 741, 742, 743], 'Convoy_125': [744, 745, 746, 747, 748, 749], 'Convoy_126': [750, 751, 752, 753, 754, 755],
'Convoy_127': [756, 757, 758, 759, 760, 761], 'Convoy_128': [762, 763, 764, 765, 766, 767], 'Convoy_129': [768, 769, 770, 771, 772, 773],
'Convoy_130': [774, 775, 776, 777, 778, 779], 'Convoy_131': [780, 781, 782, 783, 784, 785], 'Convoy_132': [786, 787, 788, 789, 790, 791],
'Convoy_133': [792, 793, 794, 795, 796, 797], 'Convoy_134': [798, 799, 800, 801, 802, 803], 'Convoy_135': [804, 805, 806, 807, 808, 809],
'Convoy_136': [810, 811, 812, 813, 814, 815], 'Convoy_137': [816, 817, 818, 819, 820, 821], 'Convoy_138': [822, 823, 824, 825, 826, 827],
'Convoy_139': [828, 829, 830, 831, 832, 833], 'Convoy_140': [834, 835, 836, 837, 838, 839], 'Convoy_141': [840, 841, 842, 843, 844, 845],
'Convoy_142': [846, 847, 848, 849, 850, 851], 'Convoy_143': [852, 853, 854, 855, 856, 857], 'Convoy_144': [858, 859, 860, 861, 862, 863]}


#Convoy = {"md":datetime.datetime(2022,1,1,0,0,0),"pa":datetime.datetime(2022,1,1,0,0,0),"pd":datetime.datetime(2022,1,1,0,0,0),"ma":datetime.datetime(2022,1,1,0,0,0)}
Convoy_1 =  {'md': datetime.datetime(2022, 1, 1, 0, 0), 'pa': datetime.datetime(2022, 1, 1, 0, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 36), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_1'}
Convoy_2 =  {'md': datetime.datetime(2022, 1, 1, 0, 0, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 30, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 36, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_2'}
Convoy_3 =  {'md': datetime.datetime(2022, 1, 1, 0, 1), 'pa': datetime.datetime(2022, 1, 1, 0, 31), 'pd': datetime.datetime(2022, 1, 1, 0, 37), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_3'}
Convoy_4 =  {'md': datetime.datetime(2022, 1, 1, 0, 1, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 31, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 37, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_4'}
Convoy_5 =  {'md': datetime.datetime(2022, 1, 1, 0, 2), 'pa': datetime.datetime(2022, 1, 1, 0, 32), 'pd': datetime.datetime(2022, 1, 1, 0, 38), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_5'}
Convoy_6 =  {'md': datetime.datetime(2022, 1, 1, 0, 2, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 32, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 38, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_6'}
Convoy_7 =  {'md': datetime.datetime(2022, 1, 1, 0, 3), 'pa': datetime.datetime(2022, 1, 1, 0, 33), 'pd': datetime.datetime(2022, 1, 1, 0, 39), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_7'}
Convoy_8 =  {'md': datetime.datetime(2022, 1, 1, 0, 3, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 33, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 39, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_8'}
Convoy_9 =  {'md': datetime.datetime(2022, 1, 1, 0, 4), 'pa': datetime.datetime(2022, 1, 1, 0, 34), 'pd': datetime.datetime(2022, 1, 1, 0, 40), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_9'}
Convoy_10 =  {'md': datetime.datetime(2022, 1, 1, 0, 4, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 34, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 40, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_10'}
Convoy_11 =  {'md': datetime.datetime(2022, 1, 1, 0, 5), 'pa': datetime.datetime(2022, 1, 1, 0, 35), 'pd': datetime.datetime(2022, 1, 1, 0, 41), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_11'}
Convoy_12 =  {'md': datetime.datetime(2022, 1, 1, 0, 5, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 35, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 41, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_12'}
Convoy_13 =  {'md': datetime.datetime(2022, 1, 1, 0, 6), 'pa': datetime.datetime(2022, 1, 1, 0, 36), 'pd': datetime.datetime(2022, 1, 1, 0, 42), 'ma': datetime.datetime(2022, 1, 1, 0, 0), 'name': 'Convoy_13'}
Convoy_14 =  {'md': datetime.datetime(2022, 1, 1, 0, 6, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 36, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 42, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 0, 30), 'name': 'Convoy_14'}
Convoy_15 =  {'md': datetime.datetime(2022, 1, 1, 0, 7), 'pa': datetime.datetime(2022, 1, 1, 0, 37), 'pd': datetime.datetime(2022, 1, 1, 0, 43), 'ma': datetime.datetime(2022, 1, 1, 0, 1), 'name': 'Convoy_15'}
Convoy_16 =  {'md': datetime.datetime(2022, 1, 1, 0, 7, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 37, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 43, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 1, 30), 'name': 'Convoy_16'}
Convoy_17 =  {'md': datetime.datetime(2022, 1, 1, 0, 8), 'pa': datetime.datetime(2022, 1, 1, 0, 38), 'pd': datetime.datetime(2022, 1, 1, 0, 44), 'ma': datetime.datetime(2022, 1, 1, 0, 2), 'name': 'Convoy_17'}
Convoy_18 =  {'md': datetime.datetime(2022, 1, 1, 0, 8, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 38, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 44, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 2, 30), 'name': 'Convoy_18'}
Convoy_19 =  {'md': datetime.datetime(2022, 1, 1, 0, 9), 'pa': datetime.datetime(2022, 1, 1, 0, 39), 'pd': datetime.datetime(2022, 1, 1, 0, 45), 'ma': datetime.datetime(2022, 1, 1, 0, 3), 'name': 'Convoy_19'}
Convoy_20 =  {'md': datetime.datetime(2022, 1, 1, 0, 9, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 39, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 45, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 3, 30), 'name': 'Convoy_20'}
Convoy_21 =  {'md': datetime.datetime(2022, 1, 1, 0, 10), 'pa': datetime.datetime(2022, 1, 1, 0, 40), 'pd': datetime.datetime(2022, 1, 1, 0, 46), 'ma': datetime.datetime(2022, 1, 1, 0, 4), 'name': 'Convoy_21'}
Convoy_22 =  {'md': datetime.datetime(2022, 1, 1, 0, 10, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 40, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 46, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 4, 30), 'name': 'Convoy_22'}
Convoy_23 =  {'md': datetime.datetime(2022, 1, 1, 0, 11), 'pa': datetime.datetime(2022, 1, 1, 0, 41), 'pd': datetime.datetime(2022, 1, 1, 0, 47), 'ma': datetime.datetime(2022, 1, 1, 0, 5), 'name': 'Convoy_23'}
Convoy_24 =  {'md': datetime.datetime(2022, 1, 1, 0, 11, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 41, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 47, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 5, 30), 'name': 'Convoy_24'}
Convoy_25 =  {'md': datetime.datetime(2022, 1, 1, 0, 12), 'pa': datetime.datetime(2022, 1, 1, 0, 42), 'pd': datetime.datetime(2022, 1, 1, 0, 48), 'ma': datetime.datetime(2022, 1, 1, 0, 6), 'name': 'Convoy_25'}
Convoy_26 =  {'md': datetime.datetime(2022, 1, 1, 0, 12, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 42, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 48, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 6, 30), 'name': 'Convoy_26'}
Convoy_27 =  {'md': datetime.datetime(2022, 1, 1, 0, 13), 'pa': datetime.datetime(2022, 1, 1, 0, 43), 'pd': datetime.datetime(2022, 1, 1, 0, 49), 'ma': datetime.datetime(2022, 1, 1, 0, 7), 'name': 'Convoy_27'}
Convoy_28 =  {'md': datetime.datetime(2022, 1, 1, 0, 13, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 43, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 49, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 7, 30), 'name': 'Convoy_28'}
Convoy_29 =  {'md': datetime.datetime(2022, 1, 1, 0, 14), 'pa': datetime.datetime(2022, 1, 1, 0, 44), 'pd': datetime.datetime(2022, 1, 1, 0, 50), 'ma': datetime.datetime(2022, 1, 1, 0, 8), 'name': 'Convoy_29'}
Convoy_30 =  {'md': datetime.datetime(2022, 1, 1, 0, 14, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 44, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 50, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 8, 30), 'name': 'Convoy_30'}
Convoy_31 =  {'md': datetime.datetime(2022, 1, 1, 0, 15), 'pa': datetime.datetime(2022, 1, 1, 0, 45), 'pd': datetime.datetime(2022, 1, 1, 0, 51), 'ma': datetime.datetime(2022, 1, 1, 0, 9), 'name': 'Convoy_31'}
Convoy_32 =  {'md': datetime.datetime(2022, 1, 1, 0, 15, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 45, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 51, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 9, 30), 'name': 'Convoy_32'}
Convoy_33 =  {'md': datetime.datetime(2022, 1, 1, 0, 16), 'pa': datetime.datetime(2022, 1, 1, 0, 46), 'pd': datetime.datetime(2022, 1, 1, 0, 52), 'ma': datetime.datetime(2022, 1, 1, 0, 10), 'name': 'Convoy_33'}
Convoy_34 =  {'md': datetime.datetime(2022, 1, 1, 0, 16, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 46, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 52, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 10, 30), 'name': 'Convoy_34'}
Convoy_35 =  {'md': datetime.datetime(2022, 1, 1, 0, 17), 'pa': datetime.datetime(2022, 1, 1, 0, 47), 'pd': datetime.datetime(2022, 1, 1, 0, 53), 'ma': datetime.datetime(2022, 1, 1, 0, 11), 'name': 'Convoy_35'}
Convoy_36 =  {'md': datetime.datetime(2022, 1, 1, 0, 17, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 47, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 53, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 11, 30), 'name': 'Convoy_36'}
Convoy_37 =  {'md': datetime.datetime(2022, 1, 1, 0, 18), 'pa': datetime.datetime(2022, 1, 1, 0, 48), 'pd': datetime.datetime(2022, 1, 1, 0, 54), 'ma': datetime.datetime(2022, 1, 1, 0, 12), 'name': 'Convoy_37'}
Convoy_38 =  {'md': datetime.datetime(2022, 1, 1, 0, 18, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 48, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 54, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 12, 30), 'name': 'Convoy_38'}
Convoy_39 =  {'md': datetime.datetime(2022, 1, 1, 0, 19), 'pa': datetime.datetime(2022, 1, 1, 0, 49), 'pd': datetime.datetime(2022, 1, 1, 0, 55), 'ma': datetime.datetime(2022, 1, 1, 0, 13), 'name': 'Convoy_39'}
Convoy_40 =  {'md': datetime.datetime(2022, 1, 1, 0, 19, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 49, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 55, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 13, 30), 'name': 'Convoy_40'}
Convoy_41 =  {'md': datetime.datetime(2022, 1, 1, 0, 20), 'pa': datetime.datetime(2022, 1, 1, 0, 50), 'pd': datetime.datetime(2022, 1, 1, 0, 56), 'ma': datetime.datetime(2022, 1, 1, 0, 14), 'name': 'Convoy_41'}
Convoy_42 =  {'md': datetime.datetime(2022, 1, 1, 0, 20, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 50, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 56, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 14, 30), 'name': 'Convoy_42'}
Convoy_43 =  {'md': datetime.datetime(2022, 1, 1, 0, 21), 'pa': datetime.datetime(2022, 1, 1, 0, 51), 'pd': datetime.datetime(2022, 1, 1, 0, 57), 'ma': datetime.datetime(2022, 1, 1, 0, 15), 'name': 'Convoy_43'}
Convoy_44 =  {'md': datetime.datetime(2022, 1, 1, 0, 21, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 51, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 57, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 15, 30), 'name': 'Convoy_44'}
Convoy_45 =  {'md': datetime.datetime(2022, 1, 1, 0, 22), 'pa': datetime.datetime(2022, 1, 1, 0, 52), 'pd': datetime.datetime(2022, 1, 1, 0, 58), 'ma': datetime.datetime(2022, 1, 1, 0, 16), 'name': 'Convoy_45'}
Convoy_46 =  {'md': datetime.datetime(2022, 1, 1, 0, 22, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 52, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 58, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 16, 30), 'name': 'Convoy_46'}
Convoy_47 =  {'md': datetime.datetime(2022, 1, 1, 0, 23), 'pa': datetime.datetime(2022, 1, 1, 0, 53), 'pd': datetime.datetime(2022, 1, 1, 0, 59), 'ma': datetime.datetime(2022, 1, 1, 0, 17), 'name': 'Convoy_47'}
Convoy_48 =  {'md': datetime.datetime(2022, 1, 1, 0, 23, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 53, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 59, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 17, 30), 'name': 'Convoy_48'}
Convoy_49 =  {'md': datetime.datetime(2022, 1, 1, 0, 24), 'pa': datetime.datetime(2022, 1, 1, 0, 54), 'pd': datetime.datetime(2022, 1, 1, 1, 0), 'ma': datetime.datetime(2022, 1, 1, 0, 18), 'name': 'Convoy_49'}
Convoy_50 =  {'md': datetime.datetime(2022, 1, 1, 0, 24, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 54, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 0, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 18, 30), 'name': 'Convoy_50'}
Convoy_51 =  {'md': datetime.datetime(2022, 1, 1, 0, 25), 'pa': datetime.datetime(2022, 1, 1, 0, 55), 'pd': datetime.datetime(2022, 1, 1, 1, 1), 'ma': datetime.datetime(2022, 1, 1, 0, 19), 'name': 'Convoy_51'}
Convoy_52 =  {'md': datetime.datetime(2022, 1, 1, 0, 25, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 55, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 1, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 19, 30), 'name': 'Convoy_52'}
Convoy_53 =  {'md': datetime.datetime(2022, 1, 1, 0, 26), 'pa': datetime.datetime(2022, 1, 1, 0, 56), 'pd': datetime.datetime(2022, 1, 1, 1, 2), 'ma': datetime.datetime(2022, 1, 1, 0, 20), 'name': 'Convoy_53'}
Convoy_54 =  {'md': datetime.datetime(2022, 1, 1, 0, 26, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 56, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 2, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 20, 30), 'name': 'Convoy_54'}
Convoy_55 =  {'md': datetime.datetime(2022, 1, 1, 0, 27), 'pa': datetime.datetime(2022, 1, 1, 0, 57), 'pd': datetime.datetime(2022, 1, 1, 1, 3), 'ma': datetime.datetime(2022, 1, 1, 0, 21), 'name': 'Convoy_55'}
Convoy_56 =  {'md': datetime.datetime(2022, 1, 1, 0, 27, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 57, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 3, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 21, 30), 'name': 'Convoy_56'}
Convoy_57 =  {'md': datetime.datetime(2022, 1, 1, 0, 28), 'pa': datetime.datetime(2022, 1, 1, 0, 58), 'pd': datetime.datetime(2022, 1, 1, 1, 4), 'ma': datetime.datetime(2022, 1, 1, 0, 22), 'name': 'Convoy_57'}
Convoy_58 =  {'md': datetime.datetime(2022, 1, 1, 0, 28, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 58, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 4, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 22, 30), 'name': 'Convoy_58'}
Convoy_59 =  {'md': datetime.datetime(2022, 1, 1, 0, 29), 'pa': datetime.datetime(2022, 1, 1, 0, 59), 'pd': datetime.datetime(2022, 1, 1, 1, 5), 'ma': datetime.datetime(2022, 1, 1, 0, 23), 'name': 'Convoy_59'}
Convoy_60 =  {'md': datetime.datetime(2022, 1, 1, 0, 29, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 59, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 5, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 23, 30), 'name': 'Convoy_60'}
Convoy_61 =  {'md': datetime.datetime(2022, 1, 1, 0, 30), 'pa': datetime.datetime(2022, 1, 1, 1, 0), 'pd': datetime.datetime(2022, 1, 1, 1, 6), 'ma': datetime.datetime(2022, 1, 1, 0, 24), 'name': 'Convoy_61'}
Convoy_62 =  {'md': datetime.datetime(2022, 1, 1, 0, 30, 30), 'pa': datetime.datetime(2022, 1, 1, 1, 0, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 6, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 24, 30), 'name': 'Convoy_62'}
Convoy_63 =  {'md': datetime.datetime(2022, 1, 1, 0, 31), 'pa': datetime.datetime(2022, 1, 1, 1, 1), 'pd': datetime.datetime(2022, 1, 1, 1, 7), 'ma': datetime.datetime(2022, 1, 1, 0, 25), 'name': 'Convoy_63'}
Convoy_64 =  {'md': datetime.datetime(2022, 1, 1, 0, 31, 30), 'pa': datetime.datetime(2022, 1, 1, 1, 1, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 7, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 25, 30), 'name': 'Convoy_64'}
Convoy_65 =  {'md': datetime.datetime(2022, 1, 1, 0, 32), 'pa': datetime.datetime(2022, 1, 1, 1, 2), 'pd': datetime.datetime(2022, 1, 1, 1, 8), 'ma': datetime.datetime(2022, 1, 1, 0, 26), 'name': 'Convoy_65'}
Convoy_66 =  {'md': datetime.datetime(2022, 1, 1, 0, 32, 30), 'pa': datetime.datetime(2022, 1, 1, 1, 2, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 8, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 26, 30), 'name': 'Convoy_66'}
Convoy_67 =  {'md': datetime.datetime(2022, 1, 1, 0, 33), 'pa': datetime.datetime(2022, 1, 1, 1, 3), 'pd': datetime.datetime(2022, 1, 1, 1, 9), 'ma': datetime.datetime(2022, 1, 1, 0, 27), 'name': 'Convoy_67'}
Convoy_68 =  {'md': datetime.datetime(2022, 1, 1, 0, 33, 30), 'pa': datetime.datetime(2022, 1, 1, 1, 3, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 9, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 27, 30), 'name': 'Convoy_68'}
Convoy_69 =  {'md': datetime.datetime(2022, 1, 1, 0, 34), 'pa': datetime.datetime(2022, 1, 1, 1, 4), 'pd': datetime.datetime(2022, 1, 1, 1, 10), 'ma': datetime.datetime(2022, 1, 1, 0, 28), 'name': 'Convoy_69'}
Convoy_70 =  {'md': datetime.datetime(2022, 1, 1, 0, 34, 30), 'pa': datetime.datetime(2022, 1, 1, 1, 4, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 10, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 28, 30), 'name': 'Convoy_70'}
Convoy_71 =  {'md': datetime.datetime(2022, 1, 1, 0, 35), 'pa': datetime.datetime(2022, 1, 1, 1, 5), 'pd': datetime.datetime(2022, 1, 1, 1, 11), 'ma': datetime.datetime(2022, 1, 1, 0, 29), 'name': 'Convoy_71'}
Convoy_72 =  {'md': datetime.datetime(2022, 1, 1, 0, 35, 30), 'pa': datetime.datetime(2022, 1, 1, 1, 5, 30), 'pd': datetime.datetime(2022, 1, 1, 1, 11, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 29, 30), 'name': 'Convoy_72'}


Convoy_73 =  {'md': datetime.datetime(2022, 1, 1, 0, 36), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 0), 'ma': datetime.datetime(2022, 1, 1, 0, 30), 'name': 'Convoy_73'}
Convoy_74 =  {'md': datetime.datetime(2022, 1, 1, 0, 36, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 0, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 30, 30), 'name': 'Convoy_74'}
Convoy_75 =  {'md': datetime.datetime(2022, 1, 1, 0, 37), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 1), 'ma': datetime.datetime(2022, 1, 1, 0, 31), 'name': 'Convoy_75'}
Convoy_76 =  {'md': datetime.datetime(2022, 1, 1, 0, 37, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 1, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 31, 30), 'name': 'Convoy_76'}
Convoy_77 =  {'md': datetime.datetime(2022, 1, 1, 0, 38), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 2), 'ma': datetime.datetime(2022, 1, 1, 0, 32), 'name': 'Convoy_77'}
Convoy_78 =  {'md': datetime.datetime(2022, 1, 1, 0, 38, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 2, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 32, 30), 'name': 'Convoy_78'}
Convoy_79 =  {'md': datetime.datetime(2022, 1, 1, 0, 39), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 3), 'ma': datetime.datetime(2022, 1, 1, 0, 33), 'name': 'Convoy_79'}
Convoy_80 =  {'md': datetime.datetime(2022, 1, 1, 0, 39, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 3, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 33, 30), 'name': 'Convoy_80'}
Convoy_81 =  {'md': datetime.datetime(2022, 1, 1, 0, 40), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 4), 'ma': datetime.datetime(2022, 1, 1, 0, 34), 'name': 'Convoy_81'}
Convoy_82 =  {'md': datetime.datetime(2022, 1, 1, 0, 40, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 4, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 34, 30), 'name': 'Convoy_82'}
Convoy_83 =  {'md': datetime.datetime(2022, 1, 1, 0, 41), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 5), 'ma': datetime.datetime(2022, 1, 1, 0, 35), 'name': 'Convoy_83'}
Convoy_84 =  {'md': datetime.datetime(2022, 1, 1, 0, 41, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 5, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 35, 30), 'name': 'Convoy_84'}
Convoy_85 =  {'md': datetime.datetime(2022, 1, 1, 0, 42), 'pa': datetime.datetime(2022, 1, 1, 0, 0), 'pd': datetime.datetime(2022, 1, 1, 0, 6), 'ma': datetime.datetime(2022, 1, 1, 0, 36), 'name': 'Convoy_85'}
Convoy_86 =  {'md': datetime.datetime(2022, 1, 1, 0, 42, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 0, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 6, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 36, 30), 'name': 'Convoy_86'}
Convoy_87 =  {'md': datetime.datetime(2022, 1, 1, 0, 43), 'pa': datetime.datetime(2022, 1, 1, 0, 1), 'pd': datetime.datetime(2022, 1, 1, 0, 7), 'ma': datetime.datetime(2022, 1, 1, 0, 37), 'name': 'Convoy_87'}
Convoy_88 =  {'md': datetime.datetime(2022, 1, 1, 0, 43, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 1, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 7, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 37, 30), 'name': 'Convoy_88'}
Convoy_89 =  {'md': datetime.datetime(2022, 1, 1, 0, 44), 'pa': datetime.datetime(2022, 1, 1, 0, 2), 'pd': datetime.datetime(2022, 1, 1, 0, 8), 'ma': datetime.datetime(2022, 1, 1, 0, 38), 'name': 'Convoy_89'}
Convoy_90 =  {'md': datetime.datetime(2022, 1, 1, 0, 44, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 2, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 8, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 38, 30), 'name': 'Convoy_90'}
Convoy_91 =  {'md': datetime.datetime(2022, 1, 1, 0, 45), 'pa': datetime.datetime(2022, 1, 1, 0, 3), 'pd': datetime.datetime(2022, 1, 1, 0, 9), 'ma': datetime.datetime(2022, 1, 1, 0, 39), 'name': 'Convoy_91'}
Convoy_92 =  {'md': datetime.datetime(2022, 1, 1, 0, 45, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 3, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 9, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 39, 30), 'name': 'Convoy_92'}
Convoy_93 =  {'md': datetime.datetime(2022, 1, 1, 0, 46), 'pa': datetime.datetime(2022, 1, 1, 0, 4), 'pd': datetime.datetime(2022, 1, 1, 0, 10), 'ma': datetime.datetime(2022, 1, 1, 0, 40), 'name': 'Convoy_93'}
Convoy_94 =  {'md': datetime.datetime(2022, 1, 1, 0, 46, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 4, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 10, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 40, 30), 'name': 'Convoy_94'}
Convoy_95 =  {'md': datetime.datetime(2022, 1, 1, 0, 47), 'pa': datetime.datetime(2022, 1, 1, 0, 5), 'pd': datetime.datetime(2022, 1, 1, 0, 11), 'ma': datetime.datetime(2022, 1, 1, 0, 41), 'name': 'Convoy_95'}
Convoy_96 =  {'md': datetime.datetime(2022, 1, 1, 0, 47, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 5, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 11, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 41, 30), 'name': 'Convoy_96'}
Convoy_97 =  {'md': datetime.datetime(2022, 1, 1, 0, 48), 'pa': datetime.datetime(2022, 1, 1, 0, 6), 'pd': datetime.datetime(2022, 1, 1, 0, 12), 'ma': datetime.datetime(2022, 1, 1, 0, 42), 'name': 'Convoy_97'}
Convoy_98 =  {'md': datetime.datetime(2022, 1, 1, 0, 48, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 6, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 12, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 42, 30), 'name': 'Convoy_98'}
Convoy_99 =  {'md': datetime.datetime(2022, 1, 1, 0, 49), 'pa': datetime.datetime(2022, 1, 1, 0, 7), 'pd': datetime.datetime(2022, 1, 1, 0, 13), 'ma': datetime.datetime(2022, 1, 1, 0, 43), 'name': 'Convoy_99'}
Convoy_100 =  {'md': datetime.datetime(2022, 1, 1, 0, 49, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 7, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 13, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 43, 30), 'name': 'Convoy_100'}
Convoy_101 =  {'md': datetime.datetime(2022, 1, 1, 0, 50), 'pa': datetime.datetime(2022, 1, 1, 0, 8), 'pd': datetime.datetime(2022, 1, 1, 0, 14), 'ma': datetime.datetime(2022, 1, 1, 0, 44), 'name': 'Convoy_101'}
Convoy_102 =  {'md': datetime.datetime(2022, 1, 1, 0, 50, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 8, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 14, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 44, 30), 'name': 'Convoy_102'}
Convoy_103 =  {'md': datetime.datetime(2022, 1, 1, 0, 51), 'pa': datetime.datetime(2022, 1, 1, 0, 9), 'pd': datetime.datetime(2022, 1, 1, 0, 15), 'ma': datetime.datetime(2022, 1, 1, 0, 45), 'name': 'Convoy_103'}
Convoy_104 =  {'md': datetime.datetime(2022, 1, 1, 0, 51, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 9, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 15, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 45, 30), 'name': 'Convoy_104'}
Convoy_105 =  {'md': datetime.datetime(2022, 1, 1, 0, 52), 'pa': datetime.datetime(2022, 1, 1, 0, 10), 'pd': datetime.datetime(2022, 1, 1, 0, 16), 'ma': datetime.datetime(2022, 1, 1, 0, 46), 'name': 'Convoy_105'}
Convoy_106 =  {'md': datetime.datetime(2022, 1, 1, 0, 52, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 10, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 16, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 46, 30), 'name': 'Convoy_106'}
Convoy_107 =  {'md': datetime.datetime(2022, 1, 1, 0, 53), 'pa': datetime.datetime(2022, 1, 1, 0, 11), 'pd': datetime.datetime(2022, 1, 1, 0, 17), 'ma': datetime.datetime(2022, 1, 1, 0, 47), 'name': 'Convoy_107'}
Convoy_108 =  {'md': datetime.datetime(2022, 1, 1, 0, 53, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 11, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 17, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 47, 30), 'name': 'Convoy_108'}
Convoy_109 =  {'md': datetime.datetime(2022, 1, 1, 0, 54), 'pa': datetime.datetime(2022, 1, 1, 0, 12), 'pd': datetime.datetime(2022, 1, 1, 0, 18), 'ma': datetime.datetime(2022, 1, 1, 0, 48), 'name': 'Convoy_109'}
Convoy_110 =  {'md': datetime.datetime(2022, 1, 1, 0, 54, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 12, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 18, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 48, 30), 'name': 'Convoy_110'}
Convoy_111 =  {'md': datetime.datetime(2022, 1, 1, 0, 55), 'pa': datetime.datetime(2022, 1, 1, 0, 13), 'pd': datetime.datetime(2022, 1, 1, 0, 19), 'ma': datetime.datetime(2022, 1, 1, 0, 49), 'name': 'Convoy_111'}
Convoy_112 =  {'md': datetime.datetime(2022, 1, 1, 0, 55, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 13, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 19, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 49, 30), 'name': 'Convoy_112'}
Convoy_113 =  {'md': datetime.datetime(2022, 1, 1, 0, 56), 'pa': datetime.datetime(2022, 1, 1, 0, 14), 'pd': datetime.datetime(2022, 1, 1, 0, 20), 'ma': datetime.datetime(2022, 1, 1, 0, 50), 'name': 'Convoy_113'}
Convoy_114 =  {'md': datetime.datetime(2022, 1, 1, 0, 56, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 14, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 20, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 50, 30), 'name': 'Convoy_114'}
Convoy_115 =  {'md': datetime.datetime(2022, 1, 1, 0, 57), 'pa': datetime.datetime(2022, 1, 1, 0, 15), 'pd': datetime.datetime(2022, 1, 1, 0, 21), 'ma': datetime.datetime(2022, 1, 1, 0, 51), 'name': 'Convoy_115'}
Convoy_116 =  {'md': datetime.datetime(2022, 1, 1, 0, 57, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 15, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 21, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 51, 30), 'name': 'Convoy_116'}
Convoy_117 =  {'md': datetime.datetime(2022, 1, 1, 0, 58), 'pa': datetime.datetime(2022, 1, 1, 0, 16), 'pd': datetime.datetime(2022, 1, 1, 0, 22), 'ma': datetime.datetime(2022, 1, 1, 0, 52), 'name': 'Convoy_117'}
Convoy_118 =  {'md': datetime.datetime(2022, 1, 1, 0, 58, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 16, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 22, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 52, 30), 'name': 'Convoy_118'}
Convoy_119 =  {'md': datetime.datetime(2022, 1, 1, 0, 59), 'pa': datetime.datetime(2022, 1, 1, 0, 17), 'pd': datetime.datetime(2022, 1, 1, 0, 23), 'ma': datetime.datetime(2022, 1, 1, 0, 53), 'name': 'Convoy_119'}
Convoy_120 =  {'md': datetime.datetime(2022, 1, 1, 0, 59, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 17, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 23, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 53, 30), 'name': 'Convoy_120'}
Convoy_121 =  {'md': datetime.datetime(2022, 1, 1, 1, 0), 'pa': datetime.datetime(2022, 1, 1, 0, 18), 'pd': datetime.datetime(2022, 1, 1, 0, 24), 'ma': datetime.datetime(2022, 1, 1, 0, 54), 'name': 'Convoy_121'}
Convoy_122 =  {'md': datetime.datetime(2022, 1, 1, 1, 0, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 18, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 24, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 54, 30), 'name': 'Convoy_122'}
Convoy_123 =  {'md': datetime.datetime(2022, 1, 1, 1, 1), 'pa': datetime.datetime(2022, 1, 1, 0, 19), 'pd': datetime.datetime(2022, 1, 1, 0, 25), 'ma': datetime.datetime(2022, 1, 1, 0, 55), 'name': 'Convoy_123'}
Convoy_124 =  {'md': datetime.datetime(2022, 1, 1, 1, 1, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 19, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 25, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 55, 30), 'name': 'Convoy_124'}
Convoy_125 =  {'md': datetime.datetime(2022, 1, 1, 1, 2), 'pa': datetime.datetime(2022, 1, 1, 0, 20), 'pd': datetime.datetime(2022, 1, 1, 0, 26), 'ma': datetime.datetime(2022, 1, 1, 0, 56), 'name': 'Convoy_125'}
Convoy_126 =  {'md': datetime.datetime(2022, 1, 1, 1, 2, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 20, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 26, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 56, 30), 'name': 'Convoy_126'}
Convoy_127 =  {'md': datetime.datetime(2022, 1, 1, 1, 3), 'pa': datetime.datetime(2022, 1, 1, 0, 21), 'pd': datetime.datetime(2022, 1, 1, 0, 27), 'ma': datetime.datetime(2022, 1, 1, 0, 57), 'name': 'Convoy_127'}
Convoy_128 =  {'md': datetime.datetime(2022, 1, 1, 1, 3, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 21, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 27, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 57, 30), 'name': 'Convoy_128'}
Convoy_129 =  {'md': datetime.datetime(2022, 1, 1, 1, 4), 'pa': datetime.datetime(2022, 1, 1, 0, 22), 'pd': datetime.datetime(2022, 1, 1, 0, 28), 'ma': datetime.datetime(2022, 1, 1, 0, 58), 'name': 'Convoy_129'}
Convoy_130 =  {'md': datetime.datetime(2022, 1, 1, 1, 4, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 22, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 28, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 58, 30), 'name': 'Convoy_130'}
Convoy_131 =  {'md': datetime.datetime(2022, 1, 1, 1, 5), 'pa': datetime.datetime(2022, 1, 1, 0, 23), 'pd': datetime.datetime(2022, 1, 1, 0, 29), 'ma': datetime.datetime(2022, 1, 1, 0, 59), 'name': 'Convoy_131'}
Convoy_132 =  {'md': datetime.datetime(2022, 1, 1, 1, 5, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 23, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 29, 30), 'ma': datetime.datetime(2022, 1, 1, 0, 59, 30), 'name': 'Convoy_132'}
Convoy_133 =  {'md': datetime.datetime(2022, 1, 1, 1, 6), 'pa': datetime.datetime(2022, 1, 1, 0, 24), 'pd': datetime.datetime(2022, 1, 1, 0, 30), 'ma': datetime.datetime(2022, 1, 1, 1, 0), 'name': 'Convoy_133'}
Convoy_134 =  {'md': datetime.datetime(2022, 1, 1, 1, 6, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 24, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 30, 30), 'ma': datetime.datetime(2022, 1, 1, 1, 0, 30), 'name': 'Convoy_134'}
Convoy_135 =  {'md': datetime.datetime(2022, 1, 1, 1, 7), 'pa': datetime.datetime(2022, 1, 1, 0, 25), 'pd': datetime.datetime(2022, 1, 1, 0, 31), 'ma': datetime.datetime(2022, 1, 1, 1, 1), 'name': 'Convoy_135'}
Convoy_136 =  {'md': datetime.datetime(2022, 1, 1, 1, 7, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 25, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 31, 30), 'ma': datetime.datetime(2022, 1, 1, 1, 1, 30), 'name': 'Convoy_136'}
Convoy_137 =  {'md': datetime.datetime(2022, 1, 1, 1, 8), 'pa': datetime.datetime(2022, 1, 1, 0, 26), 'pd': datetime.datetime(2022, 1, 1, 0, 32), 'ma': datetime.datetime(2022, 1, 1, 1, 2), 'name': 'Convoy_137'}
Convoy_138 =  {'md': datetime.datetime(2022, 1, 1, 1, 8, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 26, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 32, 30), 'ma': datetime.datetime(2022, 1, 1, 1, 2, 30), 'name': 'Convoy_138'}
Convoy_139 =  {'md': datetime.datetime(2022, 1, 1, 1, 9), 'pa': datetime.datetime(2022, 1, 1, 0, 27), 'pd': datetime.datetime(2022, 1, 1, 0, 33), 'ma': datetime.datetime(2022, 1, 1, 1, 3), 'name': 'Convoy_139'}
Convoy_140 =  {'md': datetime.datetime(2022, 1, 1, 1, 9, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 27, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 33, 30), 'ma': datetime.datetime(2022, 1, 1, 1, 3, 30), 'name': 'Convoy_140'}
Convoy_141 =  {'md': datetime.datetime(2022, 1, 1, 1, 10), 'pa': datetime.datetime(2022, 1, 1, 0, 28), 'pd': datetime.datetime(2022, 1, 1, 0, 34), 'ma': datetime.datetime(2022, 1, 1, 1, 4), 'name': 'Convoy_141'}
Convoy_142 =  {'md': datetime.datetime(2022, 1, 1, 1, 10, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 28, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 34, 30), 'ma': datetime.datetime(2022, 1, 1, 1, 4, 30), 'name': 'Convoy_142'}
Convoy_143 =  {'md': datetime.datetime(2022, 1, 1, 1, 11), 'pa': datetime.datetime(2022, 1, 1, 0, 29), 'pd': datetime.datetime(2022, 1, 1, 0, 35), 'ma': datetime.datetime(2022, 1, 1, 1, 5), 'name': 'Convoy_143'}
Convoy_144 =  {'md': datetime.datetime(2022, 1, 1, 1, 11, 30), 'pa': datetime.datetime(2022, 1, 1, 0, 29, 30), 'pd': datetime.datetime(2022, 1, 1, 0, 35, 30), 'ma': datetime.datetime(2022, 1, 1, 1, 5, 30), 'name': 'Convoy_144'}


Convoy = [Convoy_73 , Convoy_74 , Convoy_75 , Convoy_76 , Convoy_77 , Convoy_78 , Convoy_79 , Convoy_80 , Convoy_81 , Convoy_82 , Convoy_83 , Convoy_84 , Convoy_85 , Convoy_86 , Convoy_87 , Convoy_88 , 
 Convoy_89 , Convoy_90 , Convoy_91 , Convoy_92 , Convoy_93 , Convoy_94 , Convoy_95 , Convoy_96 , Convoy_97 , Convoy_98 , Convoy_99 , Convoy_100 , Convoy_101 , Convoy_102 , Convoy_103 , Convoy_104 , 
 Convoy_105 , Convoy_106 , Convoy_107 , Convoy_108 , Convoy_109 , Convoy_110 , Convoy_111 , Convoy_112 , Convoy_113 , Convoy_114 , Convoy_115 , Convoy_116 , Convoy_117 , Convoy_118 , Convoy_119 , 
 Convoy_120 , Convoy_121 , Convoy_122 , Convoy_123 , Convoy_124 , Convoy_125 , Convoy_126 , Convoy_127 , Convoy_128 , Convoy_129 , Convoy_130 , Convoy_131 , Convoy_132 , Convoy_133 , Convoy_134 , 
 Convoy_135 , Convoy_136 , Convoy_137 , Convoy_138 , Convoy_139 , Convoy_140 , Convoy_141 , Convoy_142 , Convoy_143 , Convoy_144 , 
 Convoy_1 , Convoy_2 , Convoy_3 , Convoy_4 , Convoy_5 , Convoy_6 , Convoy_7 , Convoy_8 , Convoy_9 , Convoy_10 , Convoy_11 , Convoy_12 , Convoy_13 , Convoy_14 , Convoy_15 , Convoy_16 ,Convoy_17 ,
 Convoy_18 , Convoy_19 , Convoy_20 , Convoy_21 , Convoy_22 , Convoy_23 , Convoy_24 , Convoy_25 , Convoy_26 , Convoy_27 , Convoy_28 , Convoy_29 , Convoy_30 , Convoy_31 , Convoy_32 , Convoy_33 , Convoy_34 ,
 Convoy_35 , Convoy_36 , Convoy_37 , Convoy_38 , Convoy_39 , Convoy_40 , Convoy_41 , Convoy_42 , Convoy_43 , Convoy_44 , Convoy_45 , Convoy_46 , Convoy_47 , Convoy_48 , Convoy_49 , Convoy_50 , Convoy_51 ,
 Convoy_52 , Convoy_53 , Convoy_54 , Convoy_55 , Convoy_56 , Convoy_57 , Convoy_58 , Convoy_59 , Convoy_60 , Convoy_61 , Convoy_62 , Convoy_63 , Convoy_64 , Convoy_65 , Convoy_66 , Convoy_67 , Convoy_68 ,
 Convoy_69 , Convoy_70 , Convoy_71 , Convoy_72] 




# Generates a random number between
# a given positive range


i=0
lis1=[]
lis2=[]

for m in lis_cur_mum:
    if (isinstance(m, datetime.datetime)):
        lis1.append(i)
    i+=1
print(lis1)

i=0
for m in lis_cur_pun:
    if (isinstance(m, datetime.datetime)):
        lis2.append(i)
    i+=1
print(lis2)

st_t_m = datetime.datetime(2022,1,1,0,0,0)
st_t_p = datetime.datetime(2022,1,1,0,0,0)

print(len(lis_cur_mum))

ff=0
i=0
for i in range(len(lis1)-11):
    temp = random.randint(0, len(lis1)-1)
    ele = lis1[temp]
    lis_cur_mum[ele]=st_t_m
    lis1.remove(ele)
    if (ff%6==0):
        st_t_m+=datetime.timedelta(0,30)
        ff=0
    ff+=1

i=0
ff=0
for i in range(len(lis2)-11):
    temp = random.randint(0, len(lis2)-1)
    ele = lis2[temp]
    lis_cur_pun[ele]=st_t_p
    lis2.remove(ele)
    if (ff%6==0):
        st_t_p+=datetime.timedelta(0,30)
        ff=0
    ff+=1



b = datetime.datetime(2022,1,1,0,0,0)
for i in range(2220):
    lis_mum=[]
    lis_pun=[]
    op = b + datetime.timedelta(0,30)
    
    j=0
    for ll in lis_cur_mum:
        if (isinstance(ll, datetime.datetime)):
            if (op >= ll):
                lis_mum.append(j)
        j+=1
    print(lis_mum)
    
    j=0
    for ll in lis_cur_pun:
        if (isinstance(ll, datetime.datetime)):
            if (op >= ll):
                lis_pun.append(j)
        j+=1
    print(lis_pun)
    
    print(b)
    for stri in Convoy :
        if stri["md"] == b and i<2160:
            print()
            stri["pa"]=stri["md"]+datetime.timedelta(0,1800)
            stri["pd"]=stri["pa"]+datetime.timedelta(0,360)
            stri["ma"]=stri["pd"]+datetime.timedelta(0,1800)
            stri["md"]=stri["ma"]+datetime.timedelta(0,360)
            print(stri['name'] , " Departure from Mumbai")
            
        elif stri["pd"] == b and i<2160:
            print()
            print(stri['name'], " Departure from Pune")
            

        elif stri["pa"] == b :
            print()
            print(stri["name"]," Arrival at Pune")
        
        elif stri["ma"] == b :
            print()    
            print(stri['name']," Arrival at Mumbai")    
        
        #will be arriving in pune in next 30 sec
        elif stri["pa"] == op:
            print()
            for tm in Convey[stri['name']]:
                temp = random.randint(0, len(lis_pun)-1)
                ele = lis_pun[temp]
                lis_cur_pun[ele]=stri["pd"]
                print("Pod ",tm, "part of ",stri['name'] ," arriving at pod bay" , ele , "in 30 Sec Pune station")
                lis_pun.remove(ele)
            

        elif stri["ma"] == op and i<2219:
            print()
            for tm in Convey[stri['name']]:
                temp = random.randint(0, len(lis_mum)-1)
                ele = lis_mum[temp]
                lis_cur_mum[ele]=stri["md"]
                print("Pod ",tm, "part of ",stri['name'] , " arriving at pod bay" , ele , "in 30 Sec Mumbai station")
                lis_mum.remove(ele)

    print()
    b=b+datetime.timedelta(0,30)
    time.sleep(3)