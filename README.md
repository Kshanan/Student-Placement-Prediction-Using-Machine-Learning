# Student-Placement-Prediction-Using-Machine-Learning

STUDENT’S PLACEMENT PREDICTION USING MACHINE LEARNING


 **1.0 ABSTRACT :**
 
 
Predicting academic performance is an important task for the students in university, college, schools and coaching centres etc. The factors which affect the student’s academic performance are class quizzes, assignments, lab exams, mid, and final exams. The student’s academic performance should be informed to the class teacher in advance that will decrease the student’s dropout and increase the performance. In this project we use machine learning regression algorithm such as Random Forest Regression are implemented to predict the student’s performance for the academic placements. The performance of an algorithm has been evaluated based on confusion matrix, accuracy, precision, recall, and F1 score. The obtained result shows that the Random Forest Regression algorithm performs better.

**2.0 INTRODUCTION :**


Student’s Placement is a crucial part of an academic institution. This is considered as one of the important measures for many superior universities. Some researchers stated that the student’s academic performance can be measured through learning assessment and co-curriculum activities. Though, the majority of researchers have mentioned that the student's past performances, achievements, and grades can play a vital role to predict the student’s success rate in Placements. Predominantly, most of the higher level institutions use grade as the main measure to assess student’s performance. In addition, course structure, assignment marks, final exam scores, and extracurricular activities will affect the student’s academic performance. The student’s academic program can be well planned during their sophomore period of studies in an institution to analyse the performance of students. At present, machine learning algorithms are most popular to evaluate student’s academic performance that has been extensively applied in the education sector. Mining the educational data used to predict the student’s academic performance. As a result, it would help the educators/faculty to improve the teaching approach in a constructive way. In addition, the teacher could observe student’s achievements also. In our project we use these performance attributes to predict a student’s placement in a company. Here we use a python web development frame work Django to design a UI, wherein a student can login and give simple assessments on Technical, Aptitude and Puzzle Solving. Further Teachers can Grade them on Communication skills, Training, Internships, Academic Scores etc. 


**3.0 LITERATURE SURVEY**


During my literature review study, to define the research problem as well as objectives, I would like to mention that I went through a lot of research papers and web application statistics. Few of paper’s summarized details are as follows.
1. “Predicting Student Academic Performance in KSA using Data Mining Techniques”, Journal of Information Technology & Software Engineering.

In this first research study, author used feature selection technique to reduce the number of feature form the large attribute set. 

2. “Prediction of Students Performance using Machine Learning” by J. Dhilipan

This research focuses on how to classify the most relevant attributes in student data by using prediction algorithm. Using educational machine learning methods, we could potentially improve the performance and progress of students more efficiently in an efficient manner. Students, educator and academic institutions could benefit and also have an impact.
Here the author uses tree algorithm for predicting student performance accurately. In the proposed system Education Data Mining (EDM) is used for the classification. Clustering data mining technique is used for analysing the large set of student database. This technique will speed up the searching process and the also yield the classification result more accurately .A new Learning model has been proposed by using the student information from the college registration .The final dataset is provided as input so ML algorithms which can apply and predict student's academic performance. They selected 13 algorithms from 5 categories of ML they are Naïve Bayes, SVM, MLP, IBK, Rules and tree.


**4.0 METHODOLOGY**


In this section, a brief review of the machine learning techniques that is used in this research is introduced.
1. Random Forest Regression :

 
•	Random Forest Regression is a supervised learning algorithm that uses ensemble learning method for regression. 
•	Ensemble learning method is a technique that combines predictions from multiple machine learning algorithms to make a more accurate prediction than a single model.
•	The diagram above shows the structure of a Random Forest. You can notice that the trees run in parallel with no interaction amongst them. A Random Forest operates by constructing several decision trees during training time and outputting the mean of the classes as the prediction of all the trees.

•	Random forest gives the prediction accuracy of 87%.

•	The fundamental concept behind random forest is the wisdom of crowds wherein a large number of uncorrelated models operating as a committee will outperform any of the individual constituent models.
 

**5.0 EXISTING SYSTEM**:


