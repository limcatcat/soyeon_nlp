from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice # built-in module

# main app objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Generator")
main_window.resize(600, 270)


# create all app objects/widgets
title = QLabel("Random Words")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

btn1 = QPushButton("Generate")
btn2 = QPushButton("Generate")
btn3 = QPushButton("Generate")


# all design here
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(btn1)
row3.addWidget(btn2)
row3.addWidget(btn3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)


# create functions
my_words = [
    "Pug", "Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Beagle",
    "Poodle", "French Bulldog", "Yorkshire Terrier", "Rottweiler", "Boxer",
    "Dachshund", "Siberian Husky", "Doberman Pinscher", "Great Dane", "Pembroke Welsh Corgi",
    "Australian Shepherd", "Shih Tzu", "Boston Terrier", "Pomeranian", "Havanese",
    "Shetland Sheepdog", "Brittany", "English Springer Spaniel", "Mastiff", "Cavalier King Charles Spaniel",
    "Weimaraner", "Bernese Mountain Dog", "Miniature Schnauzer", "Vizsla", "Chihuahua",
    "Collie", "Border Collie", "West Highland White Terrier", "Basset Hound", "Rhodesian Ridgeback",
    "Shiba Inu", "Shetland Sheepdog", "Maltese", "Bichon Frise", "Bullmastiff",
    "Newfoundland", "Bloodhound", "Chinese Shar-Pei", "Cane Corso", "Soft-Coated Wheaten Terrier",
    "Saint Bernard", "Old English Sheepdog", "Dalmatian", "Italian Greyhound", "Portuguese Water Dog",
    "Alaskan Malamute", "Samoyed", "Great Pyrenees", "Scottish Terrier", "Cairn Terrier",
    "Irish Wolfhound", "Australian Terrier", "American Staffordshire Terrier", "Pekingese", "Lhasa Apso",
    "Papillon", "Border Terrier", "Basenji", "Afghan Hound", "Silky Terrier",
    "Japanese Chin", "Norwegian Elkhound", "Pointer", "Whippet", "Irish Setter",
    "Airedale Terrier", "Chinese Crested", "Irish Terrier", "Wire Fox Terrier", "Norwich Terrier",
    "Komondor", "Brussels Griffon", "Irish Water Spaniel", "American Eskimo Dog", "Finnish Spitz",
    "Manchester Terrier", "Sealyham Terrier", "Toy Fox Terrier", "Coton de Tulear", "Field Spaniel",
    "Xoloitzcuintli", "Dandie Dinmont Terrier", "Skye Terrier", "Black Russian Terrier", "Bedlington Terrier",
    "Swedish Vallhund", "Lancashire Heeler", "Plott", "Sloughi", "American Hairless Terrier", "Toy Manchester Terrier", "Russian Toy", "Cesky Terrier", "Teddy Roosevelt Terrier",
    "Miniature Bull Terrier", "Peruvian Inca Orchid", "Pyrenean Shepherd", "Canaan Dog", "American Foxhound"
]

def random_word1():
    word = choice(my_words)
    text1.setText(word)

def random_word2():
    word = choice(my_words)
    text2.setText(word)

def random_word3():
    word = choice(my_words)
    text3.setText(word)


# events
btn1.clicked.connect(random_word1)
btn2.clicked.connect(random_word2)
btn3.clicked.connect(random_word3)


# show/run our app
main_window.show()
app.exec_()

