################################################################################
    # The NoRmAl VeRsIoN #
################################################################################

from sys import argv

script, from_file, to_file = argv

print(f"\nCopying:\n\n{from_file}\n\tto\n{to_file}.")

# we could do these two on one line, how?

# indata = in_file.read()
# in_file = open(from_file.read())
indata = open(from_file).read()

input("\nIf you're ready; hit ENTER to coninue or CTRL-C to abort.\n")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# Because we opend the out_file, we have to close the file. This is because
# there's a limit to how many files can be open at once. Afther that you can't
# open any more files.
out_file.close()


################################################################################ 
    # The OnE LiNeD VeRsIoN #
################################################################################

# from sys import argv; script, from_file, to_file = argv; indata = open(from_file).read(); out_file = open(to_file, 'w'); out_file.write(indata); print("Alright, all done."); out_file.close()
