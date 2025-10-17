# Files, Directories and paths

open
read
close
Now when you are done with a file it is advised that you close it down but there is a way to auto close it
we can use the with method
"with open(_) as file"
now we can refer to the file as "file" and it will automatically close when we are done

Niw when using open we can see an arguments called mode, by default it is set to "r"which is read only. but we can set it to "w" whuch is write now we can use the write method on it to write extra e.g
file.write("New Text.")
This write method overwrites the former information written on the file but we can use "a" to append, the write method is still used

Now when we try to use open on a file that does't exist py actually creates the file for us
