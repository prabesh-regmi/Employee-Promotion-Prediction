from django.db import models
from django.utils import timezone
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
import pickle


# Create your models here.
class Employee(models.Model):

    DEPARTMENT = [
        ('Sales & Marketing', 'Sales & Marketing'),
        ('Operations', 'Operations'),
        ('Technology', 'Technology'),
        ('R&D', 'R&D'),
        ('Procurement', 'Procurement'),
        ('Finance', 'Finance'),
        ('HR', 'HR'),
        ('Legal','Legal'),
        ('Analytics','Analytics')
    ]
    EDUCATION = [
        ("Master's & above", "Master's & above"),
        ("Bachelor's education", "Bachelor's education"),
        ("Below Secondary", "Below Secondary"),
    ]
    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    RECRUITMENT_CHANNEL = [
        ("Sourcing", "Sourcing"),
        ("Referred", "Referred"),
        ("Other", "Other"),
    ]
    NO_OF_TRAININGS = [
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
    (6,'6'),
    (7,'7'),
    (8,'8'),
    (9,'9'),
    (10,'10'),
    ]
    PREVIOS_YEAR_RATING =   [
    (1.0,'1.0'),
    (2.0,'2.0'),
    (3.0,'3.0'),
    (4.0,'4.0'),
    (5.0,'5.0'),
    ]

    AWARDS_WON = [
    (0,'0'),
    (1,'1'),
    ]


    employeeId = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    avg_training_score = models.SmallIntegerField(blank=False)
    length_of_service = models.SmallIntegerField(blank=False)
    department = models.CharField(max_length=20,choices=DEPARTMENT,blank=False)
    education = models.CharField(max_length=20,choices=EDUCATION,blank=False)
    gender = models.CharField(max_length=20,choices=GENDER)
    recruitment_channel = models.CharField(max_length=20,choices=RECRUITMENT_CHANNEL,blank=False)
    no_of_trainings = models.SmallIntegerField(choices=NO_OF_TRAININGS,blank=False)
    previous_year_rating = models.FloatField(choices=PREVIOS_YEAR_RATING,blank=False)
    awards_won = models.SmallIntegerField(choices=AWARDS_WON,blank=False)
    is_promated = models.SmallIntegerField(default=0)
    createdTime   = models.DateTimeField(default=timezone.now())

    def preditct(self,algorithm):
        test_data=self.get_test_data()
        test =[test_data]
        preditctions={}
        if algorithm=='all':
            algorithms=['DecisionTree','KNN','LogisticRegression','SupportVectorMachine','KMeansClustering']
            for a in algorithms:
                filename = r'C:\Users\Prabesh\Desktop\Project\Employee Promotion Prediction\Codes\overSample{}_model.sav'.format(a)
                # filename = staticfiles_storage.url('data/LogisticRegression_model.sav')
                loaded_model = pickle.load(open(filename, 'rb'))
                print(filename)
                if loaded_model.predict(test)[0]==0:
                    preditctions[a]='No Promotion!!'
                else:
                    preditctions[a]='Promotion!!'
            print(preditctions)
            if a=='KNN':
                self.is_promated = loaded_model.predict(test)[0]
                self.save()
            return preditctions
                
        else:
            # test=[[1,32,3.0,3,0,89,0,0,0,0,0,0,0,1,1,0,0,1],[1,46,1.0,15,0,78,0,0,0,0,0,0,0,1,0,1,0,0]]
            filename = r'C:\Users\Prabesh\Desktop\Project\Employee Promotion Prediction\Codes\overSample{}_model.sav'.format(algorithm)
            # filename = staticfiles_storage.url('data/LogisticRegression_model.sav')
            loaded_model = pickle.load(open(filename, 'rb'))
            print(filename)
            if loaded_model.predict(test)[0]==0:
                    preditctions[algorithm]='No Promotion'
            else:
                    preditctions[algorithm]='Promotion'
            print(test)
            self.is_promated = loaded_model.predict(test)[0]
            self.save()
            return preditctions

    def __str__(self):
        return str(self.employeeId)


    def get_test_data(self):
        test=[]
        test.append(self.no_of_trainings)
        test.append(self.age)
        test.append(self.previous_year_rating)
        test.append(self.length_of_service)
        test.append(self.awards_won)
        test.append(self.avg_training_score)

        department = ['Finance' , 'HR' , 'Legal', 'Operations' , 'Procurement','R&D', 'Sales & Marketing' , 'Technology' ]
        for dep in department:
            if dep == self.department:
                test.append(1)

            else:
                test.append(0)
        education = ["Below Secondary" , "Master's & above"]
        for edu in education:
            if edu == self.education:
                test.append(1)
            else:
                test.append(0)
        recruitment_channel = ["Referred" , "Sourcing"]
        for req in recruitment_channel:
            if req == self.recruitment_channel:
                test.append(1)
            else:
                test.append(0)
        return test
