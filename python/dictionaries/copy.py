#assignment oprator can be usd to copy immutable obket

x=10
y=x

id(x)=id(y) #op= true

#if we update y then x remain uneffates becus it immutable 

#if 
y=20
y #op=20
x# op=10

car_dict={'brand':'tata','model':'siara'}

car_cpy=car_dict
car_cpy['model']='strom'
#same object will be update becuse it ia mutabel

#cpu mutable object using copy method so change in one not afet in other

car_copy=car_dict.copy()

car_copy['model']='nano'
#now the car dict wil not be upadte


#craeting copy isng dict name
#syntext= dict_name2=dict(dict_name1)

car_kopy=dict(car_dict) #dictony get copied
