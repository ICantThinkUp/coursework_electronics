from initial_data_for_coursework import initialValuesOfVariant
import math

POWER_SUPPLY_CURRENT_FREQUENCY = 50

def calculateTransformerByTypeA(values):
    print("Максимальное значение габаритной мощности вторичных обмоток:")
    overallPowerOfSecondaryWindings = (values.U_21 * values.I_21) + 2 * \
        (values.U_31 * values.I_31 + values.U_32 * values.I_32)
    print(overallPowerOfSecondaryWindings, " ВА")

    print("Приближенное значение КПД:")
    efficiencyFactor = (1 + 0.14 *
                        pow((2 * POWER_SUPPLY_CURRENT_FREQUENCY / 50 - 2), 1/4)) * \
                        math.tanh(1.14 + 0.024 * \
                        math.sqrt(overallPowerOfSecondaryWindings))
    print(efficiencyFactor)

    print("Расчетная мощность трансформатоора:")
    ratedPowerOfTheTransformer = (math.sqrt(2) / (4 * efficiencyFactor)) * (
                                    math.sqrt(2) * (1 + efficiencyFactor) *
                                    (values.U_21 * values.I_21) +
                                    2 * (1 + math.sqrt(2 * efficiencyFactor)) *
                                    (values.U_31 * values.I_31 +
                                    values.U_32 * values.I_32)
                                )
    print(ratedPowerOfTheTransformer)

    print("Тип конструкции ленточных сердечников: ",
          values.sizeType)

    print("Вид стали: ", values.steelGrade)
    print("Тип конструкции ленточных сердечников: ",
          values.steelGrade)

    print("Толщина ленты, мм: ")
    beta_c = float(input()) # 37.5

    print("Коэффициент заполнения сталью: ")
    k_c = float(input()) # 0.93

    print("Плотность тока: ")
    currentDensity = float(input()) # 2

    print("Коэффициент заполнения окна: ")
    k_o = float(input()) #0.25

    print("Коэффициент формы: ")
    k_f = float(input())  # 1.1

    print("Расчетный габаритный параметр трансформатора")

    print("Магнитная индукция: ")
    B_m = float(input())  # 1.5

    print("Типоразмер магнитопровода: ")
    magneticCircuitStandardSize = (50 * ratedPowerOfTheTransformer) / \
                                  (POWER_SUPPLY_CURRENT_FREQUENCY * B_m * currentDensity *
                                   k_c * k_o * k_f)
    print(magneticCircuitStandardSize)

    print("Относительное падение напряжения: ")
    dU = float(input()) # 0.11

    print("Выбор типоразмера магнитопровода: ")

    print("Сечение окна магнитопровода: ")
    S_o = "" #

    print("Сечение сердечника магнитопровода: ")
    S_c = ""

def calculateTransformerByTypeB():
    print("Type B")

def calculateTransformerByTypeC():
    print("Type C")

methodsForCalculatingTheTransformer = {
    "a": calculateTransformerByTypeA,
    "b": calculateTransformerByTypeB,
    "c": calculateTransformerByTypeC
}

def getTypeOfElectricalCircuit(transformer):
    return transformer.circuit

def calculateMainParametersOfTheTransformerAtAGivenLoad():
    transformersValues = initialValuesOfVariant["transformer"]
    typeOfElectricalCircuitOfTransformer = getTypeOfElectricalCircuit(transformersValues)
    flowCalcutalions = methodsForCalculatingTheTransformer[typeOfElectricalCircuitOfTransformer]

    flowCalcutalions(transformersValues)

def calculateTheRectifierDeviceOnActiveCapacitiveLoad():
    pass

def calculateOfTheCompensationStabilizerWithContinuousVoltageRegulation():
    pass

if __name__ == '__main__':
    calculateMainParametersOfTheTransformerAtAGivenLoad()
    calculateTheRectifierDeviceOnActiveCapacitiveLoad()
    calculateOfTheCompensationStabilizerWithContinuousVoltageRegulation()