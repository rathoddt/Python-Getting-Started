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
                apps.append(t2)
                file_paths.append(dummy_path)
                print("Category:",dummy_path.split("\\")[-2])
                categories.append(dummy_path.split("\\")[-2])
            else:
                print("This is text file", filename)
    
    return file_paths, apps, categories
            



file_paths, apps, categories =path_op()

if file_paths and apps and categories :
    print('All vars are loaded')
    print("Filepaths", file_paths)
    print("apps:", apps)
    print("categories: ", categories)


# def main():
#     path_op()
