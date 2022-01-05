#
# Read and write files using the built-in Python file methods
#

def main(): 
  string1 ='textfile{}.txt'
  for i in range(1,4): 
    # Open a file for writing and create it if it doesn't exist
    f = open(string1.format(i),"a+")
  
    # Open the file for appending text to the end
    # f = open("textfile.txt","a+")

    # write some lines of data to the file
    for i in range(10):
      f.write("This is line %d\r\n" % (i+1))
  
  # close the file when done
    f.close()
  
    
if __name__ == "__main__":
  main()
