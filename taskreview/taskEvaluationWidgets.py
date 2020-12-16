from IPython.core.display import display
from IPython.display import clear_output
from ipywidgets import widgets, Button, HBox, Output, VBox, Layout

class TaskEvaluationWidgets:
    """
    A class used to represent task evaluation widgets

    ...

    Attributes
    ----------
    out_txt : Output
        output widget to display text
    out_buttons : Output
        output widget to display buttons


    Methods
    -------
    create_button(description, tooltip, icon, method)
        Creates a button with the passed parameters
    create_tipp_button(method)
        Creates a tipp button
    create_check_button(method)
        Creates a check button
    create_solution_button(method)
        Creates a solution button
    display_check_and_tipp_btn()
        Displays the check and tipp button
    display_check_tipp_and_solution_button()
        Dispays the check, tipp and solution button
    display_disabled_check_and_tipp_button()
        Displays the disabled check and tipp button
    display_text_in_output_field()
        Displays the given text
    create_check_image()
        Creates the check image 
    display_check_img()
        Displays the check image
    """

    def __init__(self):
        self.out_txt = Output()
        self.out_buttons = Output()
        
        self.create_check_image()
    
    def create_button(self, description, tooltip, icon, method):
        """General method to create a button, used to create different buttons
        
        Parameters
        -------
        description : string
            Descripton that is shown on the button
        tooltip : string
            Tooltip that is shown when the mouse is hovered over the button
        icon
            Icon that is shown on the button
        method
            Method that is called when the button is clicked

        Returns
        -------
        btn : Button
            Button that has been created
        """

        btn = widgets.Button(
            description= description,
            disabled=False,
            tooltip= tooltip,
            icon = icon
        )
        btn.on_click(method)
        
        return btn
       
    ###########################################
    ### create buttons for task evaluation ####
    ###########################################
    
    def create_tipp_button(self, method):
        """Creates a tipp button

        Parameters
        -------
        method
            Method that is called when the button is clicked
        """

        self.btn_tipp = self.create_button('Tipp', 'Tipp', '', method)
    
    def create_check_button(self, method):
        """Creates a check button

        Parameters
        -------
        method
            Method that is called when the button is clicked
        """

        self.btn_check = self.create_button('Auswertung', 'Auswertung', 'check', method)
    
    def create_solution_button(self, method):
        """Creates a solution button

        Parameters
        -------
        method
            Method that is called when the button is clicked
        """
        self.btn_solution = self.create_button('Lösung', 'Lösung', '', method)
    
    def create_submit_button(self, method):
        """Creates a submit button

        Parameters
        -------
        method
            Method that is called when the button is clicked
        """

        self.btn_submit = self.create_button('Auswertung abschicken', 'Auswertung abschicken', '', method)
        self.btn_submit.layout = Layout(width = "160px")

    ############################################
    ### display buttons for task evaluation ####
    ############################################
    
    def display_check_btn(self):
        display(self.out_buttons)
        with self.out_buttons:
            clear_output()
            display(self.btn_check)
        
        display(self.out_txt)
        with self.out_txt:
            clear_output()

    def display_check_and_tipp_btn(self):
        """Displays the check and tipp button
        """

        display(self.out_buttons)
        with self.out_buttons:
            clear_output()
            display(HBox([self.btn_check, self.btn_tipp]))
        
        display(self.out_txt)
        with self.out_txt:
            clear_output()
    
    def display_check_and_solution_button(self):
        """Displays the check and solution button
        """
        with self.out_buttons:
            clear_output()
            display(HBox([self.btn_check, self.btn_solution]))
    
    def display_check_tipp_and_solution_button(self):
        """Displays the check, tipp and solution button
        """  

        with self.out_buttons:
            clear_output()
            display(HBox([self.btn_check, self.btn_tipp, self.btn_solution]))
    
    def display_submit_button(self):
        """Displays the submit button
        """

        display(self.out_buttons)
        with self.out_buttons:
            clear_output()
            display(self.btn_submit)

    def display_disabled_check_and_tipp_button(self):
        """Displays the disabled check and tipp button
        """

        self.btn_check.disabled = True
        self.btn_tipp.disabled = True
     
    ################################   
    ### display text and image #####
    ################################
            
    def display_html_in_output_field(self, text):
        """Displays html in output field

        Parameters
        -------
        text : string
            text to be displayed as html
        """
        
        html = widgets.HTML(
            value=text
        )

        with self.out_txt:
            clear_output()
            display(html)
    
    def create_check_image(self):
        """Creates the check image out of an image file
        """

        file = open("img/green_check.png", "rb")
        image = file.read()
        self.check_img = widgets.Image(
            value=image,
            format='png',
            width=30,
            height=40,
        )

    def display_check_img(self):
        """Displays the check image
        """

        with self.out_txt:
            clear_output()
            display(self.check_img)