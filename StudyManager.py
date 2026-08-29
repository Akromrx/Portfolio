from dataclasses import dataclass, field
from abc import ABC, abstractclassmethod
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from typing import Optional
import os
import json
import datetime


# Custom Exceptions:
class NoLessonsAvailableError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Topic:
    options: dict = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D'
    } # Options for questions

    def __init__(self, subjectT: str, lesson: str, description: str, instance: Optional[str] = None):
        self.subjectT = subjectT # Subject name
        self.lesson = lesson # Lesson name
        self.description = description # Description about the lesson
        self.instance = instance # Instance about the lesson
        self.task = {} # Tasks
        self.answers = [] # Answers to tasks
        
    
    def Review(self):
        """
        Review previous lesson
        """
        # Check and read description
        if isinstance(self.description, str) and os.path.isfile(self.description):
            with open(self.description, 'r') as file:
                description_content = file.read()
        else:
            description_content = self.description
        
        # Check and read instance
        if self.instance and isinstance(self.instance, str) and os.path.isfile(self.instance):
            with open(self.instance, 'r') as file:
                instance_content = file.read()
        else:
            instance_content = self.instance if self.instance else "No examples provided"
        
        print(f"Subject type: {self.subjectT}\nLesson: {self.lesson}\n\nDescription: \n{description_content}\n\nExample(s):\n{instance_content}")
    
    def EditDescription(self):
        """
        Edit existing Description

        Args:
            self.description: existing description
            newDesc: new descritption
        
        If no description is provided, it warns you

        """
        newDesc: str = input("New description: ")
        if (not newDesc) or (newDesc == ""):
            print(f"Please, provide a valid description to edit")
            editAny = str(input("Edit anyway? [Y/n]: "))
            if editAny.lower() == "y":
                self.description = newDesc # Change the Description anyway
            else:
                return

        self.description = newDesc
    
    def AddTask(self):
        # global options
        while True:
            question = str(input("Question [-q for stop]: "))
            if question.lower() == "-q":
                break
            self.task[question] = []
            for i in ['A', 'B', 'C', 'D']:
                option = str(input(f"{i}: "))
                self.task[question].append(option)
            trueanswer = str(input("Answer: "))
            self.answers.append(trueanswer)
            
    
    def ShowTask(self, ovel: Subject): # ovel is the Subject
        useranswers = []
        totalsore = 0
        totalquestion = len(self.answers)
        for i in list(self.task.keys()):
            print(f"Question: {i}\n")
            for j, k in zip(self.task[i], ['A', 'B', 'C', 'D']):
                print(f"{k}) {j}")
            UA = str(input(f"Your answer: "))
            if   UA == "A": UA = self.task[i][0]
            elif UA == "B": UA = self.task[i][1]
            elif UA == "C": UA = self.task[i][2]
            elif UA == "D": UA = self.task[i][3]
            useranswers.append(UA)
        
        print(f"\nYour answer | Correct Answer")
        for i, j in zip(useranswers, self.answers):
            print(f"{i}       | {j}  ", "✅" if i == j else "❌")

            if i == j:
                totalsore += 1
        
        rate = round(totalsore/totalquestion) * 100
        print(f"Correctness rate: {rate}%")
        ovel.TrackProgress('Topic', self.lesson, totalquestion, totalsore)
        # def TrackProgress(self, TType: str, TName: str, NumQ: int, CAns: int):
        

    # def TrackProgress(self, CA):
    #     LQ = len(self.task.keys())

    #     ratio = round(LQ/CA) * 100
    #     date = datetime.date()
    #     self.progress

            


    
    def Save(self):
        """
        Save description and instance to .txt files

        If instance doesn't exist, don't save it.
         
        """
        file_path = f"{lesson}1.txt"
        file_path2 = f"{lesson}2.txt"

        with open(file_path, 'w') as file:
            file.write(self.description)
        self.description = file_path                              

        if self.instance:
            with open(file_path2, 'w') as file:
                file.write(self.instance)
            self.instance = file_path2

