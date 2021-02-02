"""Module that contains a class to create a learning module instance
to create tasks inside a Jupyter Notebook"""

from taskreview.task_database import TaskDatabase
from taskreview.dataframe_task import PandasDataframeTask, SparkDataframeTask
from taskreview.choice_task import SingleChoiceTask, MultipleChoiceTask
from taskreview.task_evaluation_widgets import TaskEvaluationWidgets

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
        self.database = TaskDatabase(task_db)
        self.scored_points = 0
        self.task_dict = {}
        self.score = 0
        self.task_options= {'DFP': PandasDataframeTask,
                            'DFS': SparkDataframeTask,
                            'SC': SingleChoiceTask,
                            'MC': MultipleChoiceTask,
                            }

        self.widgets = TaskEvaluationWidgets()
        self.widgets.create_submit_button(self.submit_score)

    def show_task(self, task_id, solution=None):
        """Creates a task based on the task_id and all the associated
        informations from the database

        Parameters
        -------
        task_id : int
            id of the task that should be created
        solution : object
            solution that may be submitted by the user
        """

        try:
            task_type = self.database.get_task_type(task_id)
        except TypeError as err:
            print(str(err) + "\nZu dieser Task-ID existiert keine Aufgabe.")
            return

        if not task_id in self.task_dict:
            task = self.task_options[task_type](self.database, task_id)
            task.evaluate_task(solution)
            try:
                self.task_dict[task_id] = task
            except UnboundLocalError as err:
                print(str(err) + "\nFür diese Aufgabe wurde kein Task-Type \
                hinterlegt.")
                return
        else:
            self.task_dict[task_id].evaluate_task(solution)


    def get_scored_points(self):
        """Gets the number of correct answers in the learning module
        (Can be carried out at any point in the learning module)

        Returns
        -------
        int
            number of correct answered exercises
        """
        self.scored_points = 0

        for task in self.task_dict.values():
            if isinstance(task, (SingleChoiceTask, MultipleChoiceTask)):
                self.scored_points += task.calculate_scored_points()
            else:
                self.scored_points += task.calculate_scored_points(solution_btn_available=True)

        percentage_scored_points = (100/ len(self.task_dict)) * self.scored_points

        return percentage_scored_points

    ####################
    ### Submit score ###
    ####################

    def display_submit_button(self):
        """Displays the button needed to submit the score to
        the learning platform
        """
        self.widgets.display_submit_button()

    def submit_score(self, button):
        """Submits the overall score to the learning platform
        """
        self.score = self.get_scored_points()
