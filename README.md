# simpleBackLinker
A really simple Python script to create backlinks in an Obsidian Vault

This is just a simple backlinking script I use in my Obsidian maintenance. I created it and then improved it with help from ChatGPT. 

Since I name every note (using templates) with YYYY-MM-DD as a prefix, this script runs on my Mac and creates backlinks inside each daily note to include any notes created each day. 

This script runs on your entire Obsidian Vault and creates the back links automatically based on filenames (i.e. it looks for notes with the prefix date matching the YYYY-MM-DD format.)

Simply alter the VAULT_PATH and DAILY_JOURNAL_FOLDER entries and run it!

Remmeber to install Python before running. 

The script will create a sub on your daily notes called "Notes today" - you can edit this section name easily. The script will update if you add more notes after running it once, it will append rather than duplicate to avoid ugliness in the notes.


