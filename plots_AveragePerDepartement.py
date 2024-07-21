import matplotlib.pyplot as plt
from plots_forAllTypeRentDepartement import getAverageRentValue


res_departement, res_loyer = getAverageRentValue()
plt.figure(figsize=(20, 3), dpi=100)
plt.scatter(res_departement, res_loyer)
plt.show()