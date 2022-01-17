
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window


class Application(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 3
        self.window.__name__= "LesFutésAssurance"
        Window.clearcolor = (180 / 255, 71 / 255, 159 / 255, 1)

        self.choice = Label(
            text="Choix de la ville",
            font_size=20,
        )

        self.text_ville = Label(
            text="(en France) :",
            font_size=20,
        )
        ### liste des villes
        dropdown = DropDown()
        tab1 = Button(text="Paris", size_hint_y=None, height=44)
        tab1.bind(on_release=lambda tab1: dropdown.select(tab1.text))
        dropdown.add_widget(tab1)

        tab2 = Button(text="Nice", size_hint_y=None, height=44)
        tab2.bind(on_release=lambda tab2: dropdown.select(tab2.text))
        dropdown.add_widget(tab2)

        tab3 = Button(text="Lille", size_hint_y=None, height=44)
        tab3.bind(on_release=lambda tab3: dropdown.select(tab3.text))
        dropdown.add_widget(tab3)

        tab4 = Button(text="Strasbourg", size_hint_y=None, height=44)
        tab4.bind(on_release=lambda tab4: dropdown.select(tab4.text))
        dropdown.add_widget(tab4)

        self.mainbutton = Button(text="Cliquer pour choisir la ville")
        self.mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))


        self.user = Label(
            text="saisie du pivot",
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
            text="Saisie du cout fixes journalier",
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
            text="Saisie du chiffre d'affaire possible max journalier",
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

        self.saisie_datear = Label(
            text="Saisie de la date d'arrivée ",
            font_size=20,
        )

        self.text_datear = Label(
            text=" (en format jour/mois/année) :",
            font_size=20,
        )

        self.datear = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),

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
            text="impression DEVIS",
            bold=True,
            background_color=(0, 0, 1, 1)
        )

        self.devis.bind(on_press=self.callback2)

        self.devisretro = Button(
            text="impression RETROSPECTIVE",
            bold=True,
            background_color=(0, 0, 1, 1)
        )

        self.devisretro.bind(on_press=self.callback3)
        self.datedep = Label(
            text="saisie de la date de départ",
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


        self.window.add_widget(self.choice)
        self.window.add_widget(self.text_ville)
        self.window.add_widget(self.mainbutton)

        self.window.add_widget(self.nom)
        self.window.add_widget(self.text_nom)
        self.window.add_widget(self._nom)

        self.window.add_widget(self.datedep)
        self.window.add_widget(self.text_datedep)
        self.window.add_widget(self.dd)

        self.window.add_widget(self.saisie_datear)
        self.window.add_widget(self.text_datear)
        self.window.add_widget(self.datear)

        self.window.add_widget(self.user)
        self.window.add_widget(self.text_pivot)
        self.window.add_widget(self.pivot)

        self.window.add_widget(self.saisie_cout)
        self.window.add_widget(self.text_cout)
        self.window.add_widget(self.cout)

        self.window.add_widget(self.saisie_ca)
        self.window.add_widget(self.text_ca)
        self.window.add_widget(self.ca)



        self.window.add_widget(self.resultat_assureur)
        self.window.add_widget(self.devis)
        self.window.add_widget(self.devisretro)

        return self.window




    def callback1(self):   ## callback pour afficher la prime

        # Todo:  1 ére boucle if qui vérifiera que toutes les fonctions calculatrices marchent bien et que les paramétres sont correctes
                    ## on lance le calcul et on affiche la prime


                # 2 éme boucle
                    ## la sortie d'erreur


            pass;


    def callback2(self):    ## Todo: callback pour imprimer un devis


        pass;


    def callback3(self):  ## Todo: callback pour imprimer un devis retrospective


        pass;



if __name__ == "__main__":
    Application().run()



