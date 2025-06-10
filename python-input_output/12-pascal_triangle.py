def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # İlk sətr
    
    for i in range(1, n):  # 1-dən n-ə qədər sətrlər
        prev_row = triangle[-1]  # Əvvəlki sətr
        new_row = [1]  # Yeni sətrin ilk elementi
        
        # Aradakı elementləri hesabla
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        new_row.append(1)  # Yeni sətrin son elementi
        triangle.append(new_row)  # Yeni sətri əlavə et
    
    return triangle

