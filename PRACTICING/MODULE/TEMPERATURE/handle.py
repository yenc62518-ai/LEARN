total_temp = 0.0
total_time = 0
with open ('D:/Code C/VS/temperature/temp.txt', 'r') as f : 
    for line in f:
        # Tách thời gian và nhiệt độ
        time, temp = line.strip().split(', ') # kĩ thuật tuple unpacking
        ''' strip() : loại bỏ \n, TAB hoặc space thừa  
            split(', ') : tách chuỗi ra thành 2 phần dựa trên dải ", ". VD: 9:00:00, 32 -> ['9:00:00', '32'] (1 tuple)
            time và temp sẽ = 9:00:00 và 32, respectively
        '''
        if (float(temp)>31) :
            continue
        total_temp += float (temp)
        total_time+=1
avg_temp = total_temp/total_time if total_time>0 else 0
print (round(avg_temp, 2)) 