# Setting it up
1. After downloading the "scripts" folder, place it inside your package folder (replacing the old one)
 - make sure that this is the only "scripts" folder in your package
2. Run `catkin build your-package-name`
3. Make all the files in the "scripts" folder executable 
 - by doing it from the "Properties > Permissions" tab **OR** 
 - running `chmod -R +x scripts` in your package directory 
(that recursively makes all the files in the scripts folder executable)
