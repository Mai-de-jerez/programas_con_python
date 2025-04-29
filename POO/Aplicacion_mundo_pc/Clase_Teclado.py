from Aplicacion_mundo_pc.Clase_Dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclado = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'ID: {self.id_teclado}, Marca: {self.marca}, '
                f'Tipo de Entrada: {self.tipo_entrada}')

# Código principal
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    print(teclado1)
    teclado2 = Teclado('Dell', 'Bluetooth')
    print(teclado2)