from IPython.core.display import display
from IPython.display import clear_output
from ipywidgets import widgets, Output

class SingleChoiceWidgets:
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
    create_choice_buttons(db_conn, task_id)
        Creates the single choice buttons
    display_single_choice_buttons(options, value)
        Displays the single choice buttons
    get_index_of_option(option)
        Gets the index of the chosen option in the options
    """

    def __init__(self, db_conn, task_id):
        self.out_single_choice = Output()

        # information about task
        self.options = self.get_options(db_conn, task_id)
        
        # init buttons to choose from
        self.choice_btns = self.create_choice_buttons(self.options)
    
    
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

    def create_choice_buttons(self, options, value=0):
        """Creates radio buttons with the passed options

        Parameters
        -------
        options : list
            list of options to create radio buttons from
        value : int
            represents the selected element of the options (preset to 0, first element is selected)
        
        Returns
        -------
        btns : Buttons
            radio buttons that can be used for a single choice task
        """

        radio_options = [(words, i) for i, words in enumerate(options)]
        
        btns = widgets.RadioButtons(
            options=radio_options,
            description='',
            disabled=False,
            indent=False,
            value=value
        )
        
        return btns

    def display_single_choice_buttons(self):
        """Displays the single choice buttons
        """

        display(self.out_single_choice)
        
        with self.out_single_choice:
            clear_output()
            display(self.choice_btns)
            
    def get_index_of_option(self, option):
        """Gets the index of an option in the options list

        Parameters
        -------
        option : object
            option from which the index is searched for in the options
        
        Returns
        ------
        int
            index of the option in the options
        """
        
        return self.options.index(option)