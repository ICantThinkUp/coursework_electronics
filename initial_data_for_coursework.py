class Transformer:
    def __init__(self,
    U_c,
    circuit,
    U_21,
    U_31,
    U_32,
    U_22,
    I_21,
    I_22,
    I_31,
    I_32,
    sizeType,
    steelGrade):
        # напряжение питающей электросети
        self.U_c = U_c

        # вид схемы
        self.circuit = circuit

        # напряжения вторичных обмоток
        self.U_21 = U_21
        self.U_31 = U_31
        self.U_32 = U_32
        self.U_22 = U_22

        # токи вторичных обмоток, работающих в течение двух полупериодов I_2k
        # или одного полупериода I_3k
        self.I_21 = I_21
        self.I_22 = I_22
        self.I_31 = I_31
        self.I_32 = I_32

        self.sizeType = sizeType
        self.steelGrade = steelGrade

class Stabilizer:
    def __init__(self,
    U_in,
    a_max,
    a_min,
    U_out,
    I_H_max,
    I_H_min,
    k_steel_U,
    U_out_m):
        self.U_in = U_in
        self.a_max = a_max
        self.a_min = a_min
        self.U_out = U_out
        self.I_H_max = I_H_max
        self.I_H_min = I_H_min
        self.k_steel_U = k_steel_U
        self.U_out_m = U_out_m

class Recrifiler:
    def __init__(self,
    r_tr,
    U_o,
    I_o,
    B_m):
        self.r_tr = r_tr
        self.U_o = U_o
        self.I_o = I_o
        self.B_m = B_m

# VARIANT 01 - ARAPOVA 
# first figure of variant
transformer = Transformer(220, "a", 6, 12, 12, 0, 2, 0, 0.5, 0.5, "S", 3411)
stabilizer = Stabilizer(25, 0.1, 0.11, 16, 1, 0.5, 100, 0.1)
# last figure of variant
recrifiler = Recrifiler(1.1, 6, 2, 1.5)

initialValuesOfVariant = {"transformer": transformer,
                          "stabilizer": stabilizer,
                          "recrifiler": recrifiler}

