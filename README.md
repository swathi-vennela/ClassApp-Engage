# ClassApp-Engage
#### A platform where the students and teachers can stay engaged with the regular academic activities and discover a new way of learning during the pandemic.
This application supports two types of users : Teacher and the Student. <br>
A new user can sign-up as a teacher or as a student based on his role.

## Run the project

1. Clone the repository
```
git clone https://github.com/swathi-vennela/ClassApp-Engage.git 
```
2. Go into the classApp directory and install the requirements.txt
```
cd classApp
pip install -r requirements.txt
```
4. Run the server
```
python manage.py runserver
```
On the browser http://127.0.0.1:8000/ will open the application

## Modules
The main modules in this application are: <br>
1. Quiz module with auto-evaluation
2. Student discussion forum

The other modules include <br>
3. User registration, authentication <br>
4. User dashboard 

## Quiz module
### On the Student's end
A student can view all the quizzes hosted by his teachers on the Quiz home page, and attempt them. 

![Alt text](/images/uf.png?raw=true "Optional Title")

Once the student marks the answer from the options for each question and clicks on submit, his responses will be auto-evaluated, and the results will be shown.
#### NOTE
1. Auto-evaluation works on the marking scheme of awarding 10 marks for a correct response, and no marks for an incorrect response
2. Each question is compulsory to be attempted

![Alt text](/images/result.png?raw=true "Optional Title")

The response sheet of this submission will show up on this student's profile page as well as the teacher's profile page (the teacher who has hosted this quiz).
<b>Once a student attempts a quiz, he will not be able to take the same quiz again, an alert message saying that he has already attempted the quiz pops up.</b>

### On the Teacher's end
A teacher can host a new quiz. This is involves, creating a new quiz, and adding questions into the quiz.
On the quiz-home page, the teacher will be able to view all the quizzes hosted by all teachers. On the teacher's profile page, he can view all the quizzes hosted by him, and check the result obtained by each student for that quiz. Additionally, he can also view the response sheet of a particular student to check the correct and wrong answers marked by him. 


![Alt text](/images/teacher-profile.png?raw=true "Optional Title")

![Alt text](/images/quiz-results.png?raw=true "Optional Title")

![Alt text](/images/response-sheet.png?raw=true "Optional Title")

## Discussion forum
### On Student's end
Students can create a post and reply on any post. Post content can be any "text data". 
### On Teacher's end
Teachers can only view the posts and the replies, but add any post or reply. This discussion forum is meant for student's discussions only.

## Tech stack 
1. Django web framework for backend
2. SQLite database
3. HTML, CSS, Javascript for frontend templates

### [Video demo](https://drive.google.com/file/d/14YxztlSIMWiGe0Qb1GpVf0a53mqx0fTT/view?usp=sharing)

