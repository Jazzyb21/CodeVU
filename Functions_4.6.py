def computePay(hr, rate):
    if floatHours > 40 :
        reg = floatHours * floatRate
        overTime = (floatHours - 40.0) * (floatRate * 0.5)
        finalPay = reg + overTime
    else:
        finalPay = floatHours * floatRate
    return finalPay

counter = 0
while counter < 3:
    try:
        hours = input("Enter Hours: ")
        rate = input("Enter Rate: ")
        floatHours = float(hours)
        floatRate = float(rate)
        finalPay = computePay(floatHours, floatRate)
        print("Pay:", finalPay)
    except:
          
        if counter == 2:
            print('Please try again later.')
        else:
            print('Please enter a valid number(s).')
        counter += 1  



    
    