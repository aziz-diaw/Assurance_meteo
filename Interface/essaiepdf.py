from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('herve-francois-dos-a-dos.png', 10, 8, 25)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(100, 10, 'Devis de votre commande', border=True, ln=1, align='C')
        # Line break
        self.ln(20)

# Create a PDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 15)

#Add Page
pdf.add_page()

# specify font
pdf.set_font('helvetica', 'BIU', 16)

pdf.set_font('times', '', 12)

pdf.cell(0, 10, f' Bonjour monsieur/madame X', ln=1)

pdf.output('pdf_ass.pdf')

#Todo: rajouter tous le text grace aux cells pour avoir un contrat rempli et rajouter une photo de la signature du groupe

