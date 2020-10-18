#create Energy calculator function
def Energy(p,t):
    E = 0
    for i in range(len(p)):
        e = p[i]*t[i]
        if np.isnan(e) == True: #converts the last row from nan to 0 
            e = 0
        else:
            e
        E = E+e
    return print(str(E/60) + ' Wh') #divide result by 60 to convert to Wh