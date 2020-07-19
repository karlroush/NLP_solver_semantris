# NLP_solver_semantris
This tool uses a computer vision in combination with Merriam-Webster's Thesaurus API and a NLP model built from Google News data to solve the Google Experiment [Semantris](https://research.google.com/semantris/). You can read about Google's development of Semantris at [https://experiments.withgoogle.com/semantris](https://experiments.withgoogle.com/semantris)

See it in action: [https://youtu.be/MQKlzLtKqm4](https://youtu.be/MQKlzLtKqm4)

# Objective
I was inspired by [@pravj](https://github.com/pravj)'s project "[semantris-solver](https://github.com/pravj/semantris-solver)", though I found that their code had several issues:
- It didn't work. At the most basic level, references to dependencies were broken or out of date.
- The approach of solely using word embeddings was far too slow.
- Documentation was essentially non-existent.
- Code was exceedingly verbose and not easy to navigate.

I’ve rebuilt the project from scratch, utilizing a new approach and modern methods, offering improvements over the original in every aspect.

*This program is not faster than a human, though this could simply be a limitation of my available processing power.* 

# What you'll need
This project makes use of Tesseract OCR and a NLP model built on Google. You will need
- Download the [word2vec pre-trained Google News corpus](https://github.com/karoush/NLP_solver_semantris/blob/master/process_graphic.png)
- Install Tesseract OCR ([Github](https://github.com/tesseract-ocr/tesseract) or [.exe](https://sourceforge.net/projects/tesseract-ocr/files/latest/download))
- An API key from Merriam-Webster ([how to apply](https://dictionaryapi.com/))

This program also uses PyAutoGUI for clicking and screenshots. Because of this, you may need to modify the locations and dimensions in ```roush_main.py``` which contains ```getCoords()``` to help you.

*A Python environment file (```semantris_env.yml```) has also been provided to assist you in setup. 
<br>Alternatively, use ```pip install -r requirements.txt```*

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
