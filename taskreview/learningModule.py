from taskreview.taskDatabase import TaskDatabase
from taskreview.counter import Counter
from taskreview.dataframeTask import DataframeTask, SparkDataframeTask
from taskreview.singleChoiceTask import SingleChoiceTask
from taskreview.taskEvaluationWidgets import TaskEvaluationWidgets

class LearningModule:
    """
    A class used to represent a learning module

    ...

    Attributes
    ----------
    task_db: Database-File
        Database file representing exercises of each learning module
    db: Database
        Database object on which actions can be performed
    num_correct_answered: Counter
        counter that counts the correct answers
    taskList: list
        list that is used to collect all tasks of a learning module
    

    Methods
    -------
    show_task(task_id, solution)
        Creates a task based on task_id and database
    get_num_correct_answered()
        Gets the number of correct answers
    submit_score()
        Submits the overall score to the learning platform
    """

    def __init__(self, task_db):
        self.db = TaskDatabase(task_db)
        self.num_correct_answered = Counter()
        self.taskList = []

        self.widgets = TaskEvaluationWidgets()
        self.widgets.create_submit_button(self.submit_score)

    def show_task(self, task_id, solution=0):
        """Creates a task based on the task_id and all the associated informations
        from the database

        Parameters
        -------
        task_id : int
            id of the task that should be created
        solution : object
            solution that may be submitted by the user
        """
        task_type = self.db.get_task_type(task_id)
        if task_type == "DFP":
            task = DataframeTask(self.db, task_id)
            task.evaluate_task(solution)
        elif task_type == "DFS":
            task = SparkDataframeTask(self.db, task_id)
            task.evaluate_task(solution)
        elif task_type == "SC":
            task = SingleChoiceTask(self.db, task_id)
            task.evaluate_task()
        else:
            print("Es wurde kein Task-Type hinterlegt")
            return
        
        self.taskList.append(task)

    def get_num_correct_answered(self):
        """Gets the number of correct answers in the learning module
        (Can be carried out at any point in the learning module)

        Returns
        -------
        int
            number of correct answered exercises
        """
        for task in self.taskList:
            if task.is_task_answered_correctly:
                self.num_correct_answered.increment()
        
        return self.num_correct_answered.get_value()
    
    ####################
    ### Submit score ###
    ####################

    def display_submit_button(self):
        """Displays the button needed to submit the score to the learning platform
        """
        self.widgets.display_submit_button()

    # TODO: add needed functionality to submit score
    def submit_score(self, button):
        """Submits the overall score to the learning platform
        """
        self.score = self.get_num_correct_answered()