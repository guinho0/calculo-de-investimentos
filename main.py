def juro(c,i,t):
    m = c * (1+i)**t
    return m
def main():
    ir = 0
    c = float(input("capital inicial: "))
    i = float(input("indice em %: "))
    i = i/100
    t = int(input('taxa: '))
    p = input('sua taxa está em anos ou em meses? aa ou am? ')
    if p == "aa":
        i = i
    if p == "am":
        i = i/12
    if t < 6:
        ir = 0.225
    if t > 6 and t <= 12:
        ir = 0.2
    if t > 12 and t <= 24:
        ir = 0.175
    if t > 24:
        ir = 0.15
    

    vbruto = juro(c,i,t)
    juros = vbruto-c
    vliquido = vbruto - ir*juros
    print(f'Valor Bruto = {vbruto:.2f}')
    print(f'Valor Liquido = {vliquido:.2f}')
    return 0
main()