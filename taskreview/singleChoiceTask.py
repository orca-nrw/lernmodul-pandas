from IPython.core.display import display

from taskreview.singleChoiceWidgets import SingleChoiceWidgets
from taskreview.task import Task

class SingleChoiceTask(Task):
    """
    A class to represent a single choice task

    ...

    Attributes
    ----------
    single_choice_widgets : SingleChoiceWidgets
        class that contains widgets for single choice tasks
    

    Methods
    -------
    check_solution(button)
        Checks the solution when the check button is clicked
    evaluate_task()
        Evaluates the task
    display_sc_buttons()
        Displays the single choice buttons
    get_correct_answer_index()
        Gets the index of the correct answer in the options
    """

    def __init__(self, db_conn, task_id):
        super().__init__(db_conn, task_id)
        self.single_choice_widgets = SingleChoiceWidgets(db_conn, task_id)


    def check_solution(self, button):
        """Checks if the solution the user chose is correct

        Parameters
        ----------
        button : Button
            Button that has been clicked to execute this method
        """

        a = int(self.single_choice_widgets.choice_btns.value)
        
        if a == self.get_correct_answer_index():
            self.is_task_answered_correctly = True
            self.display_img_correct()
            self.display_disabled_buttons()
        else:
            self.display_text(self.txt_incorrect_answer)
            
            # increment counter of tries
            self.cnt_false_answers.increment()
        
        
    def evaluate_task(self):
        """Makes it possible to evaluate the task by displaying the buttons
        """
        self.display_sc_buttons()
        self.display_buttons()

    def display_sc_buttons(self):
        """Displays the single choice, check and tipp buttons
        """

        self.single_choice_widgets.display_single_choice_buttons()

    def get_correct_answer_index(self):
        """Gets the index of the correct answer in the options

        Returns
        -------
        int
            Index of the solution in the options list
        """
        
        try:
            return self.single_choice_widgets.get_index_of_option(self.get_solution())
        except:
            pass  # TODO kann hier ein Fehler entstehen?