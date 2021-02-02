"""Module that contains a class to create single and
multiple choice widgets"""

from IPython.core.display import display
from IPython.display import clear_output
from ipywidgets import widgets, Output

class ChoiceWidgets:
    """
    A class used to represent single choice widgets

    ...

    Attributes
    ----------
    options : list
        list of options to choose from when answering the question
    choice_btns : RadioButtons
        buttons to choose an answer


    Methods
    -------
    get_options(db_conn, task_id)
        Gets the options from database
    create_single_choice_buttons(options)
        Creates the single choice buttons
    create_multiple_choice_buttons(options)
        Creates the multiple choice buttons
    display_single_choice_buttons()
        Displays the single choice buttons
    display_multiple_choice_buttons()
        Displays the multiple choice buttons
    get_selected_options()
        Returns the selected options for multiple choice tasks
    """

    def __init__(self, db_conn, task_id):
        self.out_choice = Output()

        # information about task
        self.options = self.get_options(db_conn, task_id)

        # init buttons to choose from
        self.sc_btns = self.create_single_choice_buttons(self.options)
        self.mc_btns = self.create_multiple_choice_buttons(self.options)


    def get_options(self, db_conn, task_id):
        """Gets the options for the task from database

        Parameters
        -------
        cd_conn : Connection
            Connection to the database
        task_id : int
            id of the task

        Returns
        -------
        list
            options for the task
        """

        return db_conn.get_options_for_task(task_id)

    def create_single_choice_buttons(self, options, value=0):
        """Creates radio buttons with the passed options

        Parameters
        -------
        options : list
            list of options to create radio buttons from
        value : int
            represents the selected element of the options
            (preset to 0, first element is selected)

        Returns
        -------
        btns : Buttons
            radio buttons that can be used for a single choice task
        """

        radio_options = [(words, i) for i, words in enumerate(options)]
        layout = widgets.Layout(width='auto', height='auto')

        btns = widgets.RadioButtons(
            options=radio_options,
            description='',
            disabled=False,
            indent=False,
            value=value,
            layout=layout
        )

        return btns

    def create_multiple_choice_buttons(self, options):
        """Creates Checkboxes with the answers for multiple choice questions

        Parameters
        -------
        options : list
            list of options to create radio buttons from

        Returns
        -------
        options_widget : VBox with Checkboxes
            Checkboxes in a VBox for display
        """
        layout = widgets.Layout(width='auto', height='auto')

        options_dict = {option: widgets.Checkbox(description=option, \
            indent=False, value=False, layout=layout) for option in options}
        options = [options_dict[option] for option in options]
        options_widget = widgets.VBox(options)

        return options_widget

    def display_single_choice_buttons(self):
        """Displays the single choice buttons
        """

        display(self.out_choice)

        with self.out_choice:
            clear_output()
            display(self.sc_btns)

    def display_multiple_choice_buttons(self):
        """Displays the multiple choice buttons
        """

        display(self.out_choice)

        with self.out_choice:
            clear_output()
            display(self.mc_btns)

    def get_selected_options(self):
        """Returns the selected options for multiple choice tasks
        """

        selected_options = [w.description for w in self.mc_btns.children if w.value]
        return selected_options
