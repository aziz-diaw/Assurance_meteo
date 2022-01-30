
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
import Calculateur.calcul
from fpdf import FPDF


class PDF1(FPDF):                                ### classe pdf pour le devis
    def header(self):
        # Logo
        self.image('herve-francois-dos-a-dos.png', 10, 8, 25)
        # signature
        self.image('signature.png', 170, 170, 30)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(100, 10, 'Devis de votre assurance', border=True, ln=1, align='C')
        # Line break
        self.ln(20)

class PDF2(FPDF):                                  ### classe pdf pour l'analyse rétrospective
    def header(self):
        # Logo
        self.image('herve-francois-dos-a-dos.png', 10, 8, 25)
        # signature
        self.image('signature.png', 170, 140, 30)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(100, 10, 'Analyse rétrospective', border=True, ln=1, align='C')
        # Line break
        self.ln(20)

class Application(App,FPDF):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 3
        self.window.__name__= "LesFutésAssurance"
        Window.clearcolor = (180 / 255, 71 / 255, 159 / 255, 1)

        self.choice1 = Label(
            text="Choix de la ville",
            font_size=20,
        )

        self.text_ville = Label(
            text="(en France) :",
            font_size=20,
        )
        ### liste des villes
        dropdown1 = DropDown()
        tab1 = Button(text="Paris", size_hint_y=None, height=44)
        tab1.bind(on_release=lambda tab1: dropdown1.select(tab1.text))
        dropdown1.add_widget(tab1)

        tab2 = Button(text="Nice", size_hint_y=None, height=44)
        tab2.bind(on_release=lambda tab2: dropdown1.select(tab2.text))
        dropdown1.add_widget(tab2)

        tab3 = Button(text="Lille", size_hint_y=None, height=44)
        tab3.bind(on_release=lambda tab3: dropdown1.select(tab3.text))
        dropdown1.add_widget(tab3)

        tab4 = Button(text="Marseille", size_hint_y=None, height=44)
        tab4.bind(on_release=lambda tab4: dropdown1.select(tab4.text))
        dropdown1.add_widget(tab4)

        self.mainbutton1 = Button(text="Cliquer pour choisir la ville")
        self.mainbutton1.bind(on_release=dropdown1.open)
        dropdown1.bind(on_select=lambda instance, x: setattr(self.mainbutton1, 'text', x))

        ########################## ### liste des annees

        self.choice2 = Label(
            text="Choix de l'année d'analyse rétrospective",
            font_size=20,
        )

        self.text_annee = Label(
            text="( sur les 4 derniéres années) :",
            font_size=20,
        )
        dropdown = DropDown()
        tab1 = Button(text="2021", size_hint_y=None, height=44)
        tab1.bind(on_release=lambda tab1: dropdown.select(tab1.text))
        dropdown.add_widget(tab1)

        tab2 = Button(text="2020", size_hint_y=None, height=44)
        tab2.bind(on_release=lambda tab2: dropdown.select(tab2.text))
        dropdown.add_widget(tab2)

        tab3 = Button(text="2019", size_hint_y=None, height=44)
        tab3.bind(on_release=lambda tab3: dropdown.select(tab3.text))
        dropdown.add_widget(tab3)

        tab4 = Button(text="2018", size_hint_y=None, height=44)
        tab4.bind(on_release=lambda tab4: dropdown.select(tab4.text))
        dropdown.add_widget(tab4)

        self.mainbutton2 = Button(text="Cliquer pour choisir l'année")
        self.mainbutton2.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton2, 'text', x))





        self.user = Label(
            text="Saisie du niveau pl pivot",
            font_size=20,
        )

        self.text_pivot = Label(
            text=" (en millimétres) :",
            font_size=20,
        )

        self.pivot = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
            input_filter="int"
        )


        self.saisie_cout = Label(
            text="Saisie des coûts fixes",
            font_size=20,
        )

        self.text_cout = Label(
            text=" (en euros) : ",
            font_size=20,
        )

        self.cout = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
            input_filter="int"
        )

        self.saisie_ca = Label(
            text="Chiffre d'affaire max journalier",
            font_size=20,
        )

        self.text_ca = Label(
            text=" (en euros) : ",
            font_size=20,
        )

        self.ca = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
            input_filter="float"
        )


        self.nom = Label(
            text="Saisie du nom de l'assuré ",
            font_size=20,
        )

        self.text_nom = Label(
            text=" (en lettres) : ",
            font_size=20,
        )

        self._nom = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
        )

        self.resultat_assureur = Button(
            text="Cliquer pour afficher la prime",
            bold=True,
            background_color=(0, 1, 1, 1)
        )

        self.resultat_assureur.bind(on_press=self.callback1)

        self.devis = Button(
            text="Impression DEVIS",
            bold=True,
            background_color=(0, 0, 1, 1)
        )

        self.devis.bind(on_press=self.callback2)

        self.devisretro = Button(
            text="Analyse RETROSPECTIVE",
            bold=True,
            background_color=(0, 0, 1, 1)
        )

        self.devisretro.bind(on_press=self.callback3)
        self.datedep = Label(
            text="Saisie de la date de départ",
            font_size=20,
        )

        self.text_datedep = Label(
            text=" (en format jour/mois/année) :",
            font_size=20,
        )

        self.dd = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),

        )


        self.window.add_widget(self.choice1)
        self.window.add_widget(self.text_ville)
        self.window.add_widget(self.mainbutton1)


        self.window.add_widget(self.nom)
        self.window.add_widget(self.text_nom)
        self.window.add_widget(self._nom)

        self.window.add_widget(self.datedep)
        self.window.add_widget(self.text_datedep)
        self.window.add_widget(self.dd)


        self.window.add_widget(self.user)
        self.window.add_widget(self.text_pivot)
        self.window.add_widget(self.pivot)

        self.window.add_widget(self.saisie_cout)
        self.window.add_widget(self.text_cout)
        self.window.add_widget(self.cout)

        self.window.add_widget(self.saisie_ca)
        self.window.add_widget(self.text_ca)
        self.window.add_widget(self.ca)

        self.window.add_widget(self.choice2)
        self.window.add_widget(self.text_annee)
        self.window.add_widget(self.mainbutton2)

        self.window.add_widget(self.resultat_assureur)
        self.window.add_widget(self.devis)
        self.window.add_widget(self.devisretro)

        return self.window


    def choix_ville(self):
        if self.mainbutton1.text == "Nice":
            return "nice"
        if self.mainbutton1.text == "Paris":
            return "paris"
        if self.mainbutton1.text == "Lille":
            return "lille"
        if self.mainbutton1.text == "Marseille":
            return "marseille"

    def choix_annee(self):
        if self.mainbutton2.text == "2021":
            return "2021"
        if self.mainbutton2.text == "2020":
            return "2020"
        if self.mainbutton2.text == "2019":
            return "2019"
        if self.mainbutton2.text == "2018":
            return "2018"

    def callback1(self,instance):   ## callback pour afficher la prime

        if int(self.pivot.text) < 0 | int(self.cout.text) < 0 | int(self.ca.text) < 0:
            self.resultat_assureur.text = " Erreur dans les paramétres saisis"
        else:
            self.resultat_assureur.text = str(Calculateur.calcul.prime(self.choix_ville(),int(self.pivot.text),int(self.cout.text)))




    def callback2(self,instance):    ##callback pour imprimer un devis

        pdf = PDF1('P', 'mm', 'Letter')

        # get total page numbers
        pdf.alias_nb_pages()

        # Set auto page break
        pdf.set_auto_page_break(auto=True, margin=15)

        # Add Page
        pdf.add_page()

        # specify font
        pdf.set_font('helvetica', 'BIU', 16)

        pdf.set_font('times', '', 12)

        pdf.cell(0, 30, f'Bonjour monsieur/madame ' + self._nom.text + ',', ln=1)

        pdf.cell(0, 10,
                 f'Vous avez demandé une assurance météorologique chez notre société les futés avec comme paramètres : ',
                 ln=1)
        pdf.cell(0, 10, f'Chiffre d\'affaire journalier : ' + self.ca.text, ln=1)
        pdf.cell(0, 10, f'Couts fixes: ' + self.cout.text, ln=1)
        pdf.cell(0, 10, f'Date de souscription :  ' + self.dd.text, ln=1)
        pdf.cell(0, 10, f'Ville de localisation du commerce : ' + self.mainbutton1.text, ln=1)
        pdf.cell(0, 10, f'Niveau de pluviométrie pivot : ' + self.pivot.text, ln=1)
        pdf.cell(0, 30,
                 f'Après étude de vos données et calculs, nous vous proposons une prime pour votre assurance s\'élevant au montant de ',
                 ln=1)
        pdf.cell(0, 10, str(int(Calculateur.calcul.prime(self.choix_ville(),int(self.pivot.text),int(self.cout.text)))) + f' Euros.', ln=1)
        filename="Devis_"+ str(self._nom.text) + ".pdf"
        pdf.output(name=filename,dest= 'F')



    def callback3(self,instance):  ## Todo: callback pour imprimer un devis retrospective

        pdf = PDF2('P', 'mm', 'Letter')

        # get total page numbers
        pdf.alias_nb_pages()

        # Set auto page break
        pdf.set_auto_page_break(auto=True, margin=15)

        # Add Page
        pdf.add_page()

        # specify font
        pdf.set_font('helvetica', 'BIU', 16)

        pdf.set_font('times', '', 12)

        pdf.cell(0, 30, f'Bonjour monsieur/madame ' + self._nom.text + ',', ln=1)

        pdf.cell(0, 10, f'Vous avez demandé une analyse rétrospective chez notre société les futésassurances pour l\'année ' + self.choix_annee() + '.', ln=1)
        pdf.cell(0, 10, f'En ' + self.choix_annee() + ', un client habitant à ' + str(self.choix_ville()) + ' non assuré, avec un niveau de pluie journalier pivot de ' + self.pivot.text + ' mm, aurait eu ', ln=1)
        pdf.cell(0, 10, f'un résultat annuel de ' + str(int(Calculateur.calcul.resultas_non_ass_ville(self.choix_ville(),self.choix_annee(),float(self.ca.text),float(self.cout.text),float(self.pivot.text)))) + ' Euros. Cependant, s\'il s\'était assuré en ' + self.choix_annee() + ', il aurait payé au début de l\'année '+ self.choix_annee() + ' une' , ln=1)
        pdf.cell(0, 10, f'prime annuelle de ' + (str(int(Calculateur.calcul.prime_periode(self.choix_ville(),float(self.pivot.text),float(self.cout.text), self.choix_annee())))) + ' Euros. Sachant que son résultat annuel protégé par l\'assurance aurait été de ' + str(int(Calculateur.calcul.resultas_ass_ville(self.choix_ville(),self.choix_annee(),float(self.ca.text),float(self.cout.text),float(self.pivot.text)))) + ' Euros,' + ' il ', ln=1)
        pdf.cell(0, 10, f'aurait eu finalement un résultat annuel à hauteur de ' + str(int(Calculateur.calcul.resultas_ass_ville(self.choix_ville(),self.choix_annee(),float(self.ca.text),float(self.cout.text),float(self.pivot.text))) - int(Calculateur.calcul.prime_periode(self.choix_ville(),float(self.pivot.text),float(self.cout.text), self.choix_annee()))) + ' Euros s\'il s\'était assuré.', ln=1)
        filename = "AnalyseRetro_" + str(self._nom.text) + "_" + self.choix_annee() + ".pdf"
        pdf.output(name=filename, dest='F')


if __name__ == "__main__":
    Application().run()



