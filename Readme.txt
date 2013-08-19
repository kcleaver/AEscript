AE script - 
designed to allow user to parse text fields from a Adobe After Effects template, and replace text dynamically and batch render out videos with finalized translations.
Written by Kyle Cleaver and Grant Shwartz
📌-place where action or code needs to be run.

1. Setup AE template -

   a. Setup AE template similar to example, add all needed text fields in english and import video track (example video.mov), and make sure video stays in your working directory during entire project.

   b. for project you need text fields to be replaced dynamically. This includes andy fade in/out of text, placement, timing, and any special font properties (bold, color, etc)  Note, full lines of bold text with be perserved, however single random words in a string that are set to a bold, or heavier weight will not be preserved only full lines.

   c. Ensure that every text layer has been set to pull the text dynamically, under each layer drop down the text options and select Source text, add/overwrite the expression in this field with the following expression:  📌text.sourceText=name

   d. Make sure that your project has all text layer set to center justified to ensure the text expands out in both directions evenly, and even after running scripts it is a good idea to go back and check the final export to ensure you don't have a translation that need to be broken out into another line due to the additional space needed for some translation strings.

   e. You can create a new project, or recommended simply re-working the provided template to fit any new project's needs.

   f. Make sure in your project to send the composition to the render queue before it is setup to run through the script, and change the render setting from lostless to H.264 codec.

   g. Save template as, select save as an xml, this will save out as a *.aepx file.



2. Extract the strings from template to send off for translations -

   a. Open the *.aepx file in sublime text, or any preferred text editor, and run a find command. (OSX = Command + F / Win = Control + F)

   b. type or copy/paste the regular expression: 📌<string>.*

   c. Collect/copy all, and paste into a new file to be named en.txt (to be your source or mother strings)

   d. The first string relates to the export name of the project, for example <string>projectname_en</string> with be in this file, however each translation will what to make projectname_LANG inbetween the first set of string tags. This will set the projects to export out the lang variable for each video.

   e. Save ex.txt and send these off to translation vendor, request translations back in the same format lang.txt, example fr.txt (french), es.txt (Spanish), and so on.


3. Feed the translations text files into the AEscript.py - 

   a. First check to ensure you have all the locals setup in the script file, open in prefered text editor and modify the following line to match the translations assets:
   locales = ["de", "es", "fr", "it", "ja", "pl", "zh"] any additional translations will simply need to match so if you want to add another lang like Russian, and , "ro" and ensure you have your russian translations named ro.txt, you can also set as "ro_RO" but the txt file will need to be named ro_RO.txt to match, if asset is missing you will get error message however script will still complete, if you get error message, simply use a notification to check for missing asset or broken file name, etc.

   b. To run the script make sure all your translation files are in the same directory as your script.

   c. Open command line and run the following (* being the name or your project/template file), also make sure you have added all translations needed to be processed:  
   📌python AEscript.py *.aepx de.txt es.txt fr.txt it.txt

   d. This will quickly run and result in creating multiple After Effects project files (each correlating to the lang.txt file) example: data_fr.aepx (This is a duplicate of the project with with French translation strings added to the AE project.)  Note: please check that you have all the languages required for the given requirements.

4. Final After Effects Batch render - (automatic and manual setup included)
  
   Automatic:

   a. Just like with the AEscript.py file, you will need to initially setup the batch script for all the language requirements, however once this has been completed can be reused without needing additional setup. (First time is always the worst time)

   b. Right click on the AERenderQ_CS6 batch script and choose Show Package Contents, navigate to /Contents/Resources/Scripts/main.scpt Double click on main.scpt and open in AppleScript editor (Windows users can access simply by purchasing a Mac!)

   c. you will need to set the projectfile_path, render_cmd, and tell command example:

      1. set projectfile_path1 to the "/Users/kcleaver/Desktop/project/data_es.aepx"
      2. set render_cmd1 to "'/Applications/Adobe After Effects CS6/aerender' -sound ON -project " & projectfile_path1
      3. tell application "Terminal"
		       do script with command render_cmd1 in window 1
		       activate
	     end tell

   d. Note: as you add more remember to change the variable number, projectfile_path2, render_cmd2, and so on.

   e. Once you have all the different translations setup initially, then you can simply drag and drop all the project files at once onto the AERenderQ_CS6 batch script (make sure you have a command window open and BAM! You projects will begin to render in order through command line without ever opening After Effects.)  When complete you will have a finalized mp4 video with translations for each lang added.  The files will be in the format of projectname_lang.mp4, example: data_fr.mp4

   Manual:

   a. Instead of using AERenderQ_CS6, simply drag and drop (1) project file onto AERenderQ, this will open a command window and the first project will begin to render via command line, as it starts running you can then drag and drop another project onto the batch script AERenderQ, this can be done as a queue so you can drag and drop as many as you need rendered and they will queue up one after another, however note you can only drag one file at a time to be dropped into the render queue, this batch script doesn't support multiple files to be dropped at once unless you follow the above automatic setup.




