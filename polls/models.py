import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model):
    """
    Model representing a question in the polls app.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time when the question was published.
        end_date (datetime, optional): The end date and time for voting (optional).
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=False)
    end_date = models.DateTimeField('end date for voting', null=True, blank=True)


    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        """
        Check if the question was published within the last day.

        Returns:
            bool: True if the question was published recently, False otherwise.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def is_published(self):
        """
        Check if the question is currently published.

        Returns:
            bool: True if the question is published, False otherwise.
        """
        current_local_time = timezone.localtime(timezone.now())
        return current_local_time >= self.pub_date

    def can_vote(self):
        """
        Check if it is currently possible to vote on the question.

        Returns:
            bool: True if voting is allowed, False otherwise.
        """
        now = timezone.now()
        if self.end_date:
            return self.pub_date <= now <= self.end_date
        else:
            return self.pub_date <= now
        
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    
    

class Choice(models.Model):
    """
    Model representing a choice for a question in the polls app.

    Attributes:
        question (Question): The question associated with this choice.
        choice_text (str): The text of the choice.
        votes (int): The number of votes for this choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text