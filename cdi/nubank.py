def main():#100%cdi
    cdi = 0
    c = float(input('capital inicial: '))
    #i = float(input('indice: '))
    t =  int(input('taxa(aa/am): '))
    p = input('sua taxa é anual ou mensal? aa ou am?')
    if p == "am":
        cdi = 0.0107
    if p == "aa":
        cdi = 0.1114
    m = c*(1+cdi)**t
    print(f'valor bruto (sem impostos) == {m:.2f}')
    
    lucro = m-c
    ir = 0.225
    lucro = lucro -  lucro*ir
    m = c+lucro

    print(f'valor total = {m:.2f} e lucro de {lucro:.2f}')
    print('considerando o imposto de renda')
 
    
    return 0
main()