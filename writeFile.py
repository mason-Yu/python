# coding=utf-8
# Function: traverse all files and subfolders under the specified folder, and modify the file contents
import sys
import os
import glob
import string
fpath = "C:/Users/yum8/Desktop/Python" # file root
sys.argv.append('javaHead.txt') # Here you can add a lot of templates, such "ts, scss"
sys.argv.append('htmlHead.txt')
javaCommentFilename = sys.argv[1]
htmlCommentFilename = sys.argv[2]

# read the java comments
f = open(javaCommentFilename)
javaCommentLines = f.readlines()
javaCommentLines += "\n"
f.close()

# read the html comments
f = open(htmlCommentFilename)
htmlCommentLines = f.readlines()
htmlCommentLines += "\n"
f.close()

def filechanger(path):
        filenames = os.listdir(path)# Save all file names under the specified path to the list filenames
        for filename in filenames:# Loop through each file
                domain = os.path.abspath(path)# Get the path to the specification
                filename = os.path.join(domain,filename)# This filename is the file name with the path
                if os.path.isdir(filename):  # If it is a folder into a recursive call
                    filechanger(filename)
                    continue
                commentLines = ''
                # Here are just matching java, ts, html, scss files
                if(filename.find('.java') >= 0 or filename.find('.ts') >= 0 or filename.find('.scss') >= 0):
                    commentLines = javaCommentLines
                elif (filename.find('.html') >= 0):
                    commentLines = htmlCommentLines
                else:
                    continue
                print(filename)
                fread = open(filename)
                srcfileLines = fread.readlines()
                fread.close()
                srcfileLines = commentLines + srcfileLines
                fwrite = open(filename,'w')
                fwrite.writelines(srcfileLines)
                fwrite.close()

filechanger(fpath)
