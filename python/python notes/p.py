import nbformat
import os

# Path to the folder containing the notebook files
folder_path = r'C:\Users\lalkr\OneDrive\Desktop\New folder\coding\python\python notes'
merged_file = os.path.join(folder_path, 'notes_python.ipynb')

# List of notebook files to merge
notebook_files = [
    '01_Python_Introduction_File.ipynb',
    '02_Python Literals, Identifiers and Data Type.ipynb',
    '03_Float_Boolean_Complex_Data_Type.ipynb',
    '04_Sequence Data Type Cateogry.ipynb',
    '05_Type_Casting_In_Python.ipynb',
    '06_bytes_bytearray_range.ipynb',
    '07_List_Data_Type.ipynb',
    '08_Tuple_Data_Type.ipynb',
    '09_Set_Data_Type.ipynb',
    '10_Dictionary_Data_Type.ipynb',
    '11_Operators_In_Python.ipynb',
    '12_Control_Flow_Structure.ipynb',
    '13_While_Loop_In_Python.ipynb',
    '14_For_Loop_And_Transfer_Flow_Statements.ipynb',
    '15_Function_In_Python.ipynb',
    '16_Types_of_Arguments_in_Python.ipynb',
    '17_Python_Lambda_and_Special_Function.ipynb',
    '18_Python_Recusrive_Function.ipynb',
    '19_Exception_Handling_In_Python.ipynb',
    '20_File_Handling_In_Python.ipynb',
    '21_Numpy_Library.ipynb',
    '22_Pandas_Series.ipynb',
    '23_Pandas_DataFrame.ipynb',
    '24_Matplotlib_Library.ipynb',
    '25_Seaborn_Library.ipynb'
]

# Initialize an empty notebook
merged_nb = nbformat.v4.new_notebook()

# Read and merge all notebooks
for notebook_file in notebook_files:
    file_path = os.path.join(folder_path, notebook_file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            merged_nb.cells.extend(nb.cells)
    else:
        print(f'File {file_path} not found. Skipping.')

# Write the merged notebook to a new file if it does not already exist
if not os.path.exists(merged_file):
    with open(merged_file, 'w', encoding='utf-8') as f:
        nbformat.write(merged_nb, f)
    print(f'Merged notebook saved to {merged_file}')
else:
    print(f'File {merged_file} already exists.')