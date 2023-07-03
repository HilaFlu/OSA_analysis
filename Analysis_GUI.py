import tkinter as tk
from tkinter import ttk
class AnalysisGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Analysis GUI")
        self.root.geometry("940x550")

        # Left Side (Experiment Analysis)
        self.experiment_frame = tk.Frame(self.root, padx=10, pady=10)
        self.experiment_frame.grid(row=0, column=0, sticky="nsew")
        
        
        self.Experiment_label = tk.Label(self.experiment_frame, text = "Experiemnt Analysis Options" )
        self.Experiment_label.grid(row = 0 , column = 1 ,padx = 5 , pady = 20)
        
        # Experiment Analysis Buttons
        self.experiment_button1 = tk.Button(self.experiment_frame, text="Average Intake", width = 22)
        self.experiment_button1.grid(row=2, column=1, pady=5)

        self.experiment_button2 = tk.Button(self.experiment_frame, text="Metric per session" ,width = 22)
        self.experiment_button2.grid(row=5, column=1, pady=10)

        self.experiment_button3 = tk.Button(self.experiment_frame, text="Group Presses" ,width = 22)
        self.experiment_button3.grid(row=8, column=1, pady=5)

        # Experiment Analysis Text Entries 
        ##Entries for exp analysis 1
        self.experiment_entry11 = tk.Entry(self.experiment_frame)## file path
        self.experiment_entry11.grid(row=4, column=0,padx=5, pady=5)
        self.experiment_entry12 = tk.Entry(self.experiment_frame)## Group list of floats 
        self.experiment_entry12.grid(row=4, column=1,padx=5, pady=5)
        self.experiment_sex_combobox1 = ttk.Combobox(self.experiment_frame, values=[ "Male" , "Female"] )
        self.experiment_sex_combobox1.grid(row=4, column=2,padx=5, pady=5)
        
        self.experiment_path_label1 = tk.Label(self.experiment_frame, text = "Enter Path:")## file path
        self.experiment_path_label1.grid(row=3, column=0,padx=5, pady=5)
        self.experiment_group_label1 = tk.Label(self.experiment_frame , text = "Enter Groups #,#") ## Group list of floats 
        self.experiment_group_label1.grid(row=3, column=1,padx=5, pady=5)
        self.experiment_sex_combobox1_label1 = tk.Label(self.experiment_frame, text = "Sex:" )
        self.experiment_sex_combobox1_label1.grid(row=3, column=2,padx=5, pady=5)

        ##Entries for exp analysis 2 
        self.experiment_entry21 = tk.Entry(self.experiment_frame,width= 15)#path 
        self.experiment_entry21.grid(row=7, column=0,padx=3, pady=5)
        self.experiment_metric_combobox2 = ttk.Combobox(self.experiment_frame, values=[ "reward","head", "left_lever", "right_lever"],width= 8 ) ## metric exp analysis 2
        self.experiment_metric_combobox2.grid(row=7, column=1,padx=3, pady=5 ,sticky=tk.W)
        self.experiment_sex_combobox2 = ttk.Combobox(self.experiment_frame, values=[ "Male" , "Female"] ,width= 10)##sex animals 2 
        self.experiment_sex_combobox2.grid(row=7, column=1,padx=3, pady=5,sticky=tk.E)
        self.experiment_entry24 = tk.Entry(self.experiment_frame ,width= 15)##list of groups
        self.experiment_entry24.grid(row=7, column=2,padx=6, pady=5 ,sticky=tk.W)
        
        self.experiment_path_label2 = tk.Label(self.experiment_frame , text = "Enter path:")## file path
        self.experiment_path_label2.grid(row=6, column=0,padx=3, pady=5)
        self.experiment_metric_combobox2_label2 = tk.Label(self.experiment_frame , text = "Choose Metric:")## Group list of floats 
        self.experiment_metric_combobox2_label2.grid(row=6, column=1,padx=3, pady=5 ,sticky=tk.W)
        self.experiment_sex_combobox1_label2 = tk.Label(self.experiment_frame, text = "Sex:")
        self.experiment_sex_combobox1_label2.grid(row=6, column=1,padx=5, pady=5,sticky=tk.NE)
        self.experiment_group_Label2 = tk.Label(self.experiment_frame , text = "Enter Groups (#,#)")## file path
        self.experiment_group_Label2.grid(row=6, column=2,padx=6, pady=5 ,sticky=tk.W)
        
        
        ##Entries for exp analysis 3
        self.experiment_entry31 = tk.Entry(self.experiment_frame)##group for exp 2 
        self.experiment_entry31.grid(row=10, column=0, pady=5)
        self.experiment_entry32 = tk.Entry(self.experiment_frame)##path for exp3
        self.experiment_entry32.grid(row=10, column=1, padx=5 ,pady=5 , sticky=tk.E)
        
        ##labels for exp 3 
        self.experiment_path_label3 = tk.Label(self.experiment_frame , text = "Enter Path:" )##group for exp 2 
        self.experiment_path_label3.grid(row=9, column=0, pady=5)
        self.experiment_group_label3= tk.Label(self.experiment_frame , text = "Enter Groups(#,#)")##path for exp3
        self.experiment_group_label3.grid(row=9, column=1, padx=5 ,pady=5 , sticky=tk.E)
        
        
        ##################################################################
        # this the right side for Anamil Based analysis.
        
        # Right Side (Animal Analysis)
        self.animal_frame = tk.Frame(self.root, padx=10, pady=10)
        self.animal_frame.grid(row=0, column=3, sticky="nsew")

        # Animal Analysis Buttons 
        
        self.animal_text_label = tk.Label(self.animal_frame , text = " Animal experiment")
        self.animal_text_label.grid(row= 0 , column = 1 , pady=10 , padx = 10)
        
        
        ### Button for analysis #1 - Total alcohol Intake:
        
        self.animal_button1 = tk.Button(self.animal_frame, text="Total Alcohol Intake" , width = 22)
        self.animal_button1.grid(row=1, column=1, pady=5)

        ## Aniaml Analysis 1 labels
        self.animal_path_label1 = tk.Label(self.animal_frame, text = "Enter Path:" )##group for exp 2 
        self.animal_path_label1.grid(row=2, column=0, pady=5)
        self.animal_label1= tk.Label(self.animal_frame , text = "Choose Animal:")##path for exp3
        self.animal_label1.grid(row=2, column=1, padx=5 ,pady=5 , sticky=tk.N)
        ##Aniaml Analysis 1 Entries
        self.animal_entry11 = tk.Entry(self.animal_frame)##Entry for path 
        self.animal_entry11.grid(row=3, column=0, pady=5)
        self.animal_entry12 = tk.Entry(self.animal_frame)## commbox for animal ID
        self.animal_entry12.grid(row=3, column=1, pady=5)
        
        

        
        # Animal Analysis 2 button
  
        
        self.animal_button2 = tk.Button(self.animal_frame, text="Alcohol Intake /session" ,width = 22)
        self.animal_button2.grid(row=4, column=1, pady=5)
         
         
          #Animal Analysis 2 labels
        self.animal_path_label2 = tk.Label(self.animal_frame, text = "Enter Path:" )##group for exp 2 
        self.animal_path_label2.grid(row=5, column=0, pady=5)
        self.animal_label2= tk.Label(self.animal_frame , text = "Choose Animal:")##path for exp3
        self.animal_label2.grid(row=5, column=1, padx=5 ,pady=5 , sticky=tk.N)
        self.animal_sess_num2= tk.Label(self.animal_frame , text = "Enter Session #:")##path for exp3
        self.animal_sess_num2.grid(row=5, column=2, padx=5 ,pady=5 , sticky=tk.N)
         
         # Animal Analysis 2 entries
        self.animal_path_entry2 = tk.Entry(self.animal_frame)##Entry for path 
        self.animal_path_entry2.grid(row=6, column=0, pady=5)
        self.animal_entry2 = tk.Entry(self.animal_frame)## commbox for animal ID
        self.animal_entry2.grid(row=6, column=1, pady=5)        
        self.animal_sess_num_entry2 = tk.Entry(self.animal_frame)## entry for session
        self.animal_sess_num_entry2.grid(row=6, column=2, pady=5) 
        
        
        
        
        # Animal Analysis3 button
        
        
        self.animal_button3 = tk.Button(self.animal_frame, text="Metrics")
        self.animal_button3.grid(row=7, column=1, pady=5)

        
          # Animal Analysis 2 labels
        self.animal_path_label3 = tk.Label(self.animal_frame, text = "Enter Path:" )##path for ani  3
        self.animal_path_label3.grid(row=8, column=0, pady=5)
        self.animal_label3= tk.Label(self.animal_frame , text = "Choose Metric:")##animal for ani3 
        self.animal_label3.grid(row=8, column=1, padx=5 ,pady=5 , sticky=tk.N)
        self.animal_metric3= tk.Label(self.animal_frame , text ="Choose Animal:")##metric for ani 3
        self.animal_metric3.grid(row=8, column=2, padx=5 ,pady=5 , sticky=tk.N)
         
        
        
        # Animal Analysis 3 entries
        self.animal_path_entry3 = tk.Entry(self.animal_frame)
        self.animal_path_entry3.grid(row=9, column=0, pady=5)
        self.animal_metric_combobox = ttk.Combobox(self.animal_frame, values=[ "reward","head", "left_lever", "right_lever"] )
        self.animal_metric_combobox.grid(row=9, column=1,padx=5, pady=5)
        self.animal_entry3 = tk.Entry(self.animal_frame)## Animal entry box
        self.animal_entry3.grid(row=9, column=2, pady=5)
     
     
            #####           #######                 #######         #######
            
            
        # Animal Analysis4 button "Average lever presses""
     
        self.animal_button4 = tk.Button(self.animal_frame, text="Average lever presses" , width = 22)
        self.animal_button4.grid(row=10, column=1, pady=5)

        

        self.animal_path_label4 = tk.Label(self.animal_frame, text = "Enter Path:" )##group for exp 2 
        self.animal_path_label4.grid(row=11, column=0, pady=5)
        self.animal_label4= tk.Label(self.animal_frame , text = "Choose Animal:"  )##path for exp3
        self.animal_label4.grid(row=11, column=1, padx=5 ,pady=5 , sticky=tk.N)
        
        
        
         # Animal Analysis 4 labels
         
        # self.animal_path_label4 = tk.Label(self.animal_frame , text = "Enter Path:")##Entry for path 
        # self.animal_path_label4.grid(row=12, column=0, pady=5)
        # self.animal_label4 = tk.Label(self.animal_frame , text = "Choose Animal:")## commbox for animal ID
        # self.animal_label4.grid(row=12, column=1, pady=5)
         
         
        
         # Animal Analysis 4 entries
        self.animal_entry41 = tk.Entry(self.animal_frame)
        self.animal_entry41.grid(row=12, column=0, pady=5)
        self.animal_entry42 = tk.Entry(self.animal_frame)
        self.animal_entry42.grid(row=12, column=1, pady=5)
  

        self.root.mainloop()


if __name__ == '__main__':
    analysis_gui = AnalysisGUI()
