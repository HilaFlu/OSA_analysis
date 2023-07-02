import tkinter as tk
from tkinter import filedialog
from Experiment_Data_Holder import ExperimentData

class LoadFileWindow:
    def __init__(self, experiment_data):
        self.file_path = ""
        self.file_contents = ""
        self.session_number = ""
        self.experiment_data = experiment_data
        self.load_file_window = tk.Tk()
        self.load_file_window.title("Load File")
        self.load_file_window.geometry("450x450")

        self.file_path_label = tk.Label(self.load_file_window, text="File Path:")
        self.file_path_label.pack(pady=15)
        
        self.file_path_text = tk.Text(self.load_file_window, height=1, width=40)
        self.file_path_text.pack()
        
        self.upload_button = tk.Button(self.load_file_window, text="Upload .txt File", command=self.upload_file)
        self.upload_button.pack(pady=20)
        
        self.session_number_label = tk.Label(self.load_file_window, text="Session Number:")
        self.session_number_label.pack(pady=10)

        self.session_number_entry = tk.Entry(self.load_file_window)
        self.session_number_entry.pack()

        
        self.file_contents_label = tk.Label(self.load_file_window, text="File Contents:")
        self.file_contents_label.pack(pady=10)

        self.file_contents_text = tk.Text(self.load_file_window, height=5, width=40)
        self.file_contents_text.pack()

        self.load_button = tk.Button(self.load_file_window, text="Load File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.proceed_button = tk.Button(self.load_file_window, text="Proceed >>", command=self.load_file_window.destroy)
        self.proceed_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.load_file_window.mainloop()

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.rtf")])
        if file_path:
            self.file_path = file_path
            self.file_path_text.delete("1.0", tk.END)
            self.file_path_text.insert(tk.END, self.file_path)

            with open(file_path, "r") as file:
                self.file_contents = file.read()
                self.file_contents_text.delete("1.0", tk.END)
                self.file_contents_text.insert(tk.END, self.file_contents)
                self.file_contents_text.config(state=tk.DISABLED)
        self.experiment_data.path = file_path
    def load_file(self):
        self.session_number = self.session_number_entry.get()
        experiment_data = self.experiment_data
        experiment_data.load_session_number(self.session_number)
        experiment_data.load_sess_path(self.experiment_data.path)
        print("file successfully Loaded")
    

# if __name__ == '__main__':
#     Experiment_Data = ExperimentData()
#     load_file_window = LoadFileWindow(Experiment_Data)
#     # file_path = load_file_window.file_path
#     # session_number = load_file_window.session_number
#     print("File Path:", Experiment_Data.path)
#     print("Session Number:", Experiment_Data.session_number)