class Subjects(ABC):
    def __init__(self, subjectT, description):
        self.name = subjectT # Subject name
        self.CR = np.nan # Correctness rate
        self.lessonsNum = 0 # Number of lessons learnt
        self.description = description # Description about the subject
        self.lessonsLearnt = {} # List of lessons learnt
        self.progress_path = f"{subjectT}_progress.json" # Path name for progress

        self.progress = pd.DataFrame({
            'Test type': [],
            'Topic': [],
            'Questions': [],
            'Correct': [],
            'Time': [],
            'Ratio': []
        })

    @abstractclassmethod
    def NewLesson(self, *args, **kwargs): # Adding new lesson
        pass

    # @abstractclassmethod
    # def Tests(self, *args, **kwargs): # Adding test/task
    #     pass

    # @abstractclassmethod
    # def TrackProgress(self, *args, **kwargs):
    #     pass 

    # # @abstractclassmethod
    def ShowDescription(self):
        print(f"Subject name: {self.name}\n\nDescription:\n {self.description}")

    @abstractclassmethod
    def Save(self, *args, **kwargs):
        pass
    
    @abstractclassmethod
    def ChooseLesson(self, *args, **kwargs):
        pass 

    def Load(self):
        """
        Load saved data from files
        """
        # Load vocabulary
        vocab_file = f"{self.name.replace(' ', '_')}_vocabulary.json"
        if os.path.isfile(vocab_file):
            with open(vocab_file, 'r') as file:
                self.vocabulary = json.load(file)
            print(f"Vocabulary loaded from {vocab_file}")
        
        # Load lessons
        lessons_file = f"{self.name.replace(' ', '_')}_lessons.json"
        if os.path.isfile(lessons_file):
            with open(lessons_file, 'r') as file:
                lessons_data = json.load(file)
            for topic_name, topic_dict in lessons_data.items():
                topic_obj = Topic(
                    subjectT=topic_dict['subjectT'],
                    lesson=topic_dict['lesson'],
                    description=topic_dict['description'],
                    instance=topic_dict.get('instance')
                )
                self.lessonsLearnt[topic_name] = topic_obj
                self.lessonsNum += 1
            print(f"Lessons loaded from {lessons_file}")
        
        # Load progress
        # Check if progress is a file path string
        if isinstance(self.progress, str) and os.path.isfile(self.progress):
            # Load the DataFrame from the file
            self.progress = pd.read_json(self.progress, orient='records')

    def TrackProgress(self, TType: str, TName: str, NumQ: int, CAns: int):
        """
        Save 
        """
        day = datetime.date()
        ratio = round(NumQ/CAns * 100, 2)

        new_data = [TType, TName, NumQ, CAns, day, ratio]
        self.progress.loc[len(self.progress)] = new_data

class German(Subjects):
    def __init__(self, subjectT, description, level, ):
        super().__init__(subjectT=subjectT, description=description)
        self.level = level
        self.vocabulary = {}
        
        
    def NewLesson(self):
        """
        Ask the topic name
        If topic already exists, cannot recreate it

        First create a new class using given arguments (subjectT, topic, description, instance: Optional)
        Then links it to the topic in lessonsLearnt dictionary

        """
        topic = input("Topic: ")
        
        if topic in self.lessonsLearnt.keys():
            print(f"Lesson '{topic}' already exists!")
            return
        
        description = input("Description: ")
        instance = input("Instance (press Enter to skip): ")
        
        if instance:
            new_lesson = Topic(subjectT=self.name, lesson=topic, description=description, instance=instance)
        else:
            new_lesson = Topic(subjectT=self.name, lesson=topic, description=description)
        
        self.lessonsLearnt[topic] = new_lesson
        self.lessonsNum += 1
        print(f"Lesson '{topic}' added successfully!")
    
    def ChooseLesson(self):
        try:
            lesson_list = list(self.lessonsLearnt.keys())
            for i, lesson_name in enumerate(lesson_list):
                print(f"{i+1}: {lesson_name}")
            
            CLesson = int(input("Lesson number: "))
            if 0 < CLesson <= len(lesson_list):
                CurrentLesson = self.lessonsLearnt[lesson_list[CLesson-1]]
                return CurrentLesson
            else:
                print("Invalid lesson number!")
                return None
        except NoLessonsAvailableError:
            print(f"No lesson is available")
        
    def AddVocabulary(self, vocabs=None, topic=None):
        """
        Add new vocabulary to the given topic

        If topic already exists, existing vocabulary will be extended

        Type -Q or -q to stop adding vocabulary
        """
        # Load vocabulary if it's a file path
        if isinstance(self.vocabulary, str) and os.path.isfile(self.vocabulary):
            with open(self.vocabulary, 'r') as file:
                self.vocabulary = json.load(file)
        
        topic = str(input(f"Vocabulary topic: "))

        if not(topic in self.vocabulary):
            self.vocabulary[topic] = []

        print("Type -Q to stop")
        words = []
        while True:
            germanvoc = str(input("German word: "))
            english = str(input("English meaning: "))
            if (germanvoc.lower() == "-q") or (english.lower() == "-q"):
                break
            new_vocab = {germanvoc: english}
            self.vocabulary[topic].append(new_vocab)
    
    def VocabTest(self):
        """
        Vocabulary quizez

        Choose a topic and test yourself
        """
        # Load vocabulary if it's a file path
        vocab_data = self.vocabulary
        if isinstance(self.vocabulary, str) and os.path.isfile(self.vocabulary):
            with open(self.vocabulary, 'r') as file:
                vocab_data = json.load(file)
        
        if vocab_data == {}:
            print("No vocabulary available yet!")
            return False
        
        print("Choose a topic:")
        for i, j in enumerate(list(vocab_data.keys())):
            print(f"{i}) {j}")
        Topic = str(input("Enter topic name: "))
        
        if Topic not in vocab_data:
            print("Topic not found!")
            return False
        
        correct_answers: int = 0
        asks: int = 0
        
        # Shuffle the vocabulary list
        vocab_list = vocab_data[Topic].copy()
        np.random.shuffle(vocab_list)
        
        for vocab_dict in vocab_list:
            german_word = list(vocab_dict.keys())[0]
            english_meaning = vocab_dict[german_word]

            print(f"German word: {german_word}")
            user_answer = input("English meaning: ")

            if user_answer.lower() == english_meaning.lower():
                correct_answers += 1
                print("✅ Correct!")
            else:
                print(f"❌ Wrong! Correct answer: {english_meaning}")
            asks += 1
        
        print(f"{correct_answers} out of {asks} is correct!")
        # Add trackprogress to vocabquiz
    
    def Save(self):
        """
        Save vocabulary and lessons to JSON files for persistent storage.
        
        This method converts in-memory data structures to JSON files:
        - Vocabulary dictionary -> {SubjectName}_vocabulary.json
        - Lessons dictionary -> {SubjectName}_lessons.json
        
        After saving, the attributes are replaced with file paths (strings)
        so the program knows data is stored on disk.
        """
        
        # === SAVE VOCABULARY ===
        # Check if vocabulary is a dictionary (in-memory data) and not empty
        if isinstance(self.vocabulary, dict) and self.vocabulary:
            # Create filename by replacing spaces with underscores
            vocab_file = f"{self.name.replace(' ', '_')}_vocabulary.json"
            
            # Write vocabulary dictionary to JSON file with pretty formatting
            with open(vocab_file, 'w') as file:
                json.dump(self.vocabulary, file, indent=2)
            
            # Replace the dictionary with the file path string
            # This marks that data is now stored on disk
            self.vocabulary = vocab_file
            print(f"Vocabulary saved to {vocab_file}")
        
        # === SAVE LESSONS ===
        # Check if there are any lessons to save
        if self.lessonsLearnt:
            # Create filename for lessons
            lessons_file = f"{self.name.replace(' ', '_')}_lessons.json"
            
            # Convert Topic objects to dictionaries for JSON serialization
            lessons_data = {}
            for topic_name, topic_obj in self.lessonsLearnt.items():
                # Extract relevant attributes from each Topic object
                lessons_data[topic_name] = {
                    'subjectT': topic_obj.subjectT,      # Subject name
                    'lesson': topic_obj.lesson,          # Lesson name
                    'description': topic_obj.description, # Lesson description
                    'instance': topic_obj.instance       # Example/instance (can be None)
                }
            
            # Write lessons data to JSON file
            with open(lessons_file, 'w') as file:
                json.dump(lessons_data, file, indent=2)
            print(f"Lessons saved to {lessons_file}")
    
        # === SAVE PROGRESS ===
        
        self.progress.to_json(self.progress_path, orient='records')

    




