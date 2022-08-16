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
        self._widget = MainWidget()
        return self._widget
    
    #     self._widget = MainWidget(scan_time=1000, server_ip='127.0.0.1',server_port=502,
    #     modbus_addrs = {
    #         'fornalha': 1000,
    #         'gas_ref': 1001,
    #         'gasolina': 1002,
    #         'nafta': 1003,
    #         'querosene': 1004,
    #         'diesel': 1005,
    #         'oleo_lub': 1006,
    #         'oleo_comb': 1007,
    #         'residuos': 1008
    #     }    
    #     )
    #     return self._widget
    # def on_stop(self):
    #     """"
    #     Metodo executado quando a alicaçao e fechada
    #     """
    #     self._widget.stopRefresh()
    
if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv", encoding="utf-8").read(), rulesonly=True)
    # Builder.load_string(open("popups.kv", encoding="utf-8").read(), rulesonly=True)
    MainApp().run()