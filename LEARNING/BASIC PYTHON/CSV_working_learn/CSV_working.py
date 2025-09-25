import csv

with open ("D:\\Code C\\VS\\CSVLearning\\diem.csv", 'r', encoding='utf-8') as csv_diem :
    diem_content = csv.reader(csv_diem) 
    sinhvien = {} #tao dictionary sinhvien
    next(diem_content) #xóa dòng đầu tiên (header)

    for line in diem_content :
        ten = line[0]
        tb = (round((float(line[1]) + float(line[2]) + float(line[3])) / 3, 2))
        sinhvien.update({ten : tb}) #thêm tên và TB vào dict sinhvien

    with open ("D:\\Code C\\VS\\CSVLearning\\result.csv", 'w', newline = '', encoding='utf-8') as csv_result :
        writer = csv.writer(csv_result) #tạo đối tượng writer, tương tác với đối tượng này sẽ là tương tác với csv_writer
        writer.writerow(['ten', 'tb']) #thêm dòng đầu tiên vào result
        writer.writerows([[ten, tb] for ten, tb in sinhvien.items()]) #list comprehension
        #sinhvien.items() trả về [(a,a0), (b,b0), (c,c0)]
        #for ten,tb in sinhvien.items() là lặp qua từng cặp ten, tb - a,a0 trong sinhvien.items()
        #[ten, tb] là 1 list, ghi ra nội dung trong list đó được tạo từ for ở trên