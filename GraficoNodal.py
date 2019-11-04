import numpy as np
import matplotlib.pyplot as plt

# Tamanho da Matrizes Verificadas
data_tammat    = [100,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000]

# Tempos de cada matriz
#data_lingC      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#data_lingC_GPU  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
data_lingPy     = [0.1274585723876953,4.881241321563721,23.764952182769775,59.09815955162048,120.97146511077881,182.7194447517395,288.8846502304077,441.4162542819977,619.8696622848511,831.1901185512543,1111.0693798065186,1411.9509959220886,1809.770141839981,2146.555803537369,2559.5322494506836,3040.410006046295,6632.7703993320465]
data_lingPy_GPU = [0.02337193489074707,1.186615228652954,7.5387067794799805,23.897207736968994,52.77848839759827,97.07695484161377,176.87205576896667,266.1067771911621,408.5240857601166,560.6376740932465,761.988275051117,908.8802387714386,1426.7386012077332,1642.3178284168243,1789.086995601654,2208.0520560741425,3265.033314943314]


# Gerar a linha da matriz em ordem
x = 10*np.array(range(len(data_tammat)))

# Linha para gerar o grafico
#plt.plot(data_tammat, data_lingC, color='blue')   
#plt.plot(data_tammat, data_lingC_GPU, color='aqua') 
plt.plot(data_tammat, data_lingPy, color='springgreen')   
plt.plot(data_tammat, data_lingPy_GPU, color='red') 

# Plotando as bolinha nos pontos
#plt.plot(data_tammat, data_lingC, 'go', color='blue')  
#plt.plot(data_tammat, data_lingC_GPU, 'go', color='aqua') 
plt.plot(data_tammat, data_lingPy, 'go', color='springgreen')   
plt.plot(data_tammat, data_lingPy_GPU, 'go', color='red') 

# Titulo e legenda 
plt.title("Tempo de matrizes usando linguagens:")
plt.grid(True)
plt.xlabel("Tamanho matriz")
plt.ylabel("Tempo (s)")
#plt.legend(['C', 'C com Gpu', 'Python', 'Python com Gpu'], loc=2)
plt.legend(['Python', 'Python com Gpu'], loc=2)
plt.show()

# Salvando as figura
plt.savefig('matriz-nodal.png')
plt.close()


i = 0
valormedido = 0
TotalCPU = 0
TotalGPU = 0
for nota in data_lingPy:
    valor = ((nota - data_lingPy_GPU[i]) / data_lingPy_GPU[i]) * 100
    valormedido = valor + valormedido
    #print(valor)
    print('Valor e percentual de ganho: ', nota - data_lingPy_GPU[i], ',      ' , str(valor) + ' %')    
    TotalCPU = TotalCPU + nota
    TotalGPU = TotalGPU + data_lingPy_GPU[i]
    i += 1


print(' ')   

print('Media CPU', TotalCPU/i)   
print('Media GPU', TotalGPU/i)   
print('Dif. Media', (TotalCPU/i) - (TotalGPU/i))

'''
valor = (((TotalCPU/i) - (TotalGPU/i)) / (TotalGPU/i)) * 100
print(str(valor) + ' %')
print(valormedido/18)
'''