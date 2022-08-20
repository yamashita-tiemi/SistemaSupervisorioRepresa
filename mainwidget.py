from multiprocessing.sharedctypes import Value
import random
from kivy.uix.boxlayout import BoxLayout
# from popups import ModbusPopup, ScanPopup, DataGraphPopup, HistGraphPopup
from pyModbusTCP.client import ModbusClient
from kivy.core.window import Window
from threading import Thread
from time import sleep
from datetime import datetime
# from timeseriesgraph import TimeSeriesGraph
# from bdhandler import BDHandler
from kivy_garden.graph import LinePlot

class MainWidget(BoxLayout):
    """
    Widget principal da aplicaçao
    """
    _updateThread = None
    _updateWidgets = True
    _tags = {}
    _max_points = 20

    def __init__(self, **kwargs):
        """
        Construtor do widget principal
        """
        super().__init__()
        self._scan_time = kwargs.get('scan_time')
        self._serverIP = kwargs.get('server_ip')
        self._serverPort = kwargs.get('server_port')
        # self._modbusPopup = ModbusPopup(self._serverIP,self._serverPort)
        # self._scanPopup = ScanPopup(scantime=self._scan_time)
        self._modbusClient = ModbusClient(host=self._serverIP,port=self._serverPort)
        self._funcs = {
            'coil': self._modbusClient.read_coils,
            'hold': self._modbusClient.read_holding_registers,
            'input': self._modbusClient.read_input_registers,
            'discrete': self._modbusClient.read_discrete_inputs,
        }
        self._meas = {}
        self._meas['timestamp'] = None
        self._meas['values'] = {}
        self._tags = kwargs.get('modbus_addrs')
        for key,value in kwargs.get('modbus_addrs').items():
            if key == 'nivel':
                plot_color = (0,0,1,1)
            else:
                plot_color = (random.random(),random.random(),random.random(),1)
            value['color']= plot_color
        # self._graph = DataGraphPopup(self._max_points, self._tags['fornalha']
        # ['color'])
        # self._hgraph = HistGraphPopup(tags=self._tags)
        # self._db = BDHandler(kwargs.get('db_path'), self._tags)

    def readData(self):
        """
        Metodo para a leitura dos dados por meio do protocolo MODBUS
        """
        self._meas['timestamp'] = datetime.now()
        for key,value in self._tags.items():
            self._meas['values'][key] = self._funcs[value['tipo']](value['addr'],1)[0]
            if value['mult'] is not None:
                self._meas['values'][key] /= value['mult']