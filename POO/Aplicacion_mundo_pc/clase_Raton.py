from Aplicacion_mundo_pc.Clase_Dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_raton = 0
    def __init__(self, marca, tipo_entrada):
        Raton.contador_raton += 1
        self.id_raton = Raton.contador_raton
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada (otra forma de ponerlo)
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'ID: {self.id_raton}, Marca: {self.marca}, '
                f'Tipo de Entrada: {self.tipo_entrada}')

# Código principal
if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
    raton2 = Raton('Acer', 'Bluetooth')
    print(raton2)