"""Module that contains classes to create choice tasks
(single and multiple choice)"""

from taskreview.choice_widgets import ChoiceWidgets
from taskreview.task import Task

class SingleChoiceTask(Task):
    """
    A class to represent a single choice task

    ...

    Attributes
    ----------
    single_choice_widgets : ChoiceWidgets
        class that contains widgets for single choice tasks


    Methods
    -------
    check_solution(button)
        Checks the solution when the check button is clicked
    evaluate_task()
        Evaluates the task
    display_sc_buttons()
        Displays the single choice buttons
    """

    def __init__(self, db_conn, task_id):
        super().__init__(db_conn, task_id)
        self.sc_widgets = ChoiceWidgets(db_conn, task_id)

    def check_solution(self, button):
        """Checks if the solution the user chose is correct

        Parameters
        ----------
        button : Button
            Button that has been clicked to execute this method
        """
        if self.sc_widgets.options[self.sc_widgets.sc_btns.value] \
            == self.solution:

            self.is_task_answered_correctly = True
            self.display_img_correct()
            self.display_disabled_buttons()
        else:
            self.display_text(self.txt_incorrect_answer)

            # increment counter of tries
            self.cnt_false_answers.increment()


    def evaluate_task(self, solution):
        """Makes it possible to evaluate the task by displaying the buttons
        """
        self.display_sc_buttons()
        self.display_buttons()

    def display_sc_buttons(self):
        """Displays the single choice, check and tipp buttons
        """
        self.sc_widgets.display_single_choice_buttons()

class MultipleChoiceTask(Task):
    """
    A class to represent a single choice task

    ...

    Attributes
    ----------
    mc_widgets : ChoiceWidgets
        class that contains widgets for single choice tasks


    Methods
    -------
    check_solution(button)
        Checks the solution when the check button is clicked
    evaluate_task()
        Evaluates the task
    display_mc_buttons()
        Displays the multiple choice buttons
    """

    def __init__(self, db_conn, task_id):
        super().__init__(db_conn, task_id)
        self.mc_widgets = ChoiceWidgets(db_conn, task_id)

    def check_solution(self, button):
        """Checks if the solution the user chose is correct

        Parameters
        ----------
        button : Button
            Button that has been clicked to execute this method
        """
        if self.mc_widgets.get_selected_options() == self.solution:
            self.is_task_answered_correctly = True
            self.display_img_correct()
            self.display_disabled_buttons()
        else:
            self.display_text(self.txt_incorrect_answer)

            # increment counter of tries
            self.cnt_false_answers.increment()

    def evaluate_task(self, solution):
        """Makes it possible to evaluate the task by displaying the buttons
        """
        self.display_mc_buttons()
        self.display_buttons()

    def display_mc_buttons(self):
        """Makes it possible to evaluate the task by displaying the buttons
        """
        self.mc_widgets.display_multiple_choice_buttons()
