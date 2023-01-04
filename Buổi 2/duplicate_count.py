def duplicate_count(text):
    #tạo biến chưa với giá trị bằng 0
    total = 0
    #tạo chuỗi rỗng chưa biến
    duplicates = {}
    #đến với từ đã chuyển đồng bộ chữ ko in hoa
    for character in text.lower():
        #Nếu có ký tự trong đó thì sẽ thêm vào chuỗi và đồng thời đếm cộng thêm 1
        if character in duplicates:
            duplicates[character] += 1
            #nếu thỏa mãn đk trên và có thêm ký tự trùng lặp và số từ trong mảng bé hơn 3 thì sẽ cộng thêm 1 vào biến đếm
            if duplicates[character] < 3:
                total += 1
            #nếu chỉ có 1 từ trong đó và không có giá trị trùng lặp sẽ gán giá trị bằng 1
        else:
            duplicates[character] = 1

    print(f'\nThere are {total} reoccurring characters.')
    for element in duplicates:
        if duplicates[element] > 1:
            print(f'\t"{element}" occurs {duplicates[element]} times.')


duplicate_count('aaaaaaabCccdeeEEefgg12334')