•	According to the IEEE paper published in the year 2021 “Prediction of Students Performance using Machine Learning “ by J. Dhilipan , here the author has used 9 attributes each of the attribute relates to the students’ academic scores from high school to college .
•	This analysis lacks more of the important attributes that also affects the students’ performance during the placements, I have covered these attributes in the proposed system which collects attributes related to academic scores as well as the inter-personal skills a student possess.


**6.0 PROPOSED SYSTEM:**
 

The first step is collecting the data from the data sources. In our case, the data has been collected using a survey given to the students and the students’ grade book. The second step is pre-processing the data in order to get a normalized dataset and then labelling the data rows. In the third step, the result of the second step, the training and testing dataset, is fed to the Machine Learning algorithm. The Machine Learning Algorithm builds a model using the training data and tests the model using the test data. Finally, the Machine Learning Algorithm produces a trained model that can take as an input a new data row and predict its label.
Attributes Used :
 Technical Skills, Coding Skills, Communication Skills, Aptitude,  Puzzle Solving, Core Knowledge, English Proficiency, Management Skills, Presentation Skills , Academic Performance , Projects, Internships , Training , Backlog.


**7.0 SYSTEM REQUIREMENTS:**

1. Hardware Requirements
 RAM: 4 GB or more
Processor: Intel I3 or more
2. Software Requirements
Operating system:     Windows 7 and above
Coding language:     Python
IDE                     :    Pycharm
Framework          :    Django
Browser              :    Chrome or Microsoft Edge

**8.0 Conclusion:**


Predicting student’s performance is exceptionally useful to help the instructors and learners to improve their learning and teaching process schematically. This project analysed the student’s academic performance with various machine learning algorithms. 

The Random Forest Regression algorithm provide better performance for predicting the Student’s Placement. In conclusion, student’s academic dataset analysis on predicting Student’s Placement has motivated us to carry out further research to be applied in our domain. It will help the educational system to track the student’s academic performance in a structured way.


 

**9.0 REFERENCES:**


1. Nawal Ali Yassein, Rasha Gaffer M Helali and Somia B Mohomad , “Predicting Student Academic Performance in KSA using Data Mining Techniques”, Journal of Information Technology & Software Engineering., Vol.7, No. 5, (2017). 

2. Md. Hedayetul Islam Shovon and Mahfuza Haque, “An Approach of Improving Student’s Academic Performance by using K-means clustering algorithm and Decision tree”, International Journal of Advanced Computer Science and Applications, Vol.3, No. 8, (2012). 

3. Thaddeus Matundura Ogwoka, Wilson Cheruiyot, and George Okeyo, “A Model for Predicting Students’ Academic Performance using a Hybrid of K-means and Decision tree Algorithms”, International Journal of Computer Applications Technology and Research, Vol. 4, No. 9, (2015), pp.693 – 697.

 4. Prashant Sahai Saxena and M. C. Govil, “Prediction of Student’s Academic Performance using Clustering”, National Conference on Cloud Computing & Big Data., (2015). 5. Nguyen Thai-Nghe, Andre Busche, and Lars Schmidt-Thieme, “Improving Academic Performance Prediction by Dealing with Class Imbalance”, International Conference on Intelligent Systems Design and Applications, IEEE Xplore., (2009)

6. Brijesh Kumar Baradwaj, and Saurabh Pal, “Mining educational data to analyze students' performance. International Journal of Advanced Computer Science and Applications Vol. 2, No. 6. (2011). 

7. Carlos Márquez-Vera, Alberto Cano, Cristóbal Romero & Sebastián Ventura, “Predicting student failure at school using genetic programming and different data mining approaches with high dimensional and imbalanced data”, Applied Intelligence, Vol.38, (2013), pp.315-330. 

8. Francisco Araquea, Concepción Roldán, and Alberto Salgueroa, “Factors influencing university drop out rates”,Computers &Education,Vol. 53, No. 3, (2009), pp. 563-574. 

9. O.J. Oyelade, O.O. Oladipupoand I.C. Obagbuwa, “Application of K-means clustering algorithm for prediction of student’s academic performance”, International Journal of Computer Science and Information Security, Vol.7, No.1, (2010), pp-292-295


	
