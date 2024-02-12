import os

import path_config

def path_op():
    file_paths =[]
    apps = []
    categories =[]

    for root, dir, filenames in os.walk(path_config.base_dir):
        #print("\nROOT:{} \nDIR : {} \nFILE:".format(root, dir, filenames))

        for filename in filenames:
            dummy_path = os.path.join(root,filename)
            print(dummy_path)

            if(dummy_path.lower().endswith('.py')):
                print(filename)
                t1=dummy_path.split("\\")[-1]
                t2=dummy_path.split("\\")[-1].split(".")[0]
                print(t1,t2)
                # apps.append()
            else:
                print("This is text file", filename)
            



path_op()
# def main():
#     path_op()
