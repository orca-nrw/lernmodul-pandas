from IPython.core.display import display

from taskreview.task import Task

class DataframeTask(Task):
    """
    A class used to represent a dataframe task

    ...

    Attributes
    ----------


    Methods
    -------
    check_solution(button)
        Checks the solution when the check button is clicked
    evaluate_task(df)
        Evaluates the task based on the submitted solution
    """

    def __init__(self, db_conn, task_id):
        super().__init__(db_conn, task_id)
    
    def check_solution(self, button):
        """Checks if the solution of the user is correct

        Parameters
        ----------
        button: Button
            Button that has been clicked to execute this method
        """

        if self.solution.equals(self.user_solution):
            self.is_task_answered_correctly = True
            self.display_img_correct()
            self.display_disabled_buttons()
        else:
            self.display_text(self.txt_incorrect_answer)
            
            # increment counter of tries
            self.cnt_false_answers.increment()
                
            if self.cnt_false_answers.get_value() >= 3:
                self.display_solution_btn()                   
            
    def evaluate_task(self, df):
        """Makes it possible to evaluate the task by displaying the buttons. Display user solution.

        Parameters
        ----------
        df : pandas.DataFrame
            Dataframe that the user submitted
        """

        display(df)
        self.user_solution = df
        self.display_buttons()




class SparkDataframeTask(DataframeTask):
    """
    A class used to represent a spark dataframe task

    ...

    Attributes
    ----------


    Methods
    -------
    evaluate_task(df)
        Evaluates the task based on the submitted solution
    """

    def __init__(self, db_conn, task_id):
        super().__init__(db_conn, task_id)

    def evaluate_task(self, df):
        """Makes it possible to evaluate the task by displaying the buttons. Shows user solution as spark dataframe.

        Parameters
        ----------
        df : pyspark.sql.DataFrame
            Dataframe that the user submitted
        """

        df.show()
        self.user_solution = df.toPandas()
        self.display_buttons()