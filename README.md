# NLP_solver_semantris
This tool uses a combination of Merriam-Webster's Thesaurus API and an NLP model built from Google News data to solve the Google game Semantris.


*This progam is  not faster than a human, though this could simply be a limitation of my avaible processing power.* 

# What you'll need
This project makes use of Tesseract OCR and a NLP model built on Google. You will need
- Download the [word2vec pre-trained Google News corpus](https://github.com/karoush/NLP_solver_semantris/blob/master/process_graphic.png)
- Install Tesseract OCR ([Github](https://github.com/tesseract-ocr/tesseract) or [.exe](https://sourceforge.net/projects/tesseract-ocr/files/latest/download))
<br>This program also uses PyAutoGUI for clicking and screenshots. Because of this, you may need to modify the locations and dimensions in ```roush_main.py``` which contains ```getCoords()``` to help you.

**A Python enviroment file has also been provided to assist you in setup** 
# How it works
![](https://github.com/karoush/NLP_solver_semantris/blob/master/process_graphic.png)
The program works as follows:
1. **Load the NLP model**
2. **Find the target word**
    1. Take a screenshot of the current game
	2. Find the triangle indicator using OpenCV
	3. Isolate the text next to the triangle indicator
	4. Save the cropped target word
3. **Identify the target word**
    1. Convert the text to greyscale
	2. Use Tesseract OCR to convert image to string
4. **Find related word(s)**
    1. Make a call to the Merriam-Webster's Thesaurus API for synonyms. This is usually faster than using the NLP model which is important because Semantris is all about speed.
	2. From the list of synonyms, ignore words with the same first four letters (rule from Semantris)
	3. Take the first item in the list and go to the next process 
	3. If the API call fails or Semantris does not accept the entered word, use the NLP model
	    1. Use the NLP model to return the top 10 most related words
		2. Parse the list according to the same rules as above.
5. **Input the related word**
    1. Use PyAutoGUI to click on the entry box
	2. Type in the related word 
	3. If Semantris does not accept the word, return to the previous step
6. **Exit the process**
    1. The program can be stopped by moving the mouse outside user set boundaries
	2. Alternatively, hit cntrl+alt+del which will cause the screenshot functionality to fail and quit the process
