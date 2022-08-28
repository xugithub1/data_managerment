import sys
import os
import json
import sys


with open("final.txt", 'r') as f:
    file_dict = json.load(f)

unique_dict = {
    "gac": 1,
    "baidu": 1 ,
    "pilot": 1 ,
}

repeat_dict = {
    "gac_curve_c2": 80,
    "gac_change_c2": 40,
    "gac_curve": 5,
    "gac_change": 5,
    "gac_lane_truncation_c2": 3,
    "gac_roadmarker_c2": 3,
    "lukou": 10,
    "gac": 1,
    "pilot": 1,
    "baidu": 1,
}


merge_type = sys.argv[1]

assert str(merge_type) in ["unique", "repeat"], "only support unique and repeat merge type!" 

if merge_type == "unique":
    for k, v in unique_dict.items():
        filelist = file_dict[k]
        for i in range(v):
            for f in filelist:
                if f.startswith("#"):
                    continue
                f = '../projects/' + f
                line = f"cat {f} >> result_unique_v1.json"
                os.system(line)
elif merge_type == "repeat":
    for k, v in repeat_dict.items():
        filelist = file_dict[k]
        for i in range(v):
            for f in filelist:
                if f.startswith("#"):
                    continue
                f = '../projects/' + f
                line = f"cat {f} >> result_repeat_v1.json"
                os.system(line)
