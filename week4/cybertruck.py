import matplotlib.pyplot as plt
import numpy as np
import os

plt.scatter([2024, 2025], [38965, 20237], color='black', label='Actual Full Year Sales')

####################################
# Problem 1 
# Build Linear Model from Two Points
data = [(2024,38965), (2025, 20237)]

t = np.array([0,1])
trucks = np.array([38965, 20237])

coeff_deg1 = np.polyfit(t, trucks, 1)
print("m,b: ", coeff_deg1)
print("2026: ", np.polyval(coeff_deg1,2))

plt.scatter([2026],[1508], color='purple', label="Linear Model Prediction" )
plt.scatter([2026],[3519], color='orange', marker='x', label="Q1 deliveries" )

# give years as line
t_dense = np.linspace(-0.2, 2.3, 200)

# plot years and model
plt.plot(t_dense+2024, np.polyval(coeff_deg1,t_dense),'--', color='blue', linewidth=2, label='Linear Fit (Degree 1)')

plt.legend()
plt.xlabel("Calendar Year")
plt.ylabel("Deliveries (Units)")
plt.title("Tesla Cybertruck Deliveries: Polynomial Fit & 2026 Projection")
 # plt.show()

##########################################
# Problem 2
# Build Quadratic Function
#
# Complete the three time points using the initial
# two years
data = [(2024,38965), (2025, 20237)]

# give value to Q1 sales below
# supply the quarterly data
Q1 = 3519
data = data + [(2026,4*Q1)]

t_extended = np.array([0, 1, 2])
trucks_extended = np.array([38965, 20237, 4*Q1])

# Uncomment after Q1 is correctly assigned
coeffs_deg2 = np.polyfit(t_extended, trucks_extended, 2)
print("quadratic coeffs(a,b,c): ", coeffs_deg2)
print("2026 (imputed from Q1*4): ", trucks_extended[2])

plt.scatter([2026], [trucks_extended[2]], color='red', label="Quadratic Prediction")
plt.plot(2024 + t_dense, np.polyval(coeffs_deg2,t_dense), '-', color='darkgreen', linewidth=2.5, label='Quadratic Fit (Degree 2)')



plt.title('Tesla Cybertruck Deliveries: Polynomial Fit & 2026 Projection', fontsize=13, fontweight='bold')
plt.xlabel('Calendar Year', fontsize=11)
plt.ylabel('Deliveries (Units)', fontsize=11)
plt.xticks([2024, 2025, 2026])
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')



# Note - about setting the correct filesystem path:
#  the path variable set below,
#  used to determine where files are to be saved,
#  assumes that the "fall2026c200" directory/folder is located
#  *exactly* as shown in lecture slides.
# 
# TODO: if your "fall2026c200" directory is in a different
#  location, you need to modify the path below accordingly.
# 
# Warning - about finding the saved file on your system:
#  if you don't set a correct path for your system,
#  your Python code may not even crash, instead it may save a
#  file that isn't correctly named,
#  nor correctly located on your system.


# Windows filesystem path here:
path = "C:\\fall2026c200\\week4\\"

# Mac and Linux filesystem path here:
# first, place a # in front of the Windows line above, and
# delete the # (and the space after it) on the line below:
# path = os.path.expanduser("~/fall2026c200/week4/")


plt.savefig('/Users/tyrosenbaum/Desktop/fall2026c200/week4/cybertruck.png', dpi=300, bbox_inches='tight')
plt.show()