GermanDesc = """
German is a major West Germanic language with over 110-130 million total speakers, serving as an official language in Germany, Austria, Switzerland, Liechtenstein, Luxembourg, and parts of Belgium. It is the most widely spoken native language in the European Union. Known for its compound words, strict grammar with three genders (masculine, feminine, neuter), and four cases (nominative, accusative, dative, genitive), it is a highly structured language.
"""
# GermanLan.ShowDescription()
# GermanLan.NewLesson()

GermanLan: German = German('German Language', GermanDesc, 'A1')
GermanLan.Load()  # Load saved data if available

while True:
    next_command = input("Next command to execute (type -h for help): ")
    current_subject = GermanLan
    next_command = next_command.lower()
    if next_command == "-h":
        print(f"Type -SB to choose the subject")
        print(f"Type -TP to choose the topic inside the chosen subject")
        print(f"Type -NL to add new lesson to the current subject")
        print(f"Type -AV to add vocabulary")
        print(f"Type -VT to take vocabulary test")
        print(f"Type -S to save all data")
        print(f"Type -Q to quit session")
    
    
    elif next_command == "-tp":
        current_topic: Topic = current_subject.ChooseLesson()
        if current_topic:
            while True:
                topic_command = input(f"Input the next command [-H for help]: ")
                topic_command = topic_command.lower()
                if topic_command == "-h":
                    print(f"""
                    -R to review
                    -E to edit the description
                    -A to add/edit an instance
                    -AT to add task
                    -ST to show task
                    -Q to quit session
                    """)
                elif topic_command == "-r":
                    current_topic.Review()
                elif topic_command == "-at":
                    current_topic.AddTask()
                elif topic_command == "-st":
                    current_topic.ShowTask()
                elif topic_command == "-q":
                    break
                elif topic_command == "e":
                    current_topic.EditDescription()
    
    elif next_command == "-nl":
        current_subject.NewLesson()
    
    elif next_command == "-av":
        current_subject.AddVocabulary()
    
    elif next_command == "-vt":
        current_subject.VocabTest()
    
    elif next_command == "-s":
        current_subject.Save()
    
    elif next_command == "-q":
        save_prompt = input("Save before quitting? [Y/n]: ")
        if save_prompt.lower() == "y":
            current_subject.Save()
        break
    

# Make Vocabulary quizez at random


