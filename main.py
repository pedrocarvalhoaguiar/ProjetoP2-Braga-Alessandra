from controller import Controlador
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
if __name__ == '__main__':
    controlador = Controlador()
    controlador.gerenciador.gerBiometria.compararBiometria(filedialog.askopenfilename())
    