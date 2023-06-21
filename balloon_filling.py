'''
Macy Mosier
6/18/23
USIP VI Flight Ops
Python 3.10.5


The point of this script is to calculate the amount of helium needed to launch a balloon for a given temperature, balloon, and payload weight.

I've assumed the attraction b/t molceules is negligible b/c He is a noble gas, haven't taken into account variable payload weight, 
and that the can contains almost 100% He.

'''


# outside temperature in celsius
temp_C = 25

# converts celsius to kelvin
temp_K = temp_C + 273.15

# helium can volume (L)
v_can = 100

# pressure of helium can before filling (I think the valve uses mmHg ??)
p0_can = 10

# universal gas constant (mmHg*L/K/mol)
R = 62.3656

# b*n is the correction of ideal gas law for the amount of space the He mlcs take up
# PV = nRT --> P(V - n*b) = nRT

# b is some experimentally determined constant (L/mol)
b = .0237

# calculates the initial quantity of moles in the can
mol0 = p0_can*v_can/(R*temp_K + b*p0_can)

# final amount of moles in the can, gonna be determined by amount of lift needed, i think
# later, this calculation will take into account weight of payload etc 
molf = ?????????




# calculates final pressure of can
p_fnal_can = p0_can + R*temp_K*(molf/(v_can-molf*b) - mol0/(v_can - mol0*b))

print(f'{(p_final_can - p0_can):.1f} mmHgs of pressure need to be released so the final pressure is {p_final_can:.1f} ')