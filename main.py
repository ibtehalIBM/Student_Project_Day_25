from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob('txt_files/*.txt')
pdf = FPDF(orientation='p', unit='mm', format='A4')
txt = ''
for file_path in filepaths:
    print(file_path)


    pdf.add_page()
    pdf.set_font(family='Times', style='b', size=24)
    file_name = Path(file_path).stem
    pdf.cell(w=0, h=12, txt=f'{file_name}', align='L', ln=1)
    # file_name_withoutextention = file_name.split('.')[0]

    # df = pd.read_csv(file_path, sep=' ')
    # for index, row in df.iterrows():
    #     txt += row
    with open(file_path,'r') as file:
        txt = file.read()
    print(txt)
    pdf.set_font(family='Times',  size=12)
    pdf.multi_cell(w=0, h=6, txt=f'{txt}', align='L')
    # pdf.set_font(family='Times', style='', size=18)
    # pdf.cell(w=0, h=9, txt=f'{txt}', align='L', ln=1)
pdf.output(f'pdfs/animals.pdf')
