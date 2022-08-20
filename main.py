from ast import ClassDef
from inspect import classify_class_attrs
from pyclbr import Class
from pydoc import classname
from types import ClassMethodDescriptorType
from kivy.app import App
from mainwidget import MainWidget
from kivy.lang.builder import Builder

class MainApp(App):
    """
    Classe com o aplicativo
    """
    def build(self):
        """
        Metodo que gera o aplicativo com o main widget
        """
        self._widget = MainWidget(scan_time=1000, server_ip='127.0.0.1', server_port=502,
        modbus_addrs = {
                'estado_mot': {'addr':800, 'tipo': 'coil', 'mult': None},
                'freq_des': {'addr': 799, 'tipo': 'hold', 'mult': 1},
                't_part': {'addr': 798, 'tipo': 'hold', 'mult': 10},
                'freq_mot': {'addr': 800, 'tipo': 'input', 'mult': 10},
                'tensao': {'addr': 801, 'tipo': 'input', 'mult': 1},
                'rotacao': {'addr': 803, 'tipo': 'input', 'mult': 1},
                'pot_entrada': {'addr': 804, 'tipo': 'input', 'mult': 10},
                'corrente': {'addr': 805, 'tipo': 'input', 'mult': 100},
                'temp_estator': {'addr': 806, 'tipo': 'input', 'mult': 10},
                'vz_entrada': {'addr': 807, 'tipo': 'input', 'mult': 100},
                'nivel': {'addr': 808, 'tipo': 'input', 'mult': 10},
                'nivel_h': {'addr': 809, 'tipo': 'discrete', 'mult': None},
                'nivel_1': {'addr': 810, 'tipo': 'discrete', 'mult': None},
                'Solenoide 1': {'addr': 801, 'tipo': 'coil', 'mult': None},
                'Solenoide 2': {'addr': 802, 'tipo': 'coil', 'mult': None},
                'Solenoide 3': {'addr': 803, 'tipo': 'coil', 'mult': None},

            
        },
        )
        return self._widget
    # def on_stop(self):
    #     """"
    #     Metodo executado quando a alicaçao e fechada
    #     """
    #     self._widget.stopRefresh()
    
if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv", encoding="utf-8").read(), rulesonly=True)
    # Builder.load_string(open("popups.kv", encoding="utf-8").read(), rulesonly=True)
    MainApp().run()