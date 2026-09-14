str='a'+'B'+'h' #op-> abh

#repeation oprateo

string='abhay'
# * use to cpie string multiple time
n= 2

string*n #op-> abhayabhay
#special case what if n=0
string*0 #op '' we will get empty string

#1. equlaity oprator ==  it return true if two string equle else false

'abhay'== 'abhay' #true
'Abhay'=='abhay' #op-> false

# 2 != not equal oprator it return true id 2 string not same 

'abhay'!='Abhay' #op-> true

#membership opration 1st "in " it retrun true id 1st oprend contained in 2nd oprand

print('ab' in 'abhay')
#op-> true
print('aby' in 'abhay') # op-> false becue aby sequenc ein abhay

#not in membership oprator 
print('aby' not in 'abhay') #op-> true not sequence

#string formatting oprator
#%d,%c,%s and more
age=23
print("my age id %d"%(age))

 