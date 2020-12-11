from abc import ABC
from IPython.core.display import display

from taskreview.taskEvaluationWidgets import TaskEvaluationWidgets
from taskreview.counter import Counter
from taskreview.taskDatabase import TaskDatabase

class Task(ABC):
    """
    A class used to represent a task

    ...

    Attributes
    ----------
    widgets : TaskEvaluationWidgets
        class that contains widgets for task evaluation
    solution : object
        solution of the task
    solution_as_text : str
        solution that should be displayed when the solution button is hit
    tipp : str
        tipp that helps the user to edit the task
    txt_incorrect_answer : str
        text that is shown when the user solution was wrong
    user_solution : object
        solution that the user created for a task
    cnt_false_answers : Counter
        counter that counts the false answers of a user for a task
    is_task_answered_correctly : Boolean
        displays if a user has already edited the task correctly 
    db: Database
        Database connection to get information about tasks
    

    Methods
    -------
    get_solution()
        Gets the solution from database
    get_solution_as_text()
        Gets the solution as text from database
    get_tipp()
        Gets the tipp for the task from database
    print_solution(button)
        Prints the solution when the solution button is clicked
    print_tipp(button)
        Prints the tipp when the tipp button is clicked
    display_buttons()
        Displays the check and tipp button
    display_colution_btn():
        Displays the check, tipp and solution button
    display_img_correct():
        Displays the check image 
    display_text(text):
        Displays the given text
    check_solution():
        Abstract method that checks the user solution
    evaluate_task():
        Abstract method that evaluates the task
    
        
    """
    
    def __init__(self, db_conn, task_id):
        self.db_conn = db_conn
        # id of task
        self.task_id = task_id
        
        # init buttons for evaluation of task
        self.widgets = TaskEvaluationWidgets()
        self.widgets.create_tipp_button(self.print_tipp)
        self.widgets.create_check_button(self.check_solution)
        self.widgets.create_solution_button(self.print_solution)
        
        # information about task
        self.solution = self.get_solution()
        self.solution_as_text = self.get_solution_as_text()
        self.tipp = self.get_tipp()

        # text for incorrect answers
        self.txt_incorrect_answer = "Leider nicht korrekt. Bitte versuche es erneut."

        # user specific information
        self.user_solution = None
        self.cnt_false_answers = Counter()
        self.is_task_answered_correctly = False   

    #####################################
    ### get information from database ###
    #####################################

    def get_solution(self):
        """Gets the solution of a task from database
        
        Returns
        -------
        object
            solution of the task with the respective data type
        """

        return self.db_conn.get_solution_for_task(self.task_id)


        
    def get_solution_as_text(self):
        """Gets the solution of a task as text from database. This solution should be displayed
        if the user clicks on the solution button. Therefore it should display the code that 
        leads to the solution.
        
        Returns
        -------
        str
            solution of the task as code
        """

        return self.db_conn.get_solution_as_text(self.task_id)
    
    def get_tipp(self):
        """Gets the tipp of a task from database
        
        Returns
        -------
        str
            tipp of the task
        """

        return self.db_conn.get_tipp_for_task(self.task_id)

    ###########################
    ### methods for buttons ###
    ###########################

    def print_solution(self, button):
        """Prints the solution of a task as text/ code
        
        Parameters
        -------
        button : Button
            Button that has been clicked to execute this method

        """

        self.widgets.display_text_in_output_field(self.solution_as_text)
        
    def print_tipp(self, button):
        """Prints the tipp of a task
        
        Parameters
        -------
        button : Button
            Button that has been clicked to execute this method

        """

        self.widgets.display_text_in_output_field(self.tipp)    
    
    ################################
    ### display buttons for task ###
    ################################

    def display_buttons(self):
        """Displays the buttons needed for task evaluation
        """

        self.widgets.display_check_and_tipp_btn()
        
    def display_solution_btn(self):
        """Adds a solution button next to the check and tipp button
        """

        self.widgets.display_check_tipp_and_solution_button()
    
    def display_disabled_buttons(self):
        """Displays the disabled check and tipp buttons
        """

        self.widgets.display_disabled_check_and_tipp_button()

    ###############################
    ### display task evaluation ###
    ###############################

    def display_img_correct(self):
        """Displays the check image 
        """

        self.widgets.display_check_img()
        
    def display_text(self, text):
        """Displays the given text
        
        Parameters
        -------
        text : str
            Text that should be displayed

        """

        self.widgets.display_text_in_output_field(text)
    
    ########################
    ### abstract methods ###
    ########################

    def check_solution(self, button): 
        """Checks if the solution of the user is correct
        
        Parameters
        -------
        button : Button
            Button that has been clicked to execute this method

        """

        pass
    
    def evaluate_task(self):
        """Makes it possible to evaluate a task
        """

        pass
    