nums = []
moda = {}
print("Escreva X pra confirmar")
while True:
    nums.append(input("Adicionar Numero: "))
    if nums[-1] == 'X' or nums[-1] == 'x':
        nums.pop(-1)
        break
    try:
        nums[-1] = int(nums[-1])
    except:
        print("Insira Apenas Numeros!")
        nums.pop(-1)

nums.sort()

if nums == []:
    print("Lista Vazia!")
divisao = len(nums)
if divisao%2 == 0:
    print(f'Mediana = {nums[int(divisao/2 -1)]} e {nums[int(divisao/2)]}')
else:
    print(f"Mediana: {nums[int(divisao/2)]}")

maisRep = 0
num = 0
for i in nums:
    aux = nums.count(i)
    if aux > maisRep:
        maisRep = aux
        num = i

print(f'Moda: {num}')
print(f'Média: {sum(nums)/divisao}')
