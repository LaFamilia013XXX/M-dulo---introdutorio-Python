# Reforcando tudo em python é um objeto;

a = 'A'
b = 'B'
c = 1.1213124

formato = 'a={nome1}, b={nome2}, c={nome3:.10f}, k={nome4}'.format(nome1=a, nome2=b, nome3=c, nome4='1223'); #Um bom filho a casa retorna;
# Parâmetro nomeado, é quando você da nome para na criação/chamada das funções;

print(formato);
 
nome = "luiz";
idade = 23;
formato = '{0} tem {1} anos'.format(nome, idade); # Cada argumento enviado tem o seu Indíce onde neste caso você poderá controlar a ordem de quem aparece no formt();
print(formato);